from enum import Enum, auto
from typing import Generator

from modules.context import context
from modules.memory import (
    get_event_flag,
    read_symbol,
    unpack_uint32,
)
from modules.map_data import MapFRLG, PokemonCenter
from modules.modes._interface import BotMode, BotModeError
from modules.modes.util.pokecenter_loop import PokecenterLoopController
from modules.modes.util import navigate_to
from modules.modes.util.higher_level_actions import buy_in_shop, talk_to_npc
from modules.items import get_item_bag, get_item_by_name
from modules.pokedex import get_pokedex
from modules.pokemon_party import get_party
from modules.map import (
    get_effective_encounter_rates_for_current_map,
    get_map_data_for_current_position,
)
from modules.battle_state import BattleOutcome
from modules.battle_strategies.level_up import LevelUpLeadBattleStrategy
from modules.battle_strategies.level_balancing import LevelBalancingBattleStrategy
from modules.battle_strategies.catch import CatchStrategy


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

# Placeholder coordinates for each gym entrance
GYM_COORDS = [
    (4, 7),  # Pewter Gym
    (4, 7),  # Cerulean Gym
    (4, 7),  # Vermilion Gym
    (4, 7),  # Celadon Gym
    (4, 7),  # Fuchsia Gym
    (4, 7),  # Saffron Gym
    (4, 7),  # Cinnabar Gym
    (4, 7),  # Viridian Gym
]

# Placeholder mart maps and coordinates for restocking Poké Balls
MART_MAPS = [
    MapFRLG.PEWTER_CITY_MART,
    MapFRLG.CERULEAN_CITY_MART,
    MapFRLG.VERMILION_CITY_MART,
    MapFRLG.CELADON_CITY_DEPARTMENT_STORE_2F,
    MapFRLG.FUCHSIA_CITY_MART,
    MapFRLG.SAFFRON_CITY_MART,
    MapFRLG.CINNABAR_ISLAND_MART,
    MapFRLG.VIRIDIAN_CITY_MART,
]

MART_COORDS = [
    (4, 7),
    (4, 7),
    (4, 7),
    (4, 7),
    (4, 7),
    (4, 7),
    (4, 7),
    (4, 7),
]


class AutoAdventureMode(BotMode):
    @staticmethod
    def name() -> str:
        return "Auto Adventure"

    def __init__(self):
        super().__init__()
        self._controller = PokecenterLoopController(focus_on_lead_pokemon=True)
        # Use a strategy that keeps the whole party leveled
        self._battle_strategy = LevelBalancingBattleStrategy

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

    def _missing_species_in_area(self) -> list[str]:
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

    def _count_pokeballs(self) -> int:
        return sum(slot.quantity for slot in get_item_bag().poke_balls)

    def _restock_pokeballs(self, index: int) -> Generator:
        mart_map = MART_MAPS[index]
        mart_coords = MART_COORDS[index]
        # Move to the mart and talk to the shopkeeper
        yield from navigate_to(mart_map, mart_coords, run=True, avoid_encounters=False)
        yield from talk_to_npc(1)
        yield from buy_in_shop([(get_item_by_name("Poké Ball"), 10)])

    def on_battle_started(self, encounter):
        if (
            encounter is not None
            and encounter.pokemon.species not in get_pokedex().owned_species
            and self._count_pokeballs() > 0
        ):
            print("Pensando...")
            return CatchStrategy()
        return self._battle_strategy()

    def on_battle_ended(self, outcome: BattleOutcome) -> None:
        self._controller.on_battle_ended()

    def on_whiteout(self) -> bool:
        return self._controller.on_whiteout()

    def run(self) -> Generator:
        try:
            # If the player is still on the title screen, gMapHeader will be 0
            if unpack_uint32(read_symbol("gMapHeader", size=4)) == 0:
                raise BotModeError(
                    "Game not ready. Load a save state and make sure the player is in-game before starting Auto Adventure."
                )
            self._controller.verify_on_start()
        except Exception as error:
            if isinstance(error, BotModeError):
                raise
            raise BotModeError(
                "Failed to initialise Auto Adventure. Make sure a save is loaded and the player is on the map."
            ) from error
        while True:
            print("Pensando...")
            # Heal if necessary
            yield from self._controller.run()

            if self._count_pokeballs() == 0:
                yield from self._restock_pokeballs(self._get_next_objective().value - 1)
                continue

            objective = self._get_next_objective()
            context.message = f"Objetivo actual: {objective.name}"
            print(context.message)
            if objective is AdventureObjective.DONE:
                context.set_manual_mode()
                return

            index = objective.value - 1
            center = GYM_CENTERS[index]
            gym_map = GYM_MAPS[index]
            gym_coords = GYM_COORDS[index]

            missing_here = self._missing_species_in_area()
            if missing_here:
                context.message = (
                    "Veo Pokémon nuevos en esta zona: " + ", ".join(missing_here) + ". Intentando capturarlos..."
                )
                print(context.message)
                yield from self._controller.run(lambda: len(self._missing_species_in_area()) == 0)
                continue

            party_levels = [p.level for p in get_party() if not p.is_egg]
            area_max = self._area_max_level()
            if party_levels:
                avg_level = sum(party_levels) / len(party_levels)
                overleveled = avg_level > area_max + 5 or all(l > area_max + 5 for l in party_levels)
                if overleveled:
                    context.message = (
                        f"Equipo sobreleveleado (promedio lvl {avg_level:.1f}) para zona, avanzando al siguiente centro"
                    )
                    print(context.message)
                    yield from navigate_to(*center.value, run=True, avoid_encounters=False)
                    continue

            # Travel to the city's Pokémon Center first
            yield from navigate_to(*center.value, run=True, avoid_encounters=False)
            yield from self._controller.run()

            # Navigate to the gym entrance
            yield from navigate_to(gym_map, gym_coords, run=True, avoid_encounters=False)
            # Wait until badge is obtained (handled by battle strategy)
            while not get_event_flag(BADGE_FLAGS[index]):
                yield

    def _get_next_objective(self) -> AdventureObjective:
        for idx, flag in enumerate(BADGE_FLAGS):
            if not get_event_flag(flag):
                return AdventureObjective(idx + 1)
        return AdventureObjective.DONE