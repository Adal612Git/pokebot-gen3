from typing import Generator

from modules.context import context
from modules.map_data import MapRSE
from modules.player import get_player, get_player_avatar
from ._interface import BotMode, BotModeError
from .util import wait_for_n_frames

COIN_LIMIT = 9999


class MauvilleGameCornerMode(BotMode):
    @staticmethod
    def name() -> str:
        return "Mauville Game Corner"

    @staticmethod
    def is_selectable() -> bool:
        return context.rom.is_emerald

    def enter_game_corner(self) -> Generator:
        """Enter the Mauville Game Corner if standing outside."""
        if get_player_avatar().map_group_and_number == MapRSE.MAUVILLE_CITY_GAME_CORNER:
            return

        targeted_tile = get_player_avatar().map_location_in_front
        if (
            targeted_tile is None
            or targeted_tile.map_group_and_number != MapRSE.MAUVILLE_CITY_GAME_CORNER
        ):
            raise BotModeError(
                "Player is not standing in front of the Mauville Game Corner door."
            )

        context.emulator.press_button("A")
        # wait until the map transition is done
        while (
            get_player_avatar().map_group_and_number
            != MapRSE.MAUVILLE_CITY_GAME_CORNER
        ):
            yield

    def has_coin_space(self) -> bool:
        """Return True if the player can still carry more coins."""
        # TODO: read coins directly from memory once symbol available
        return get_player().coins < COIN_LIMIT

    def farm_coins(self) -> Generator:
        """Naively mash A to simulate slot machine usage."""
        start_coins = get_player().coins
        target = COIN_LIMIT
        context.message = (
            f"Starting coins: {start_coins:,}. Target: {target:,}. Farming..."
        )
        while self.has_coin_space() and context.bot_mode != "Manual":
            context.emulator.press_button("A")
            yield from wait_for_n_frames(2)
        context.message = ""

    def run(self) -> Generator:
        if not context.rom.is_emerald:
            raise BotModeError("This mode only works on Pokémon Emerald.")

        yield from self.enter_game_corner()

        if not self.has_coin_space():
            raise BotModeError("Coin case is already full.")

        yield from self.farm_coins()
