from enum import Enum, auto
from typing import Generator

from modules.context import context
from modules.memory import get_event_flag
from modules.map_data import MapFRLG, PokemonCenter
from modules.modes._interface import BotMode
from modules.modes.util.pokecenter_loop import PokecenterLoopController
from modules.modes.util import navigate_to
from modules.battle_state import BattleOutcome
from modules.battle_strategies.level_up import LevelUpLeadBattleStrategy


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


class AutoAdventureMode(BotMode):
    @staticmethod
    def name() -> str:
        return "Auto Adventure"

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

    def run(self) -> Generator:
        self._controller.verify_on_start()
        while True:
            # Heal if necessary
            yield from self._controller.run()

            objective = self._get_next_objective()
            if objective is AdventureObjective.DONE:
                context.set_manual_mode()
                return

            index = objective.value - 1
            center = GYM_CENTERS[index]
            gym_map = GYM_MAPS[index]
            gym_coords = GYM_COORDS[index]

            # Travel to the city's Pokémon Center first
            yield from navigate_to(*center.value)
            yield from self._controller.run()

            # Navigate to the gym entrance
            yield from navigate_to(gym_map, gym_coords)
            # Wait until badge is obtained (handled by battle strategy)
            while not get_event_flag(BADGE_FLAGS[index]):
                yield

    def _get_next_objective(self) -> AdventureObjective:
        for idx, flag in enumerate(BADGE_FLAGS):
            if not get_event_flag(flag):
                return AdventureObjective(idx + 1)
        return AdventureObjective.DONE
