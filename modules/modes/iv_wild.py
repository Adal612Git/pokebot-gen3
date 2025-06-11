from typing import Generator

from rich.prompt import IntPrompt, Prompt

from modules.console import console
from modules.player import get_player_avatar
from modules.pokemon import (
    get_species_by_name,
    StatsValues,
    _species_by_name,
    _natures_by_name,
)
from ._asserts import assert_player_has_poke_balls, assert_boxes_or_party_can_fit_pokemon
from ._interface import BotMode, BattleAction, BotModeError
from .util import apply_white_flute_if_available, spin


class IVWildMode(BotMode):
    @staticmethod
    def name() -> str:
        return "IV_WILD"

    @staticmethod
    def is_selectable() -> bool:
        return get_player_avatar().map_location.has_encounters

    def __init__(self):
        super().__init__()
        self._target_species = None
        self._min_ivs = StatsValues(0, 0, 0, 0, 0, 0)
        self._allowed_natures: set[str] | None = None

    def _ask_parameters(self) -> None:
        species_name = Prompt.ask("¿Qué especie de Pokémon deseas buscar?").strip()
        for name in _species_by_name:
            if name.lower() == species_name.lower():
                self._target_species = get_species_by_name(name)
                break
        else:
            raise BotModeError(f"Species '{species_name}' not found")

        self._min_ivs = StatsValues(
            hp=IntPrompt.ask("IV mínimo HP", default=0),
            attack=IntPrompt.ask("IV mínimo ATK", default=0),
            defence=IntPrompt.ask("IV mínimo DEF", default=0),
            special_attack=IntPrompt.ask("IV mínimo SPATK", default=0),
            special_defence=IntPrompt.ask("IV mínimo SPDEF", default=0),
            speed=IntPrompt.ask("IV mínimo SPD", default=0),
        )

        nature_str = Prompt.ask(
            "¿Qué naturaleza o naturalezas deseas?",
            default="Any",
        ).strip()
        if nature_str.lower() == "any":
            self._allowed_natures = None
        else:
            natures = {n.strip().lower() for n in nature_str.split(",") if n.strip()}
            resolved: set[str] = set()
            for nature_input in natures:
                for name in _natures_by_name:
                    if name.lower() == nature_input:
                        resolved.add(name.lower())
                        break
                else:
                    raise BotModeError(f"Naturaleza '{nature_input}' no encontrada")
            self._allowed_natures = resolved

    def on_battle_started(self, encounter) -> BattleAction | None:
        if self._target_species is None:
            self._ask_parameters()
        pokemon = encounter.pokemon
        ivs = pokemon.ivs
        console.print(
            f"Encontrado {pokemon.species.name} IVs: HP {ivs.hp}, ATK {ivs.attack}, DEF {ivs.defence}, SPATK {ivs.special_attack}, SPDEF {ivs.special_defence}, SPD {ivs.speed}"
        )
        if pokemon.species != self._target_species:
            console.print("⛔ Huir por especie.")
            return BattleAction.RunAway
        if self._allowed_natures is not None and pokemon.nature.name.lower() not in self._allowed_natures:
            console.print(f"⛔ Huir por naturaleza ({pokemon.nature.name})")
            return BattleAction.RunAway
        checks = [
            ("hp", ivs.hp, self._min_ivs.hp),
            ("attack", ivs.attack, self._min_ivs.attack),
            ("defence", ivs.defence, self._min_ivs.defence),
            ("special_attack", ivs.special_attack, self._min_ivs.special_attack),
            ("special_defence", ivs.special_defence, self._min_ivs.special_defence),
            ("speed", ivs.speed, self._min_ivs.speed),
        ]
        for stat, value, threshold in checks:
            if threshold > 0 and value < threshold:
                console.print("❌ Huir por IVs")
                return BattleAction.RunAway
        if self._allowed_natures is None:
            console.print("✅ Captura")
        else:
            console.print(f"✅ Captura (Cumple con naturaleza: {pokemon.nature.name})")
        return BattleAction.Catch

    def run(self) -> Generator:
        assert_player_has_poke_balls()
        assert_boxes_or_party_can_fit_pokemon()
        if self._target_species is None:
            self._ask_parameters()
        yield from apply_white_flute_if_available()
        while True:
            yield from spin()
