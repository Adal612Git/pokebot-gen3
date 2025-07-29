from enum import Enum, auto
from typing import Generator, Iterable

from modules.context import context
from modules.memory import get_event_flag, read_symbol, unpack_uint32
from modules.map_data import MapFRLG, PokemonCenter
from modules.pokedex import get_pokedex
from modules.map import (
    get_effective_encounter_rates_for_current_map,
    get_map_data_for_current_position,
)
from modules.modes._interface import BotMode, BotModeError
from modules.modes.util.pokecenter_loop import PokecenterLoopController
from modules.modes.util import navigate_to
from modules.pokemon_party import get_party
from modules.battle_state import BattleOutcome
from modules.battle_strategies.level_up import LevelUpLeadBattleStrategy

# Difference in levels between the party and local encounters after which the
# bot should advance to the next area.
OVERLEVELED_LEVEL_DIFF = 10


class AdventureObjective(Enum):
    GYM1 = auto()
    GYM2 = auto()
    GYM3 = auto()
    GYM4 = auto()
    GYM5 = auto()
    GYM6 = auto()
    GYM7 = auto()
    GYM8 = auto()
    DONE = auto()


BADGE_FLAGS = [
    "BADGE01_GET",
    "BADGE02_GET",
    "BADGE03_GET",
    "BADGE04_GET",
    "BADGE05_GET",
    "BADGE06_GET",
    "BADGE07_GET",
    "BADGE08_GET",
]

GYM_CENTERS = [
    PokemonCenter.PewterCity,
    PokemonCenter.CeruleanCity,
    PokemonCenter.VermilionCity,
    PokemonCenter.CeladonCity,
    PokemonCenter.FuchsiaCity,
    PokemonCenter.SaffronCity,
    PokemonCenter.CinnabarIsland,
    PokemonCenter.ViridianCity,
]

GYM_MAPS = [
    MapFRLG.PEWTER_CITY_GYM,
    MapFRLG.CERULEAN_CITY_GYM,
    MapFRLG.VERMILION_CITY_GYM,
    MapFRLG.CELADON_CITY_GYM,
    MapFRLG.FUCHSIA_CITY_GYM,
    MapFRLG.SAFFRON_CITY_GYM,
    MapFRLG.CINNABAR_ISLAND_GYM,
    MapFRLG.VIRIDIAN_CITY_GYM,
]

GYM_COORDS = [
    (4, 7),
    (4, 7),
    (4, 7),
    (4, 7),
    (4, 7),
    (4, 7),
    (4, 7),
    (4, 7),
]


class SmartAdventureMode(BotMode):
    @staticmethod
    def name() -> str:
        return "Smart Adventure"

    def __init__(self):
        super().__init__()
        self._controller = PokecenterLoopController(focus_on_lead_pokemon=True)
        self._battle_strategy = LevelUpLeadBattleStrategy

    def on_battle_started(self, encounter):
        return self._battle_strategy()

    def on_battle_ended(self, outcome: BattleOutcome) -> None:
        self._controller.on_battle_ended()

    def on_whiteout(self) -> bool:
        return self._controller.on_whiteout()

    def _area_max_level(self) -> int:
        encounters = get_effective_encounter_rates_for_current_map()
        if encounters is None:
            return 0
        max_level = 0
        for e in (
            encounters.land_encounters
            + encounters.surf_encounters
            + encounters.rock_smash_encounters
            + encounters.old_rod_encounters
            + encounters.good_rod_encounters
            + encounters.super_rod_encounters
        ):
            max_level = max(max_level, e.max_level)
        return max_level

    def _missing_species_in_area(self) -> Iterable[str]:
        pokedex = get_pokedex()
        encounters = get_effective_encounter_rates_for_current_map()
        if encounters is None:
            return []
        missing = []
        for e in (
            encounters.land_encounters
            + encounters.surf_encounters
            + encounters.rock_smash_encounters
            + encounters.old_rod_encounters
            + encounters.good_rod_encounters
            + encounters.super_rod_encounters
        ):
            if e.species not in pokedex.owned_species:
                missing.append(e.species.name)
        return missing

    def run(self) -> Generator:
        try:
            if unpack_uint32(read_symbol("gMapHeader", size=4)) == 0:
                raise BotModeError(
                    "Game not ready. Load a save state and make sure the player is in-game before starting Smart Adventure."
                )
            self._controller.verify_on_start()
        except Exception as error:
            if isinstance(error, BotModeError):
                raise
            raise BotModeError(
                "Failed to initialise Smart Adventure. Make sure a save is loaded and the player is on the map."
            ) from error

        while True:
            yield from self._controller.run()

            objective = self._get_next_objective()
            if objective is AdventureObjective.DONE:
                context.set_manual_mode()
                return

            current_area = get_map_data_for_current_position()
            missing_here = list(self._missing_species_in_area())
            if missing_here:
                context.message = (
                    "Veo Pokémon nuevos en esta zona: "
                    + ", ".join(missing_here)
                    + ". Intentando capturarlos..."
                )
                print(context.message)
                yield from self._controller.run(
                    lambda: len(self._missing_species_in_area()) == 0
                )
                continue

            area_max_level = self._area_max_level()
            party_levels = [p.level for p in get_party() if not p.is_egg]
            if party_levels and all(
                l > area_max_level + OVERLEVELED_LEVEL_DIFF for l in party_levels
            ):
                context.message = f"Equipo sobreleveleado (lvl {max(party_levels)}) para zona '{current_area.map_name}'"
                print(context.message)
                index = objective.value - 1
                center = GYM_CENTERS[index]
                context.message += ". Avanzando a la siguiente zona..."
                yield from navigate_to(*center.value)
                continue

            gym_index = objective.value - 1
            if max(party_levels) >= area_max_level:
                context.message = f"Listo para el próximo gimnasio {objective.name}. Dirigiéndose allá."
                print(context.message)
                center = GYM_CENTERS[gym_index]
                gym_map = GYM_MAPS[gym_index]
                gym_coords = GYM_COORDS[gym_index]
                yield from navigate_to(*center.value)
                yield from self._controller.run()
                yield from navigate_to(gym_map, gym_coords)
                while not get_event_flag(BADGE_FLAGS[gym_index]):
                    yield
                continue
            else:
                context.message = "Necesito entrenar más antes del gimnasio."
                print(context.message)
                yield from self._controller.run()

    def _get_next_objective(self) -> AdventureObjective:
        for idx, flag in enumerate(BADGE_FLAGS):
            if not get_event_flag(flag):
                return AdventureObjective(idx + 1)
        return AdventureObjective.DONE
