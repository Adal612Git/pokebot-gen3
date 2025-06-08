# Project Report

## Introducción
Este reporte fue generado por `analyze_project.py`. Ejecuta `python analyze_project.py` para regenerarlo.

Se generaron los siguientes archivos:
- `diagrams.puml`
- `project_report.md`
- `modification_guide.md`
- carpeta `examples/`

## Índice
- [Resumen por módulo](#resumen-por-módulo)
- [Clases Principales](#clases-principales)
- [Funciones Globales](#funciones-globales)
- [Dependencias Externas](#dependencias-externas)

## Resumen por módulo
### analyze_project.py
Clases: 3 | Funciones: 7

### pokebot.py
Clases: 1 | Funciones: 3

### requirements.py
Clases: 0 | Funciones: 3

### updater.py
Clases: 1 | Funciones: 5

### modules\battle_action_selection.py
Clases: 0 | Funciones: 4

### modules\battle_evolution_scene.py
Clases: 0 | Funciones: 1

### modules\battle_handler.py
Clases: 0 | Funciones: 3

### modules\battle_menuing.py
Clases: 0 | Funciones: 2

### modules\battle_move_replacing.py
Clases: 1 | Funciones: 3

### modules\battle_state.py
Clases: 10 | Funciones: 8

### modules\clock.py
Clases: 2 | Funciones: 2

### modules\console.py
Clases: 0 | Funciones: 8

### modules\context.py
Clases: 1 | Funciones: 0

### modules\daycare.py
Clases: 2 | Funciones: 1

### modules\debug.py
Clases: 1 | Funciones: 0

### modules\debug_utilities.py
Clases: 0 | Funciones: 10

### modules\discord.py
Clases: 2 | Funciones: 3

### modules\encounter.py
Clases: 2 | Funciones: 4

### modules\exceptions.py
Clases: 5 | Funciones: 0

### modules\exceptions_hook.py
Clases: 0 | Funciones: 2

### modules\files.py
Clases: 0 | Funciones: 6

### modules\fishing.py
Clases: 3 | Funciones: 1

### modules\game.py
Clases: 0 | Funciones: 10

### modules\game_sprites.py
Clases: 1 | Funciones: 1

### modules\game_stats.py
Clases: 1 | Funciones: 2

### modules\items.py
Clases: 12 | Funciones: 6

### modules\keyboard.py
Clases: 5 | Funciones: 4

### modules\libmgba.py
Clases: 2 | Funciones: 1

### modules\main.py
Clases: 1 | Funciones: 1

### modules\map.py
Clases: 11 | Funciones: 9

### modules\map_data.py
Clases: 5 | Funciones: 2

### modules\map_path.py
Clases: 7 | Funciones: 1

### modules\mart.py
Clases: 0 | Funciones: 3

### modules\memory.py
Clases: 1 | Funciones: 24

### modules\menuing.py
Clases: 9 | Funciones: 8

### modules\menu_parsers.py
Clases: 5 | Funciones: 13

### modules\player.py
Clases: 7 | Funciones: 6

### modules\player_pc_navigaton.py
Clases: 2 | Funciones: 2

### modules\plugins.py
Clases: 0 | Funciones: 18

### modules\plugin_interface.py
Clases: 1 | Funciones: 0

### modules\pokedex.py
Clases: 1 | Funciones: 1

### modules\pokemon.py
Clases: 18 | Funciones: 18

### modules\pokemon_party.py
Clases: 2 | Funciones: 4

### modules\pokemon_storage.py
Clases: 3 | Funciones: 1

### modules\pokemon_storage_navigaton.py
Clases: 4 | Funciones: 1

### modules\profiles.py
Clases: 1 | Funciones: 5

### modules\region_map.py
Clases: 2 | Funciones: 2

### modules\roamer.py
Clases: 1 | Funciones: 2

### modules\roms.py
Clases: 3 | Funciones: 2

### modules\runtime.py
Clases: 0 | Funciones: 5

### modules\safari_strategy.py
Clases: 8 | Funciones: 10

### modules\save_data.py
Clases: 1 | Funciones: 2

### modules\save_import.py
Clases: 1 | Funciones: 4

### modules\sprites.py
Clases: 0 | Funciones: 7

### modules\state_cache.py
Clases: 2 | Funciones: 0

### modules\stats.py
Clases: 10 | Funciones: 0

### modules\stats_migrate.py
Clases: 0 | Funciones: 1

### modules\tasks.py
Clases: 3 | Funciones: 6

### modules\tcg_card.py
Clases: 0 | Funciones: 6

### modules\text_printer.py
Clases: 2 | Funciones: 1

### modules\version.py
Clases: 0 | Funciones: 0

### modules\battle_strategies\catch.py
Clases: 1 | Funciones: 0

### modules\battle_strategies\default.py
Clases: 1 | Funciones: 0

### modules\battle_strategies\item_stealing.py
Clases: 1 | Funciones: 0

### modules\battle_strategies\level_balancing.py
Clases: 1 | Funciones: 0

### modules\battle_strategies\level_up.py
Clases: 1 | Funciones: 0

### modules\battle_strategies\lose_on_purpose.py
Clases: 1 | Funciones: 0

### modules\battle_strategies\run_away.py
Clases: 1 | Funciones: 0

### modules\battle_strategies\_interface.py
Clases: 3 | Funciones: 0

### modules\battle_strategies\_util.py
Clases: 2 | Funciones: 0

### modules\battle_strategies\__init__.py
Clases: 0 | Funciones: 0

### modules\built_in_plugins\discord_integration.py
Clases: 1 | Funciones: 5

### modules\built_in_plugins\generate_encounter_media.py
Clases: 2 | Funciones: 0

### modules\built_in_plugins\obs.py
Clases: 1 | Funciones: 0

### modules\config\schemas_v1.py
Clases: 16 | Funciones: 0

### modules\config\__init__.py
Clases: 1 | Funciones: 2

### modules\config\templates\customcatchfilters.py
Clases: 0 | Funciones: 1

### modules\data\extract.py
Clases: 0 | Funciones: 11

### modules\data\get_pret_maps.py
Clases: 0 | Funciones: 0

### modules\data\event_flags\compile_pret_flags.py
Clases: 0 | Funciones: 0

### modules\data\event_vars\compile_pret_vars.py
Clases: 0 | Funciones: 0

### modules\data\symbols\fetch_symbols.py
Clases: 0 | Funciones: 1

### modules\gui\create_profile_screen.py
Clases: 1 | Funciones: 0

### modules\gui\debug_edit_item_bag.py
Clases: 2 | Funciones: 1

### modules\gui\debug_edit_party.py
Clases: 2 | Funciones: 1

### modules\gui\debug_edit_pokedex.py
Clases: 1 | Funciones: 1

### modules\gui\debug_menu.py
Clases: 4 | Funciones: 0

### modules\gui\debug_tabs.py
Clases: 11 | Funciones: 0

### modules\gui\desktop_notification.py
Clases: 0 | Funciones: 1

### modules\gui\emulator_controls.py
Clases: 3 | Funciones: 0

### modules\gui\emulator_screen.py
Clases: 1 | Funciones: 0

### modules\gui\ev_selection_window.py
Clases: 0 | Funciones: 1

### modules\gui\headless.py
Clases: 1 | Funciones: 0

### modules\gui\load_state_window.py
Clases: 1 | Funciones: 0

### modules\gui\multi_select_window.py
Clases: 1 | Funciones: 3

### modules\gui\select_profile_screen.py
Clases: 1 | Funciones: 0

### modules\gui\__init__.py
Clases: 1 | Funciones: 0

### modules\modes\berry_blend.py
Clases: 1 | Funciones: 0

### modules\modes\bunny_hop.py
Clases: 1 | Funciones: 0

### modules\modes\daycare.py
Clases: 1 | Funciones: 0

### modules\modes\ev_train.py
Clases: 2 | Funciones: 0

### modules\modes\feebas.py
Clases: 3 | Funciones: 0

### modules\modes\fishing.py
Clases: 1 | Funciones: 0

### modules\modes\game_corner.py
Clases: 1 | Funciones: 0

### modules\modes\item_steal.py
Clases: 1 | Funciones: 0

### modules\modes\kecleon.py
Clases: 1 | Funciones: 0

### modules\modes\level_grind.py
Clases: 1 | Funciones: 0

### modules\modes\nugget_bridge.py
Clases: 1 | Funciones: 0

### modules\modes\puzzle_solver.py
Clases: 1 | Funciones: 4

### modules\modes\roamer_reset.py
Clases: 1 | Funciones: 0

### modules\modes\rock_smash.py
Clases: 1 | Funciones: 0

### modules\modes\safari.py
Clases: 1 | Funciones: 0

### modules\modes\spin.py
Clases: 1 | Funciones: 0

### modules\modes\starters.py
Clases: 1 | Funciones: 3

### modules\modes\static_gift_resets.py
Clases: 1 | Funciones: 0

### modules\modes\static_run_away.py
Clases: 1 | Funciones: 0

### modules\modes\static_soft_resets.py
Clases: 2 | Funciones: 0

### modules\modes\sudowoodo.py
Clases: 1 | Funciones: 0

### modules\modes\sweet_scent.py
Clases: 1 | Funciones: 0

### modules\modes\_asserts.py
Clases: 1 | Funciones: 10

### modules\modes\_interface.py
Clases: 5 | Funciones: 0

### modules\modes\_listeners.py
Clases: 9 | Funciones: 0

### modules\modes\__init__.py
Clases: 0 | Funciones: 4

### modules\modes\util\event_flags_and_vars.py
Clases: 0 | Funciones: 4

### modules\modes\util\higher_level_actions.py
Clases: 1 | Funciones: 14

### modules\modes\util\items.py
Clases: 1 | Funciones: 7

### modules\modes\util\map.py
Clases: 0 | Funciones: 2

### modules\modes\util\pokecenter_loop.py
Clases: 1 | Funciones: 0

### modules\modes\util\sleep.py
Clases: 0 | Funciones: 1

### modules\modes\util\soft_reset.py
Clases: 0 | Funciones: 2

### modules\modes\util\tasks_scripts.py
Clases: 0 | Funciones: 10

### modules\modes\util\walking.py
Clases: 1 | Funciones: 9

### modules\modes\util\_util_helper.py
Clases: 0 | Funciones: 1

### modules\modes\util\__init__.py
Clases: 0 | Funciones: 0

### modules\web\http.py
Clases: 0 | Funciones: 2

### modules\web\http_stream.py
Clases: 3 | Funciones: 3

### tests\test_battle_evolution.py
Clases: 1 | Funciones: 0

### tests\test_battle_move_learning.py
Clases: 1 | Funciones: 0

### tests\test_map.py
Clases: 1 | Funciones: 0

### tests\test_mode_spin.py
Clases: 1 | Funciones: 0

### tests\test_mode_starter.py
Clases: 1 | Funciones: 0

### tests\test_pathfinding.py
Clases: 1 | Funciones: 0

### tests\utility.py
Clases: 3 | Funciones: 4

### tests\__init__.py
Clases: 0 | Funciones: 0

### utility\extract_stats_encounters.py
Clases: 0 | Funciones: 1


## Clases Principales
### FunctionInfo
Firma: `class FunctionInfo(object)`
Docstring: Sin docstring

### ClassInfo
Firma: `class ClassInfo(object)`
Docstring: Sin docstring

### ModuleInfo
Firma: `class ModuleInfo(object)`
Docstring: Sin docstring

### StartupSettings
Firma: `class StartupSettings(object)`
Docstring: Sin docstring

### ReleaseInfo
Firma: `class ReleaseInfo(object)`
Docstring: Sin docstring

### LearnMoveState
Firma: `class LearnMoveState(Enum)`
Docstring: Sin docstring

### Weather
Firma: `class Weather(Enum)`
Docstring: Sin docstring

### BattleType
Firma: `class BattleType(Flag)`
Docstring: Sin docstring

### TemporaryStatus
Firma: `class TemporaryStatus(Enum)`
Docstring: Sin docstring

### StatsModifiers
Firma: `class StatsModifiers(object)`
Docstring: Sin docstring

### BattleState
Firma: `class BattleState(object)`
Docstring: Sin docstring

### BattleSideTimer
Firma: `class BattleSideTimer(object)`
Docstring: Sin docstring

### BattleStateSide
Firma: `class BattleStateSide(object)`
Docstring: Sin docstring

### BattlePokemon
Firma: `class BattlePokemon(object)`
Docstring: Sin docstring

### BattleOutcome
Firma: `class BattleOutcome(Enum)`
Docstring: Sin docstring

### EncounterType
Firma: `class EncounterType(Enum)`
Docstring: Sin docstring

### ClockTime
Firma: `class ClockTime(object)`
Docstring: Sin docstring

### PlayTime
Firma: `class PlayTime(object)`
Docstring: Sin docstring

### BotContext
Firma: `class BotContext(object)`
Docstring: Sin docstring

### DaycareCompatibility
Firma: `class DaycareCompatibility(IntEnum)`
Docstring: Sin docstring

### DaycareData
Firma: `class DaycareData(object)`
Docstring: Sin docstring

### DebugUtil
Firma: `class DebugUtil(object)`
Docstring: Sin docstring

### DiscordMessageEmbed
Firma: `class DiscordMessageEmbed(object)`
Docstring: Sin docstring

### DiscordMessage
Firma: `class DiscordMessage(object)`
Docstring: Sin docstring

### EncounterInfo
Firma: `class EncounterInfo(object)`
Docstring: Sin docstring

### EncounterValue
Firma: `class EncounterValue(Enum)`
Docstring: Sin docstring

### PrettyException
Firma: `class PrettyException(Exception)`
Docstring: Base class for all exceptions with rich print methods.

### PrettyValueError
Firma: `class PrettyValueError(PrettyException)`
Docstring: Exception to print a rich message whenever a ValueError would be raised.

### CriticalDirectoryMissing
Firma: `class CriticalDirectoryMissing(PrettyException)`
Docstring: Exception for whenever a core file is missing.

### CriticalFileMissing
Firma: `class CriticalFileMissing(PrettyException)`
Docstring: Exception for whenever a core file is missing.

### InvalidConfigData
Firma: `class InvalidConfigData(PrettyException)`
Docstring: Exception for whenever config file validation fails.

### FishingRod
Firma: `class FishingRod(Enum)`
Docstring: Sin docstring

### FishingResult
Firma: `class FishingResult(Enum)`
Docstring: Sin docstring

### FishingAttempt
Firma: `class FishingAttempt(object)`
Docstring: Sin docstring

### GameSprite
Firma: `class GameSprite(object)`
Docstring: This represents in _in-game_ Sprite object, as opposed to a

### GameStat
Firma: `class GameStat(Enum)`
Docstring: Sin docstring

### ItemType
Firma: `class ItemType(Enum)`
Docstring: Sin docstring

### ItemPocket
Firma: `class ItemPocket(Enum)`
Docstring: Sin docstring

### ItemBattleUse
Firma: `class ItemBattleUse(Enum)`
Docstring: Sin docstring

### ItemFieldUse
Firma: `class ItemFieldUse(Enum)`
Docstring: Sin docstring

### ItemHoldEffect
Firma: `class ItemHoldEffect(Enum)`
Docstring: Sin docstring

### Item
Firma: `class Item(object)`
Docstring: This represents an item type in the game.

### PokeblockColour
Firma: `class PokeblockColour(Enum)`
Docstring: Sin docstring

### PokeblockType
Firma: `class PokeblockType(Enum)`
Docstring: Sin docstring

### Pokeblock
Firma: `class Pokeblock(object)`
Docstring: Sin docstring

### ItemSlot
Firma: `class ItemSlot(object)`
Docstring: Sin docstring

### ItemBag
Firma: `class ItemBag(object)`
Docstring: Sin docstring

### ItemStorage
Firma: `class ItemStorage(object)`
Docstring: Sin docstring

### KeyboardLayout
Firma: `class KeyboardLayout(object)`
Docstring: Sin docstring

### KeyboardPage
Firma: `class KeyboardPage(object)`
Docstring: Sin docstring

### KeyboardPageType
Firma: `class KeyboardPageType(Enum)`
Docstring: Sin docstring

### NamingScreenState
Firma: `class NamingScreenState(Enum)`
Docstring: Sin docstring

### NamingScreen
Firma: `class NamingScreen(object)`
Docstring: Sin docstring

### PerformanceTracker
Firma: `class PerformanceTracker(object)`
Docstring: This is a little helper utility used for measuring the FPS rate and allowing

### LibmgbaEmulator
Firma: `class LibmgbaEmulator(object)`
Docstring: This class wraps libmgba and handles the actual emulation of a game, and exposes some of the

### ManualBotMode
Firma: `class ManualBotMode(BotMode)`
Docstring: Sin docstring

### MapConnection
Firma: `class MapConnection(object)`
Docstring: Sin docstring

### MapWarp
Firma: `class MapWarp(object)`
Docstring: Sin docstring

### MapCoordEvent
Firma: `class MapCoordEvent(object)`
Docstring: A 'coord event' is an event that gets triggered by entering a tile.

### MapBgEvent
Firma: `class MapBgEvent(object)`
Docstring: A 'BG event' is an event that triggers when interacting with a tile.

### MapLocation
Firma: `class MapLocation(object)`
Docstring: Sin docstring

### ObjectEvent
Firma: `class ObjectEvent(object)`
Docstring: Sin docstring

### ObjectEventTemplate
Firma: `class ObjectEventTemplate(object)`
Docstring: Sin docstring

### WildEncounter
Firma: `class WildEncounter(object)`
Docstring: Sin docstring

### WildEncounterList
Firma: `class WildEncounterList(object)`
Docstring: Sin docstring

### EffectiveWildEncounter
Firma: `class EffectiveWildEncounter(object)`
Docstring: Sin docstring

### EffectiveWildEncounterList
Firma: `class EffectiveWildEncounterList(object)`
Docstring: Sin docstring

### MapGroupFRLG
Firma: `class MapGroupFRLG(Enum)`
Docstring: Sin docstring

### MapFRLG
Firma: `class MapFRLG(Enum)`
Docstring: Sin docstring

### MapGroupRSE
Firma: `class MapGroupRSE(Enum)`
Docstring: Sin docstring

### MapRSE
Firma: `class MapRSE(Enum)`
Docstring: Sin docstring

### PokemonCenter
Firma: `class PokemonCenter(Enum)`
Docstring: Sin docstring

### Direction
Firma: `class Direction(IntEnum)`
Docstring: Sin docstring

### PathTile
Firma: `class PathTile(object)`
Docstring: Sin docstring

### PathMap
Firma: `class PathMap(object)`
Docstring: Sin docstring

### PathFindingError
Firma: `class PathFindingError(RuntimeError)`
Docstring: Sin docstring

### PathNode
Firma: `class PathNode(object)`
Docstring: Sin docstring

### WaypointAction
Firma: `class WaypointAction(Enum)`
Docstring: Sin docstring

### Waypoint
Firma: `class Waypoint(object)`
Docstring: Sin docstring

### GameState
Firma: `class GameState(IntEnum)`
Docstring: Sin docstring

### BaseMenuNavigator
Firma: `class BaseMenuNavigator(object)`
Docstring: Sin docstring

### StartMenuNavigator
Firma: `class StartMenuNavigator(BaseMenuNavigator)`
Docstring: Opens the start menu and moves to the option with the desired index from the menu.

### PokemonPartySubMenuNavigator
Firma: `class PokemonPartySubMenuNavigator(BaseMenuNavigator)`
Docstring: Sin docstring

### PokemonPartyMenuNavigator
Firma: `class PokemonPartyMenuNavigator(BaseMenuNavigator)`
Docstring: Sin docstring

### BattlePartyMenuNavigator
Firma: `class BattlePartyMenuNavigator(PokemonPartyMenuNavigator)`
Docstring: Sin docstring

### CheckForPickup
Firma: `class CheckForPickup(BaseMenuNavigator)`
Docstring: class that handles pickup farming.

### PartyMenuExit
Firma: `class PartyMenuExit(BaseMenuNavigator)`
Docstring: Sin docstring

### MenuWrapper
Firma: `class MenuWrapper(object)`
Docstring: Sin docstring

### RotatePokemon
Firma: `class RotatePokemon(BaseMenuNavigator)`
Docstring: Sin docstring

### CursorOptionFRLG
Firma: `class CursorOptionFRLG(IntEnum)`
Docstring: Sin docstring

### CursorOptionEmerald
Firma: `class CursorOptionEmerald(IntEnum)`
Docstring: Sin docstring

### CursorOptionRS
Firma: `class CursorOptionRS(IntEnum)`
Docstring: Sin docstring

### StartMenuOptionHoenn
Firma: `class StartMenuOptionHoenn(IntEnum)`
Docstring: Sin docstring

### StartMenuOptionKanto
Firma: `class StartMenuOptionKanto(IntEnum)`
Docstring: Sin docstring

### AvatarFlags
Firma: `class AvatarFlags(IntFlag)`
Docstring: Sin docstring

### RunningState
Firma: `class RunningState(IntEnum)`
Docstring: Sin docstring

### TileTransitionState
Firma: `class TileTransitionState(IntEnum)`
Docstring: Sin docstring

### AcroBikeState
Firma: `class AcroBikeState(IntEnum)`
Docstring: Sin docstring

### FacingDirection
Firma: `class FacingDirection(Enum)`
Docstring: Sin docstring

### PlayerAvatar
Firma: `class PlayerAvatar(object)`
Docstring: Sin docstring

### Player
Firma: `class Player(object)`
Docstring: Sin docstring

### WithdrawItemNavigator
Firma: `class WithdrawItemNavigator(BaseMenuNavigator)`
Docstring: Sin docstring

### DepositItemNavigator
Firma: `class DepositItemNavigator(BaseMenuNavigator)`
Docstring: Sin docstring

### BotPlugin
Firma: `class BotPlugin(object)`
Docstring: Sin docstring

### Pokedex
Firma: `class Pokedex(object)`
Docstring: Sin docstring

### Type
Firma: `class Type(object)`
Docstring: This represents an elemental type such as Fight, Electric, etc.

### Move
Firma: `class Move(object)`
Docstring: This represents a battle move, but not the connection to any particular Pokémon.

### LearnedMove
Firma: `class LearnedMove(object)`
Docstring: This represents a move slot for an individual Pokémon.

### StatsValues
Firma: `class StatsValues(object)`
Docstring: A collection class for all 6 stats; can be used as a convenience thing wherever a list of

### ContestConditions
Firma: `class ContestConditions(object)`
Docstring: Represents the stats that are being used in the Pokémon Contest, equivalent to `StatsValues`.

### HeldItem
Firma: `class HeldItem(object)`
Docstring: Represents a possible held item for a Pokémon encounter, along with the probability of it

### Nature
Firma: `class Nature(object)`
Docstring: Represents a Pokémon nature and its stats modifiers, along with preferred and disliked Pokéblock flavors.

### Ability
Firma: `class Ability(object)`
Docstring: Sin docstring

### LevelUpType
Firma: `class LevelUpType(Enum)`
Docstring: Sin docstring

### SpeciesLevelUpMove
Firma: `class SpeciesLevelUpMove(object)`
Docstring: Sin docstring

### SpeciesTmHmMove
Firma: `class SpeciesTmHmMove(object)`
Docstring: Sin docstring

### SpeciesMoveLearnset
Firma: `class SpeciesMoveLearnset(object)`
Docstring: Sin docstring

### Species
Firma: `class Species(object)`
Docstring: Sin docstring

### OriginalTrainer
Firma: `class OriginalTrainer(object)`
Docstring: Sin docstring

### Marking
Firma: `class Marking(Enum)`
Docstring: Sin docstring

### StatusCondition
Firma: `class StatusCondition(Enum)`
Docstring: Sin docstring

### PokerusStatus
Firma: `class PokerusStatus(object)`
Docstring: Sin docstring

### Pokemon
Firma: `class Pokemon(object)`
Docstring: Represents an individual Pokémon.

### PartyPokemon
Firma: `class PartyPokemon(Pokemon)`
Docstring: Sin docstring

### Party
Firma: `class Party(object)`
Docstring: Sin docstring

### PokemonStorageSlot
Firma: `class PokemonStorageSlot(object)`
Docstring: Sin docstring

### PokemonStorageBox
Firma: `class PokemonStorageBox(object)`
Docstring: Sin docstring

### PokemonStorage
Firma: `class PokemonStorage(object)`
Docstring: Sin docstring

### PCMainMenuNavigator
Firma: `class PCMainMenuNavigator(BaseMenuNavigator)`
Docstring: Sin docstring

### MenuNavigator
Firma: `class MenuNavigator(BaseMenuNavigator)`
Docstring: Sin docstring

### BoxNavigator
Firma: `class BoxNavigator(BaseMenuNavigator)`
Docstring: This class is for navigating the box menu.

### StorageCursor
Firma: `class StorageCursor(object)`
Docstring: Sin docstring

### Profile
Firma: `class Profile(object)`
Docstring: Profiles are config directories that contain all data for a save game, such as saves,

### FlyDestinationRSE
Firma: `class FlyDestinationRSE(Enum)`
Docstring: Sin docstring

### FlyDestinationFRLG
Firma: `class FlyDestinationFRLG(Enum)`
Docstring: Sin docstring

### Roamer
Firma: `class Roamer(object)`
Docstring: Sin docstring

### ROMLanguage
Firma: `class ROMLanguage(Enum)`
Docstring: Sin docstring

### ROM
Firma: `class ROM(object)`
Docstring: Sin docstring

### InvalidROMError
Firma: `class InvalidROMError(Exception)`
Docstring: Sin docstring

### SafariHuntingMode
Firma: `class SafariHuntingMode(Enum)`
Docstring: Sin docstring

### SafariHuntingObject
Firma: `class SafariHuntingObject(object)`
Docstring: Sin docstring

### PokeblockState
Firma: `class PokeblockState(Enum)`
Docstring: Sin docstring

### SafariCatchingLocation
Firma: `class SafariCatchingLocation(object)`
Docstring: Sin docstring

### SafariPokemon
Firma: `class SafariPokemon(Enum)`
Docstring: Enum for Pokémon locations and strategies in the Safari Zone.

### SafariPokemonRSE
Firma: `class SafariPokemonRSE(Enum)`
Docstring: Enum for Pokémon locations and strategies in the Safari Zone.

### FRLGSafariStrategy
Firma: `class FRLGSafariStrategy(object)`
Docstring: Sin docstring

### RSESafariStrategy
Firma: `class RSESafariStrategy(object)`
Docstring: Sin docstring

### SaveData
Firma: `class SaveData(object)`
Docstring: Sin docstring

### MigrationError
Firma: `class MigrationError(Exception)`
Docstring: Sin docstring

### StateCacheItem
Firma: `class StateCacheItem(Generic[T])`
Docstring: Sin docstring

### StateCache
Firma: `class StateCache(object)`
Docstring: Sin docstring

### StatsDatabaseSchemaTooNew
Firma: `class StatsDatabaseSchemaTooNew(Exception)`
Docstring: Sin docstring

### BaseData
Firma: `class BaseData(object)`
Docstring: Sin docstring

### SpeciesRecord
Firma: `class SpeciesRecord(object)`
Docstring: Sin docstring

### Encounter
Firma: `class Encounter(object)`
Docstring: Sin docstring

### ShinyPhase
Firma: `class ShinyPhase(object)`
Docstring: Sin docstring

### EncounterSummary
Firma: `class EncounterSummary(object)`
Docstring: Sin docstring

### EncounterTotals
Firma: `class EncounterTotals(object)`
Docstring: Sin docstring

### PickupItem
Firma: `class PickupItem(object)`
Docstring: Sin docstring

### GlobalStats
Firma: `class GlobalStats(object)`
Docstring: Sin docstring

### StatsDatabase
Firma: `class StatsDatabase(object)`
Docstring: Sin docstring

### Task
Firma: `class Task(object)`
Docstring: Sin docstring

### TaskList
Firma: `class TaskList(object)`
Docstring: Sin docstring

### ScriptContext
Firma: `class ScriptContext(object)`
Docstring: Sin docstring

### TextPrinterState
Firma: `class TextPrinterState(Enum)`
Docstring: Sin docstring

### TextPrinter
Firma: `class TextPrinter(object)`
Docstring: Sin docstring

### CatchStrategy
Firma: `class CatchStrategy(DefaultBattleStrategy)`
Docstring: Sin docstring

### DefaultBattleStrategy
Firma: `class DefaultBattleStrategy(BattleStrategy)`
Docstring: Sin docstring

### ItemStealingBattleStrategy
Firma: `class ItemStealingBattleStrategy(DefaultBattleStrategy)`
Docstring: Sin docstring

### LevelBalancingBattleStrategy
Firma: `class LevelBalancingBattleStrategy(DefaultBattleStrategy)`
Docstring: Sin docstring

### LevelUpLeadBattleStrategy
Firma: `class LevelUpLeadBattleStrategy(DefaultBattleStrategy)`
Docstring: Sin docstring

### LoseOnPurposeBattleStrategy
Firma: `class LoseOnPurposeBattleStrategy(BattleStrategy)`
Docstring: Sin docstring

### RunAwayStrategy
Firma: `class RunAwayStrategy(DefaultBattleStrategy)`
Docstring: Sin docstring

### BattleStrategy
Firma: `class BattleStrategy(object)`
Docstring: Sin docstring

### TurnAction
Firma: `class TurnAction(Enum)`
Docstring: Sin docstring

### SafariTurnAction
Firma: `class SafariTurnAction(Enum)`
Docstring: Sin docstring

### DamageRange
Firma: `class DamageRange(object)`
Docstring: Sin docstring

### BattleStrategyUtil
Firma: `class BattleStrategyUtil(object)`
Docstring: Sin docstring

### DiscordPlugin
Firma: `class DiscordPlugin(BotPlugin)`
Docstring: Sin docstring

### GifGeneratorListener
Firma: `class GifGeneratorListener(BotListener)`
Docstring: Sin docstring

### GenerateEncounterMediaPlugin
Firma: `class GenerateEncounterMediaPlugin(BotPlugin)`
Docstring: Sin docstring

### OBSPlugin
Firma: `class OBSPlugin(BotPlugin)`
Docstring: Sin docstring

### Battle
Firma: `class Battle(BaseConfig)`
Docstring: Schema for the catch_block configuration.

### CatchBlock
Firma: `class CatchBlock(BaseConfig)`
Docstring: Schema for the catch_block configuration.

### Cheats
Firma: `class Cheats(BaseConfig)`
Docstring: Schema for the cheat configuration.

### Discord
Firma: `class Discord(BaseConfig)`
Docstring: Schema for the discord configuration.

### DiscordWebhook
Firma: `class DiscordWebhook(BaseConfig)`
Docstring: Schema for the different webhooks sections contained in the Discord config.

### Keys
Firma: `class Keys(BaseConfig)`
Docstring: Schema for GBA key configuration.

### KeysEmulator
Firma: `class KeysEmulator(BaseConfig)`
Docstring: Schema for the emulator keys section in the Keys config.

### KeysGBA
Firma: `class KeysGBA(BaseConfig)`
Docstring: Schema for the GBA keys section in the Keys config.

### Logging
Firma: `class Logging(BaseConfig)`
Docstring: Schema for the logging configuration.

### LoggingSavePK3
Firma: `class LoggingSavePK3(BaseConfig)`
Docstring: Schema for the save_pk3 section in the Logging config.

### HTTP
Firma: `class HTTP(BaseConfig)`
Docstring: Schema for the HTTP configuration.

### OBS
Firma: `class OBS(BaseConfig)`
Docstring: Schema for the OBS configuration.

### OBSWebsocket
Firma: `class OBSWebsocket(BaseConfig)`
Docstring: Schema for the obs_websocket section in the OBS config.

### HTTPServer
Firma: `class HTTPServer(BaseConfig)`
Docstring: Schema for the http_server section in the HTTP config.

### ProfileMetadata
Firma: `class ProfileMetadata(BaseConfig)`
Docstring: Schema for the metadata configuration file part of profiles.

### ProfileMetadataROM
Firma: `class ProfileMetadataROM(BaseConfig)`
Docstring: Schema for the rom section of the metadata config.

### Config
Firma: `class Config(object)`
Docstring: Initializes a config directory and provides access to the different settings.

### CreateProfileScreen
Firma: `class CreateProfileScreen(object)`
Docstring: Sin docstring

### ItemBagEditMenu
Firma: `class ItemBagEditMenu(object)`
Docstring: Sin docstring

### ItemPocketFrame
Firma: `class ItemPocketFrame(object)`
Docstring: Sin docstring

### PartyEditMenu
Firma: `class PartyEditMenu(object)`
Docstring: Sin docstring

### PokemonEditFrame
Firma: `class PokemonEditFrame(object)`
Docstring: Sin docstring

### PokedexEditMenu
Firma: `class PokedexEditMenu(object)`
Docstring: Sin docstring

### InfiniteRepelListener
Firma: `class InfiniteRepelListener(BotListener)`
Docstring: Sin docstring

### InfiniteSafariZoneListener
Firma: `class InfiniteSafariZoneListener(BotListener)`
Docstring: Sin docstring

### ForceShinyEncounterListener
Firma: `class ForceShinyEncounterListener(BotListener)`
Docstring: Sin docstring

### DebugMenu
Firma: `class DebugMenu(Menu)`
Docstring: Sin docstring

### FancyTreeview
Firma: `class FancyTreeview(object)`
Docstring: Sin docstring

### MapViewer
Firma: `class MapViewer(object)`
Docstring: Sin docstring

### TasksTab
Firma: `class TasksTab(DebugTab)`
Docstring: Sin docstring

### BattleTab
Firma: `class BattleTab(DebugTab)`
Docstring: Sin docstring

### SymbolsTab
Firma: `class SymbolsTab(DebugTab)`
Docstring: Sin docstring

### PlayerTab
Firma: `class PlayerTab(DebugTab)`
Docstring: Sin docstring

### MiscTab
Firma: `class MiscTab(DebugTab)`
Docstring: Sin docstring

### EventFlagsTab
Firma: `class EventFlagsTab(DebugTab)`
Docstring: Sin docstring

### EventVarsTab
Firma: `class EventVarsTab(DebugTab)`
Docstring: Sin docstring

### EmulatorTab
Firma: `class EmulatorTab(DebugTab)`
Docstring: Sin docstring

### MapTab
Firma: `class MapTab(DebugTab)`
Docstring: Sin docstring

### EmulatorControls
Firma: `class EmulatorControls(object)`
Docstring: Sin docstring

### DebugTab
Firma: `class DebugTab(object)`
Docstring: Sin docstring

### DebugEmulatorControls
Firma: `class DebugEmulatorControls(EmulatorControls)`
Docstring: Sin docstring

### EmulatorScreen
Firma: `class EmulatorScreen(object)`
Docstring: Sin docstring

### PokebotHeadless
Firma: `class PokebotHeadless(object)`
Docstring: Sin docstring

### LoadStateWindow
Firma: `class LoadStateWindow(object)`
Docstring: Sin docstring

### Selection
Firma: `class Selection(object)`
Docstring: Sin docstring

### SelectProfileScreen
Firma: `class SelectProfileScreen(object)`
Docstring: Sin docstring

### PokebotGui
Firma: `class PokebotGui(object)`
Docstring: Sin docstring

### BerryBlendMode
Firma: `class BerryBlendMode(BotMode)`
Docstring: Sin docstring

### BunnyHopMode
Firma: `class BunnyHopMode(BotMode)`
Docstring: Sin docstring

### DaycareMode
Firma: `class DaycareMode(BotMode)`
Docstring: Sin docstring

### NoRotateLeadDefaultBattleStrategy
Firma: `class NoRotateLeadDefaultBattleStrategy(DefaultBattleStrategy)`
Docstring: Sin docstring

### EVTrainMode
Firma: `class EVTrainMode(BotMode)`
Docstring: Sin docstring

### FishingSpot
Firma: `class FishingSpot(object)`
Docstring: Sin docstring

### FishingSpotList
Firma: `class FishingSpotList(object)`
Docstring: Sin docstring

### FeebasMode
Firma: `class FeebasMode(BotMode)`
Docstring: Sin docstring

### FishingMode
Firma: `class FishingMode(BotMode)`
Docstring: Sin docstring

### GameCornerMode
Firma: `class GameCornerMode(BotMode)`
Docstring: Sin docstring

### ItemStealMode
Firma: `class ItemStealMode(BotMode)`
Docstring: Sin docstring

### KecleonMode
Firma: `class KecleonMode(BotMode)`
Docstring: Sin docstring

### LevelGrindMode
Firma: `class LevelGrindMode(BotMode)`
Docstring: Sin docstring

### NuggetBridgeMode
Firma: `class NuggetBridgeMode(BotMode)`
Docstring: Sin docstring

### PuzzleSolverMode
Firma: `class PuzzleSolverMode(BotMode)`
Docstring: Sin docstring

### RoamerResetMode
Firma: `class RoamerResetMode(BotMode)`
Docstring: Sin docstring

### RockSmashMode
Firma: `class RockSmashMode(BotMode)`
Docstring: Sin docstring

### SafariMode
Firma: `class SafariMode(BotMode)`
Docstring: Sin docstring

### SpinMode
Firma: `class SpinMode(BotMode)`
Docstring: Sin docstring

### StartersMode
Firma: `class StartersMode(BotMode)`
Docstring: Sin docstring

### StaticGiftResetsMode
Firma: `class StaticGiftResetsMode(BotMode)`
Docstring: Sin docstring

### StaticRunAway
Firma: `class StaticRunAway(BotMode)`
Docstring: Sin docstring

### Encounter
Firma: `class Encounter(object)`
Docstring: Sin docstring

### StaticSoftResetsMode
Firma: `class StaticSoftResetsMode(BotMode)`
Docstring: Sin docstring

### SudowoodoMode
Firma: `class SudowoodoMode(BotMode)`
Docstring: Sin docstring

### SweetScentMode
Firma: `class SweetScentMode(BotMode)`
Docstring: Sin docstring

### SavedMapLocation
Firma: `class SavedMapLocation(object)`
Docstring: Sin docstring

### BattleAction
Firma: `class BattleAction(Enum)`
Docstring: Sin docstring

### BotMode
Firma: `class BotMode(object)`
Docstring: Sin docstring

### BotModeError
Firma: `class BotModeError(Exception)`
Docstring: Sin docstring

### FrameInfo
Firma: `class FrameInfo(object)`
Docstring: Sin docstring

### BotListener
Firma: `class BotListener(object)`
Docstring: Sin docstring

### BattleListener
Firma: `class BattleListener(BotListener)`
Docstring: Sin docstring

### TrainerApproachListener
Firma: `class TrainerApproachListener(BotListener)`
Docstring: Sin docstring

### FishingListener
Firma: `class FishingListener(BotListener)`
Docstring: Sin docstring

### PokenavListener
Firma: `class PokenavListener(BotListener)`
Docstring: Sin docstring

### EggHatchListener
Firma: `class EggHatchListener(BotListener)`
Docstring: Sin docstring

### RepelListener
Firma: `class RepelListener(BotListener)`
Docstring: Sin docstring

### PoisonListener
Firma: `class PoisonListener(BotListener)`
Docstring: Sin docstring

### WhiteoutListener
Firma: `class WhiteoutListener(BotListener)`
Docstring: Sin docstring

### SafariZoneListener
Firma: `class SafariZoneListener(BotListener)`
Docstring: Sin docstring

### TaskFishing
Firma: `class TaskFishing(Enum)`
Docstring: Sin docstring

### RanOutOfRepels
Firma: `class RanOutOfRepels(BotModeError)`
Docstring: Sin docstring

### PokecenterLoopController
Firma: `class PokecenterLoopController(object)`
Docstring: Sin docstring

### TimedOutTryingToReachWaypointError
Firma: `class TimedOutTryingToReachWaypointError(BotModeError)`
Docstring: Sin docstring

### DataSubscription
Firma: `class DataSubscription(IntFlag)`
Docstring: Sin docstring

### ThreadSafeEvent
Firma: `class ThreadSafeEvent(asyncio.Event)`
Docstring: Sin docstring

### ThreadSafeCounter
Firma: `class ThreadSafeCounter(object)`
Docstring: Sin docstring

### TestBattleEvolution
Firma: `class TestBattleEvolution(BotTestCase)`
Docstring: Sin docstring

### TestBattleMoveLearning
Firma: `class TestBattleMoveLearning(BotTestCase)`
Docstring: Sin docstring

### TestEffectiveEncounterRatesForCurrentMap
Firma: `class TestEffectiveEncounterRatesForCurrentMap(unittest.TestCase)`
Docstring: Sin docstring

### TestSpin
Firma: `class TestSpin(BotTestCase)`
Docstring: Sin docstring

### TestStarter
Firma: `class TestStarter(BotTestCase)`
Docstring: Sin docstring

### TestPathfinding
Firma: `class TestPathfinding(BotTestCase)`
Docstring: Sin docstring

### MockStatsDatabase
Firma: `class MockStatsDatabase(object)`
Docstring: Sin docstring

### AutomatedTestBotMode
Firma: `class AutomatedTestBotMode(BotMode)`
Docstring: Sin docstring

### BotTestCase
Firma: `class BotTestCase(unittest.TestCase)`
Docstring: Sin docstring


## Funciones Globales
- `scan_files(base_path=Path('.'))` – Return all .py files under base_path excluding EXCLUDE_DIRS.
- `parse_module(path)` – Parse a module and extract classes, functions and imports.
- `generate_plantuml(modules)` – Generate PlantUML diagrams.
- `write_markdown_report(modules)` – Sin docstring
- `write_modification_guide(modules)` – Sin docstring
- `write_example_scripts()` – Sin docstring
- `main()` – Sin docstring
- `on_exit()` – Sin docstring
- `directory_arg(value)` – Determine if the value is a valid readable directory.
- `parse_arguments(bot_mode_names)` – Parses command-line arguments.
- `get_requirements_hash()` – This is used to check whether (a) the requirements have changed or (b) the system's Python version
- `update_requirements(ask_for_confirmation=True)` – This will run `pip install` for all requirements configured above, as well as check that
- `check_requirements()` – Checks whether the dependencies of this app are up-to-date, and if necessary runs
- `get_last_update_check_datetime()` – Sin docstring
- `get_most_recent_release_on_github()` – Sin docstring
- `fetch_release_from_github(release_info)` – Sin docstring
- `extract_update_file(release_info)` – Sin docstring
- `run_updater(ignore_last_update=False)` – Sin docstring
- `handle_battle_action_selection(strategy)` – Sin docstring
- `battle_action_use_item(battle_state, item, target_index=0)` – Sin docstring
- `battle_action_use_pokeblock(poke_block_index)` – Sin docstring
- `battle_action_use_move(action, battler_index, move_index, battle_state)` – Sin docstring
- `handle_evolution_scene(strategy)` – Sin docstring
- `handle_battle(strategy)` – This is the main battle-handling function that will attempt to finish the
- `handle_fainted_pokemon(strategy)` – Sin docstring
- `handle_nickname_caught_pokemon(encounter)` – Sin docstring
- `scroll_to_battle_action(action_index)` – Sin docstring
- `scroll_to_move(move_index, is_right_side_pokemon=False)` – Sin docstring
- `get_learn_move_state()` – Determines what step of the move_learning process we're on.
- `handle_move_replacement_dialogue(strategy)` – Sin docstring
- `get_move_learning_state_index()` – Sin docstring
- `get_battle_state()` – Sin docstring
- `battle_is_active()` – Sin docstring
- `get_main_battle_callback()` – Sin docstring
- `get_current_battle_script_instruction()` – Sin docstring
- `get_battle_controller_callback(battler_index)` – Sin docstring
- `get_last_battle_outcome()` – Sin docstring
- `get_battle_type()` – Sin docstring
- `get_encounter_type()` – Sin docstring
- `get_clock_time()` – Returns the in-game time that clock events are based on. This clock is based on
- `get_play_time()` – Returns the play time counter. This gets advanced every frame and so is tied to
- `iv_value(pokemon, iv_stat)` – Sin docstring
- `iv_colour(value)` – Sin docstring
- `iv_sum_colour(value)` – Sin docstring
- `sv_colour(value)` – Sin docstring
- `format_shiny_average(encounter_summary)` – Sin docstring
- `number(value)` – Sin docstring
- `percentage(value, total)` – Sin docstring
- `print_stats(stats, encounter)` – Sin docstring
- `get_daycare_data()` – Sin docstring
- `export_flags_and_vars(file_path)` – Exports event flags and event vars into a file, using an INI-like format.
- `import_flags_and_vars(file_path)` – Reads event flags and variables from a file and updates them.
- `debug_create_pokemon(species, level, original_pokemon=None, is_egg=False, is_shiny=False, gender=None, nickname='', held_item=None, has_second_ability=False, nature=None, experience=None, friendship=70, moves=None, ivs=None, evs=None, current_hp=None, status_condition=StatusCondition.Healthy)` – Generates a Pokémon data block given a set of criteria.
- `debug_write_party(party_pokemon)` – Replaces the current party in memory by a new list of Pokémon. If this
- `debug_write_item_bag(items, key_items, poke_balls, tms_hms, berries)` – Sin docstring
- `debug_give_test_item_pack(rse_bicycle='Acro Bike')` – Sin docstring
- `debug_get_test_party()` – Sin docstring
- `debug_give_fainted_first_slot_pokemon_with_special_ability(ability)` – Sin docstring
- `debug_give_max_coins_and_money()` – Sin docstring
- `debug_write_pokedex(seen_species, owned_species)` – Sin docstring
- `discord_send(message)` – Sin docstring
- `discord_rich_presence_loop()` – Sin docstring
- `discord_message_thread()` – Sin docstring
- `run_custom_catch_filters(pokemon)` – Sin docstring
- `judge_encounter(pokemon)` – Checks whether an encountered Pokémon matches any of the criteria that makes it
- `log_encounter(encounter_info)` – Sin docstring
- `handle_encounter(encounter_info, disable_auto_catch=False, enable_auto_battle=False, do_not_log_battle_action=False, do_not_switch_to_manual=False)` – Sin docstring
- `exception_hook(exc_type, exc_instance, traceback)` – General handler for exceptions to remove tracebacks and highlight messages if debug is off.
- `register_exception_hook()` – Sin docstring
- `read_file(file)` – Simple function to read data from a file, return False if file doesn't exist
- `write_file(file, value, mode='w')` – Simple function to write data to a file, will create the file if doesn't exist.
- `make_string_safe_for_file_name(base_string)` – :return: The string name with any characters that might be problematic in file names replaced.
- `save_pk3(pokemon)` – Takes the byte data of [obj]Pokémon.data and outputs it in a pkX format in the /profiles/[PROFILE]/pokemon dir.
- `get_rng_state_history()` – Sin docstring
- `save_rng_state_history(data)` – Sin docstring
- `get_feebas_tiles()` – Sin docstring
- `set_rom(rom)` – Sin docstring
- `get_symbol(symbol_name)` – Sin docstring
- `get_symbol_name(address, pretty_name=False)` – Get the name of a symbol based on the address
- `get_symbol_name_before(address, pretty_name=False)` – Looks up the name of the symbol that comes at or before a memory address (i.e.
- `get_event_flag_offset(flag_name)` – Sin docstring
- `get_event_flag_name(flag_number)` – Sin docstring
- `get_event_var_offset(var_name)` – Sin docstring
- `get_event_var_name(var_number)` – Sin docstring
- `decode_string(encoded_string, replace_newline=True, character_set='rom_default')` – Generation III Pokémon games use a proprietary character encoding to store text data.
- `encode_string(string, character_set='rom_default', ignore_errors=False)` – Sin docstring
- `get_game_sprite_by_id(id)` – Sin docstring
- `get_game_stat(game_stat)` – Sin docstring
- `get_total_number_of_battles()` – Sin docstring
- `get_item_by_name(name)` – Sin docstring
- `get_item_by_index(index)` – Sin docstring
- `get_item_by_move_id(move_id)` – Sin docstring
- `get_item_bag()` – Sin docstring
- `get_item_storage()` – Sin docstring
- `get_pokeblocks()` – Sin docstring
- `get_current_keyboard_layout()` – Sin docstring
- `get_naming_screen_data()` – Sin docstring
- `type_in_naming_screen(name, max_length=8)` – This will type a given string into the in-game keyboard.
- `handle_naming_screen(nickname_choice)` – Sin docstring
- `inputs_to_strings(inputs)` – :return: Converts the bitfield representing the emulator's input state to a list
- `main_loop()` – This function is run after the user has selected a profile and the emulator has been started.
- `get_map_data_for_current_position()` – Sin docstring
- `get_map_data(map_group_and_number, local_position)` – Sin docstring
- `get_map_objects()` – Sin docstring
- `get_player_map_object()` – Sin docstring
- `get_map_all_tiles(map_location=None)` – Sin docstring
- `get_wild_encounters_for_map(map_group, map_number)` – Sin docstring
- `get_encounter_affecting_abilities()` – Sin docstring
- `get_effective_encounter_rates_for_current_map()` – Sin docstring
- `calculate_targeted_coords(current_coordinates, facing_direction)` – Sin docstring
- `get_map_enum(map_group_and_number)` – Sin docstring
- `is_safari_map()` – Checks if the current map is a Safari Zone map.
- `calculate_path(source, destination, avoid_encounters=True, avoid_scripted_events=True, no_surfing=False, has_acro_bike=False, has_mach_bike=False)` – Attempts to calculate the best path from one tile to another.
- `get_mart_buyable_items()` – Sin docstring
- `get_mart_main_menu_scroll_position()` – Sin docstring
- `get_mart_buy_menu_scroll_position()` – Sin docstring
- `unpack_sint8(value)` – Sin docstring
- `unpack_uint16(value)` – Sin docstring
- `unpack_uint32(value)` – Sin docstring
- `pack_uint8(value)` – Sin docstring
- `pack_uint16(value)` – Sin docstring
- `pack_uint32(value)` – Sin docstring
- `read_symbol(name, offset=0, size=0)` – This function uses the symbol tables from the Pokémon decompilation projects found here: https://github.com/pret
- `write_symbol(name, data, offset=0)` – Sin docstring
- `get_callback_for_pointer_symbol(symbol, offset=0, pretty_name=True)` – Reads the value of a symbol (which should be a 4-byte pointer) and returns the nearest symbol that
- `get_save_block(num=1, offset=0, size=0)` – Reads and returns the entirety (or just parts of, if `offset` and/or `size` are set) of
- `write_to_save_block(data, num=1, offset=0)` – Writes data to one of the two 'save blocks'.
- `get_encryption_key()` – On Emerald and FR/LG, certain values in memory are 'encrypted' by XORing
- `decrypt16(value, encryption_key=None)` – Decrypts (or encrypts, same thing) a 16-bit value using the encryption key
- `decrypt32(value, encryption_key=None)` – Decrypts (or encrypts, same thing) a 32-bit value using the encryption key
- `get_game_state_symbol()` – Sin docstring
- `get_game_state()` – Sin docstring
- `game_has_started()` – Reports whether the game has progressed past the main menu (save loaded
- `get_event_flag(flag_name)` – Sin docstring
- `get_event_flag_by_number(flag_number)` – Sin docstring
- `set_event_flag(flag_name, new_value=None)` – Sin docstring
- `set_event_flag_by_number(flag_number)` – Sin docstring
- `get_event_var(var_name)` – Sin docstring
- `get_event_var_by_number(var_number)` – Sin docstring
- `set_event_var(var_name, new_value)` – Sin docstring
- `is_fade_active()` – Sin docstring
- `party_menu_is_open()` – helper function to determine whether the Pokémon party menu is active
- `scroll_to_item_in_bag(item)` – This will select the correct bag pocket and scroll to the correct position therein.
- `scroll_to_party_menu_index(target_index)` – Sin docstring
- `get_current_party_menu_index()` – Sin docstring
- `get_items_available_for_pickup()` – Sin docstring
- `should_check_for_pickup()` – Sin docstring
- `use_field_move(move_name)` – Sin docstring
- `get_party_menu_cursor_pos(party_length)` – Function to parse the party menu data and return usable information
- `parse_menu()` – Function to parse the currently displayed menu and return usable information.
- `parse_party_menu()` – Function to parse info about the party menu
- `get_battle_cursor(cursor_type)` – Sin docstring
- `get_learning_mon()` – If the learning state is entered through evolution, returns the Pokémon that is learning the move.
- `get_learning_move()` – helper function that returns the move trying to be learned
- `get_learning_move_cursor_pos()` – helper function that returns the position of the move learning cursor
- `parse_start_menu()` – Helper function that decodes the state of the start menu.
- `get_battle_menu()` – determines whether we're on the action selection menu, move selection menu, or neither
- `get_battle_controller()` – Sin docstring
- `name_requested()` – Determines whether the prompt to name a Pokémon is on the screen
- `switch_requested()` – Determines whether the prompt to use another Pokémon is on the screen
- `get_cursor_options(idx)` – Sin docstring
- `get_player()` – Sin docstring
- `get_player_avatar()` – Sin docstring
- `player_avatar_is_controllable()` – Sin docstring
- `player_avatar_is_standing_still()` – Sin docstring
- `get_player_location()` – Sin docstring
- `player_is_at(map, coordinates)` – Sin docstring
- `player_pc_menu_index()` – Sin docstring
- `withdraw_amount()` – Sin docstring
- `load_plugins()` – Sin docstring
- `load_built_in_plugins()` – Sin docstring
- `is_plugin_loaded(plugin_class)` – Sin docstring
- `get_plugin_instance(plugin_class)` – Sin docstring
- `plugin_get_additional_bot_modes()` – Sin docstring
- `plugin_get_additional_bot_listeners()` – Sin docstring
- `plugin_profile_loaded(profile)` – Sin docstring
- `plugin_config_reloaded()` – Sin docstring
- `plugin_battle_started(encounter)` – Sin docstring
- `plugin_wild_encounter_visible(encounter)` – Sin docstring
- `plugin_battle_ended(outcome)` – Sin docstring
- `plugin_logging_encounter(encounter)` – Sin docstring
- `plugin_pokemon_evolved(evolved_pokemon)` – Sin docstring
- `plugin_egg_starting_to_hatch(hatching_pokemon)` – Sin docstring
- `plugin_egg_hatched(hatched_pokemon)` – Sin docstring
- `plugin_whiteout()` – Sin docstring
- `plugin_judge_encounter(pokemon)` – Sin docstring
- `plugin_should_nickname_pokemon(encounter)` – Sin docstring
- `get_pokedex()` – Sin docstring
- `parse_pokemon(data)` – Sin docstring
- `get_unown_letter_by_index(letter_index)` – Sin docstring
- `get_unown_index_by_letter(letter)` – Sin docstring
- `get_type_by_name(name)` – Sin docstring
- `get_type_by_index(index)` – Sin docstring
- `get_move_by_name(name)` – Sin docstring
- `get_move_by_index(index)` – Sin docstring
- `get_nature_by_name(name)` – Sin docstring
- `get_nature_by_index(index)` – Sin docstring
- `get_ability_by_name(name)` – Sin docstring
- `get_ability_by_index(index)` – Sin docstring
- `get_species_by_name(name)` – Sin docstring
- `get_species_by_index(index)` – Sin docstring
- `get_species_by_national_dex(national_dex_number)` – Sin docstring
- `get_opponent()` – :return: The first Pokémon of the opponent's party, or None if there is no active opponent.
- `clear_opponent()` – Sin docstring
- `opponent_changed()` – Checks if the current opponent/encounter from `gEnemyParty` has changed since the function was last called.
- `pokemon_has_usable_damaging_move(pokemon)` – Checks if the given Pokémon has at least one usable attacking move.
- `get_party_size()` – Sin docstring
- `get_party()` – :return: The player's party of Pokémon.
- `get_opponent_party()` – Gets the opponent's party (obviously only makes sense to check when in a battle.)
- `get_current_repel_level()` – :return: The minimum level that wild encounters can have, given the current Repel
- `get_pokemon_storage()` – Sin docstring
- `pc_slot_from_number(slot)` – Returns the x and y for a given slot in the PC.
- `list_available_profiles()` – Sin docstring
- `load_profile_by_name(name)` – Sin docstring
- `load_profile(path)` – Sin docstring
- `profile_directory_exists(name)` – Sin docstring
- `create_profile(name, rom)` – Sin docstring
- `get_map_cursor()` – Sin docstring
- `get_map_region()` – Sin docstring
- `get_roamer()` – Sin docstring
- `get_roamer_location_history()` – Sin docstring
- `list_available_roms(force_recheck=False)` – This scans all files in the `roms/` directory and returns any entry that might
- `load_rom_data(file)` – Sin docstring
- `is_bundled_app()` – :return: Whether the bot is running in a bundled app (i.e. something built by pyinstaller.)
- `is_virtualenv()` – :return: Whether we are running in a virtualenv (True) or in the global Python environment (False)
- `get_base_path()` – :return: A `Path` object to the base directory of the bot (where `pokebot.py` or `pokebot.exe`
- `get_data_path()` – :return: A `Path` object to the `data` directory. Not that in pyinstaller distributions, this
- `get_sprites_path()` – :return: A `Path` object to the `sprites` directory. Not that in pyinstaller distributions, this
- `get_safari_zone_config(rom)` – Sin docstring
- `get_safari_strategy_action(pokemon, number_of_balls, index, has_been_baited)` – Get the safari strategy action based on the number of balls and an action index.
- `load_safari_data(file_path)` – Loads the safari strategy data from a YAML file.
- `is_watching_carefully()` – We do not intentionally check on the bait count to mimic a real user behavior
- `get_safari_balls_left()` – Sin docstring
- `get_safari_pokemon(name)` – Sin docstring
- `get_baiting_state(pokeblock)` – We do not intentionally check on the Pokémon to know what Pokéblock to throw to mimic a real user behavior
- `get_lowest_feel_any_pokeblock()` – Return the index and the Pokéblock with the lowest feel when there are no flavor preferences.
- `get_lowest_feel_excluding_type(excluded_type)` – Return the index and the Pokéblock with the lowest feel that is not of the excluded PokéblockType.
- `get_navigation_path(target_map, tile_location)` – Returns the navigation path for a given target map.
- `get_last_heal_location()` – Sin docstring
- `get_save_data()` – Extracts and normalises the save game data.
- `migrate_save_state(file, profile_name, selected_rom)` – Sin docstring
- `guess_rom_from_save_state(file, selected_rom)` – Sin docstring
- `get_state_data_from_mgba_state_file(file)` – Sin docstring
- `get_state_data_from_png(file)` – Sin docstring
- `choose_random_sprite()` – :return: Path to a random Pokémon sprite file
- `crop_sprite_square(path)` – Crops a sprite to the smallest possible size while keeping the image square.
- `generate_placeholder_image(width, height)` – Create a black placeholder image with a random sprite in the middle.
- `get_regular_sprite(pokemon_or_species)` – Sin docstring
- `get_shiny_sprite(pokemon_or_species)` – Sin docstring
- `get_anti_shiny_sprite(pokemon_or_species)` – Sin docstring
- `get_sprite(pokemon)` – Sin docstring
- `migrate_file_based_stats_to_sqlite(profile, insert_encounter, insert_shiny_phase, update_shiny_phase, insert_encounter_summary, get_encounter_summaries, query_encounters, query_shiny_phases, execute_statement, commit)` – Sin docstring
- `get_tasks()` – Sin docstring
- `get_task(task_name)` – Sin docstring
- `task_is_active(task_name)` – Sin docstring
- `get_global_script_context()` – Sin docstring
- `get_immediate_script_context()` – Sin docstring
- `is_waiting_for_input()` – :return: Whether the game is currently waiting for the A or B button to be pressed in order
- `suffix(d)` – Sin docstring
- `custom_strftime(format, t)` – Sin docstring
- `resize_image(image, factor)` – Sin docstring
- `draw_text(draw, text, coords=(0, 0), size=15, text_colour='#FFF', shadow_colour='#6B5A73', anchor='lt')` – Sin docstring
- `get_tcg_card_file_name(pokemon)` – Sin docstring
- `generate_tcg_card(pokemon_data, location='')` – Sin docstring
- `get_text_printer(index=0)` – Sin docstring
- `iv_table(pokemon)` – Sin docstring
- `pokemon_label(encounter)` – Sin docstring
- `pokemon_fields(pokemon, species_stats, short=False)` – Sin docstring
- `phase_summary_fields(pokemon, phase, global_stats)` – Sin docstring
- `send_discord_message(webhook_config, content)` – Sin docstring
- `load_config_file(file_path, config_cls, strict=False)` – Helper to load files from a path without manually creating the sources.
- `save_config_file(config_dir, config_inst, strict=False)` – Helper to save config data from a model into a config directory.
- `custom_catch_filters(pokemon)` – See readme for documentation: https://github.com/40Cakes/pokebot-gen3/tree/main/wiki/pages/Configuration%20-%20Custom%20Catch%20Filters.md
- `find_roms()` – Ensures that we have a valid Emerald ROM for every possible language.
- `initialise_localised_string()` – Sets up the default dict structure for translatable strings.
- `get_address(symbol_name)` – The GBA maps the ROM to memory location 0x0800_0000, so the symbol table
- `read_string(file, offset=-1)` – Reads a string of unknown length from a file, all the way up to the next
- `get_tm_hm_move_map(data_source)` – Sin docstring
- `extract_items(english_rom, localised_roms)` – Sin docstring
- `extract_abilities(english_rom, localised_roms)` – Sin docstring
- `extract_types(english_rom, localised_roms)` – Sin docstring
- `extract_natures(english_rom, localised_roms)` – Sin docstring
- `extract_moves(english_rom, localised_roms, types_list)` – Sin docstring
- `extract_species(english_rom, localised_roms, other_editions_roms, type_list, ability_list, item_list)` – Sin docstring
- `download_file(url)` – Sin docstring
- `run_edit_item_bag_screen()` – Sin docstring
- `run_edit_party_screen()` – Sin docstring
- `run_edit_pokedex_screen()` – Sin docstring
- `desktop_notification(title, message, icon=None)` – Sin docstring
- `ask_for_ev_targets(pokemon)` – Sin docstring
- `ask_for_choice(choices, window_title='Choose...')` – Sin docstring
- `ask_for_confirmation(message, window_title='Confirmation')` – Displays a confirmation window with the given message and Yes/No buttons.
- `ask_for_choice_scroll(choices, window_title='Choose...', options_per_row=3, button_width=165, button_height=165, visible_rows=2)` – Sin docstring
- `mount_bike()` – Sin docstring
- `unmount_bike()` – Sin docstring
- `use_rock_smash(facing_direction)` – Sin docstring
- `use_strength(direction_to_push)` – Sin docstring
- `run_frlg()` – Sin docstring
- `run_rse_hoenn()` – Sin docstring
- `run_rse_johto()` – Sin docstring
- `assert_save_game_exists(error_message)` – Raises an exception if there is no saved game.
- `assert_saved_on_map(expected_locations, error_message)` – Raises an exception if the game has not been saved on the given map.
- `assert_registered_item(expected_items, error_message, check_in_saved_game=False)` – Raises an exception if the given item is not registered (for the Select button.)
- `assert_has_pokemon_with_any_move(moves, error_message, check_in_saved_game=False, with_pp_remaining=False)` – Raises an exception if the player has no Pokémon that knows any of the given move in their
- `assert_item_exists_in_bag(expected_items, error_message, check_in_saved_game=False)` – Raises an exception if the player does not have the given item in their bag.
- `assert_empty_slot_in_party(error_message, check_in_saved_game=False)` – Raises an exception if the player has a full party.
- `assert_boxes_or_party_can_fit_pokemon(error_message=None, check_in_saved_game=False)` – Raises an exception if all boxes are full and there is no empty slot in the player's party,
- `assert_player_has_poke_balls(check_in_saved_game=False)` – Raises an exception if the player doesn't have any Pokeballs when starting a catching mode
- `assert_party_has_damaging_move(error_message, check_in_saved_game=False)` – Ensures the party has at least one Pokémon with a usable attacking move.
- `assert_pokemon_in_party_slot(species_name, slot, error_message, check_in_saved_game=False)` – Raises an exception if the pokemon specified is not in the party slot required
- `get_bot_modes()` – Sin docstring
- `get_bot_mode_names()` – Sin docstring
- `get_bot_mode_by_name(name)` – Sin docstring
- `get_bot_listeners(rom)` – Sin docstring
- `wait_until_event_flag_is_true(flag_name, button_to_press=None)` – This will wait until an event flag in is set to true.
- `wait_until_event_flag_is_false(flag_name, button_to_press=None)` – This will wait until an event flag in is set to false.
- `wait_until_event_var_equals(var_name, expected_value, button_to_press=None)` – Wait until an event var has a particular value.
- `wait_until_event_var_not_equals(var_name, avoid_value, button_to_press=None)` – Wait until an event var does NOT have a particular value.
- `fly_to(destination)` – Sin docstring
- `fish(stop_condition=None, loop=False)` – Handles both single fishing actions or continuous fishing loop.
- `spin(stop_condition=None, counter_clockwise=False)` – Sin docstring
- `heal_in_pokemon_center(pokemon_center_door_location)` – Sin docstring
- `change_lead_party_pokemon(slot)` – Sin docstring
- `save_the_game()` – Uses the in-game save function.
- `leave_safari_zone()` – Sin docstring
- `buy_in_shop(shopping_list)` – This can be used to walk through the Mart's buying menu and purchase one or
- `sell_in_shop(items_to_sell)` – This can be used to walk through the Mart's selling menu and sell one or more
- `talk_to_npc(local_object_id)` – Sin docstring
- `mount_bicycle()` – Sin docstring
- `unmount_bicycle()` – Sin docstring
- `dive()` – Sin docstring
- `surface_from_dive()` – Sin docstring
- `scroll_to_item_in_bag(item)` – This will select the correct bag pocket and scroll to the correct position therein.
- `use_item_from_bag(item, wait_for_start_menu_to_reappear=True)` – Sin docstring
- `register_key_item(item)` – Ensures that a Key Item is registered to the Select button.
- `apply_white_flute_if_available()` – Sin docstring
- `apply_repel()` – Tries to use the strongest Repel available in the player's item bag (i.e. it will
- `repel_is_active()` – Checks if a Repel is currently active.
- `teach_hm_or_tm(hm_or_tm, party_index, move_index_to_replace=3)` – Attempts to teach an HM or TM move to a party Pokémon.
- `find_closest_pokemon_center(location=None)` – Sin docstring
- `map_has_pokemon_center_nearby(map_enum)` – Sin docstring
- `wait_for_n_frames(number_of_frames)` – This will wait for a certain number of frames to pass.
- `soft_reset(mash_random_keys=True)` – Soft-resets the emulation. This only works if there is a save game, otherwise it will
- `wait_for_unique_rng_value()` – Wait until the RNG value is unique. This is faster if the `random_soft_reset_rng`
- `wait_until_task_is_active(function_name, button_to_press=None)` – This will wait until an in-game task starts, optionally mashing a particular button
- `wait_until_task_is_not_active(function_name, button_to_press=None)` – This will wait until an in-game task finishes (i.e. is no longer part of the task list, or
- `wait_for_task_to_start_and_finish(function_name, button_to_press=None)` – This will wait until an in-game task starts (if it is not yet running) and finishes (i.e.
- `wait_for_yes_no_question(answer_to_give)` – Waits for a Yes/No question to pop up and answers it.
- `wait_for_multiple_choice_question(choice_index)` – Sin docstring
- `wait_until_script_is_active(function_name, button_to_press=None)` – Sin docstring
- `wait_until_script_is_no_longer_active(function_name, button_to_press=None)` – Sin docstring
- `wait_for_script_to_start_and_finish(function_name, button_to_press=None)` – Sin docstring
- `wait_for_no_script_to_run(button_to_press=None)` – Sin docstring
- `wait_for_fade_to_finish()` – Sin docstring
- `walk_to(destination_coordinates, run=True)` – Moves the player to a set of coordinates on the same map. Does absolutely no
- `follow_path(waypoints, run=True)` – Moves the player along a given path.
- `follow_waypoints(path, run=True)` – Follows a given set of waypoints.
- `navigate_to(map, coordinates, run=True, avoid_encounters=True, avoid_scripted_events=True, expecting_script=False)` – Tries to walk the player to a given location while circumventing obstacles.
- `walk_one_tile(direction, run=True)` – Moves the player one tile in a given direction, and then waiting for the movement
- `ensure_facing_direction(facing_direction)` – If the player avatar is not already facing a certain direction this will make it turn
- `run_in_circle(on_map, bottom_left, top_right, clockwise=True, exit_condition=None)` – Function name is lying: This actually makes the character run in a _square_
- `wait_for_player_avatar_to_be_controllable(button_to_press=None)` – Sin docstring
- `wait_for_player_avatar_to_be_standing_still(button_to_press=None)` – Sin docstring
- `isolate_inputs(generator_function)` – Sin docstring
- `http_server(host, port)` – Run Flask server to make bot data available via HTTP requests.
- `start_http_server(host, port)` – Sin docstring
- `add_subscriber(subscribed_topics)` – Sin docstring
- `run_watcher()` – Sin docstring
- `send_message(subscription_flag, data, event_type=None)` – Sin docstring
- `with_save_state(state_file_names)` – Sin docstring
- `with_frame_timeout(timeout_in_frames)` – Sin docstring
- `set_next_rng_seed(rng_seed)` – Sin docstring
- `set_next_choice(next_choice)` – Sin docstring
- `fail(error_message, exit_code=1, extra_content=None)` – Sin docstring

## Dependencias Externas
- PIL
- __future__
- _asserts
- _interface
- _util
- _util_helper
- aiohttp
- apispec
- argparse
- ast
- asyncio
- atexit
- base64
- battle_handler
- battle_state
- battle_strategies
- binascii
- clock
- collections
- confz
- console
- context
- contextlib
- csv
- darkdetect
- dataclasses
- datetime
- default
- discord_webhook
- encounter
- enum
- event_flags_and_vars
- fishing
- functools
- game
- gui
- hashlib
- higher_level_actions
- importlib
- inspect
- io
- items
- itertools
- json
- keyboard
- map
- map_data
- map_path
- mart
- math
- memory
- menuing
- mgba
- notifypy
- numpy
- obsws_python
- os
- pathlib
- platform
- plugins
- plyer
- pokemon
- pokemon_storage
- pydantic
- pypresence
- queue
- random
- re
- requests
- rich
- ruamel
- runtime
- showinfm
- shutil
- sleep
- soft_reset
- sounddevice
- sprites
- sqlite3
- string
- struct
- sys
- tasks_scripts
- tests
- text_printer
- textwrap
- threading
- time
- tkinter
- ttkthemes
- types
- typing
- unittest
- urllib
- util
- walking
- webbrowser
- yaml
- zipfile
- zlib
- zoneinfo