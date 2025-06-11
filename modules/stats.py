import sqlite3
import sys
import time
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from functools import cached_property
from textwrap import dedent
from typing import TYPE_CHECKING, Iterable, Optional

from modules.battle_state import BattleOutcome, EncounterType
from modules.console import console
from modules.context import context
from modules.fishing import FishingAttempt, FishingResult
from modules.items import Item, get_item_by_index
from modules.pokemon import Pokemon, get_species_by_index, Species, get_unown_letter_by_index, get_unown_index_by_letter

if TYPE_CHECKING:
    from modules.encounter import EncounterInfo
    from modules.profiles import Profile


current_schema_version = 2


class StatsDatabaseSchemaTooNew(Exception):
    pass


class BaseData:
    key: str
@@ -736,50 +736,77 @@ class StatsDatabase:
        ):
            self._longest_shiny_phase = self.current_shiny_phase
        self.current_shiny_phase = None
        for species_id in self._encounter_summaries:
            if self._encounter_summaries[species_id].is_same_species(encounter.pokemon):
                self.last_shiny_species_phase_encounters = self._encounter_summaries[species_id].phase_encounters

            encounter_summary = self._encounter_summaries[species_id]
            encounter_summary.phase_encounters = 0
            encounter_summary.phase_highest_iv_sum = None
            encounter_summary.phase_lowest_iv_sum = None
            encounter_summary.phase_highest_sv = None
            encounter_summary.phase_lowest_sv = None

        self._commit()

    def log_end_of_battle(self, battle_outcome: "BattleOutcome", encounter_info: "EncounterInfo"):
        if self.last_encounter is not None:
            self.last_encounter.outcome = battle_outcome
            self._update_encounter_outcome(self.last_encounter)
            if self.last_encounter.species_id in self._encounter_summaries and encounter_info.is_of_interest:
                self._encounter_summaries[self.last_encounter.species_id].update_outcome(battle_outcome)
                self._insert_or_update_encounter_summary(self._encounter_summaries[self.last_encounter.species_id])
            self._commit()

            try:
                from .csv_logger import registrar_encuentro

                pkm = encounter_info.pokemon
                local_time = encounter_info.encounter_time + timedelta(hours=-6)
                registrar_encuentro(
                    {
                        "fecha_hora": local_time.strftime("%d/%m/%Y %H:%M"),
                        "especie": pkm.species.name,
                        "género": pkm.gender if pkm.gender is not None else "", 
                        "nivel": pkm.level,
                        "naturaleza": pkm.nature.name,
                        "habilidad": pkm.ability.name,
                        "hp": pkm.ivs.hp,
                        "atk": pkm.ivs.attack,
                        "def": pkm.ivs.defence,
                        "spatk": pkm.ivs.special_attack,
                        "spdef": pkm.ivs.special_defence,
                        "spd": pkm.ivs.speed,
                        "shiny_value": pkm.shiny_value,
                        "es_shiny": pkm.is_shiny,
                        "atrapado": battle_outcome is BattleOutcome.Caught,
                    }
                )
            except Exception:
                pass

    def log_pickup_items(self, picked_up_items: list["Item"]) -> None:
        need_updating: set[int] = set()
        for item in picked_up_items:
            if item.index not in self._pickup_items:
                self._pickup_items[item.index] = PickupItem(item)
            self._pickup_items[item.index].times_picked_up += 1
            need_updating.add(item.index)
        for item_index in need_updating:
            self._insert_or_update_pickup_item(self._pickup_items[item_index])
            self._commit()

    def log_fishing_attempt(self, attempt: FishingAttempt):
        self.last_fishing_attempt = attempt
        if self.current_shiny_phase is not None:
            self.current_shiny_phase.update_fishing_attempt(attempt)
            if attempt.result is not FishingResult.Encounter:
                self._update_shiny_phase(self.current_shiny_phase)
                self._commit()
        context.message = f"Fishing attempt with {attempt.rod.name} and result {attempt.result.name}"

    def log_pokenav_call(self):
        if self.current_shiny_phase is not None:
            self.current_shiny_phase.pokenav_calls += 1
            self._update_shiny_phase(self.current_shiny_phase)
            self._commit()