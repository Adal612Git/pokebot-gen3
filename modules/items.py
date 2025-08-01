import json
from dataclasses import dataclass
from enum import Enum
from functools import cached_property

from modules.context import context
from modules.memory import get_save_block, unpack_uint16, decrypt16
from modules.runtime import get_data_path
from modules.state_cache import state_cache


class ItemType(Enum):
    Mail = ("mail",)
    UsableOutsideBattle = "usable_outside_battle"
    UsableInCertainLocations = "usable_in_certain_locations"
    PokeblockCase = "pokeblock_case"
    NotUsableOutsideBattle = "not_usable_outside_battle"

    def __str__(self):
        return self.value

    @classmethod
    def from_value(cls, value: str) -> "ItemType":
        for name, member in ItemType.__members__.items():
            if member.value == value:
                return member


class ItemPocket(Enum):
    Items = "items"
    PokeBalls = "poke_balls"
    TmsAndHms = "tms_and_hms"
    Berries = "berries"
    KeyItems = "key_items"

    @property
    def rse_index(self) -> int:
        return {self.Items: 0, self.PokeBalls: 1, self.TmsAndHms: 2, self.Berries: 3, self.KeyItems: 4}[self]

    @property
    def frlg_index(self) -> int:
        return {self.Items: 0, self.KeyItems: 1, self.PokeBalls: 2}[self]

    @property
    def index(self) -> int:
        return self.rse_index if context.rom.is_rse else self.frlg_index

    @property
    def capacity(self) -> int:
        sizes = {
            ItemPocket.Items: {"rs": 20, "e": 30, "frlg": 42},
            ItemPocket.KeyItems: {"rs": 20, "e": 30, "frlg": 30},
            ItemPocket.PokeBalls: {"rs": 16, "e": 16, "frlg": 13},
            ItemPocket.TmsAndHms: {"rs": 64, "e": 64, "frlg": 58},
            ItemPocket.Berries: {"rs": 46, "e": 46, "frlg": 43},
        }

        if context.rom.is_rs:
            return sizes[self]["rs"]
        elif context.rom.is_emerald:
            return sizes[self]["e"]
        else:
            return sizes[self]["frlg"]

    def __str__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)


class ItemBattleUse(Enum):
    NotUsable = "not_usable"
    Catch = "catch"
    StatIncrease = "stat_increase"
    Healing = "healing"
    PpRecovery = "pp_recovery"
    Escape = "escape"
    EnigmaBerry = "enigma_berry"

    def __str__(self):
        return self.value

    @classmethod
    def from_value(cls, value: str) -> "ItemBattleUse":
        for name, member in ItemBattleUse.__members__.items():
            if member.value == value:
                return member
        return ItemBattleUse.NotUsable


class ItemFieldUse(Enum):
    NotUsable = "not_usable"
    Healing = "healing"
    PpRecovery = "pp_recovery"
    EnigmaBerry = "enigma_berry"

    def __str__(self):
        return self.value

    @classmethod
    def from_value(cls, value: str) -> "ItemFieldUse":
        for name, member in ItemFieldUse.__members__.items():
            if member.value == value:
                return member
        return ItemFieldUse.NotUsable


class ItemHoldEffect(Enum):
    NoEffect = "no_effect"
    RestoreHP = "restore_hp"
    CureParalysis = "cure_paralysis"
    CureSleep = "cure_sleep"
    CurePoison = "cure_poison"
    CureBurn = "cure_burn"
    CureFreeze = "cure_freeze"
    RestorePP = "restore_pp"
    CureConfusion = "cure_confusion"
    CureStatusCondition = "cure_status_condition"
    ConfuseSpicy = "confuse_spicy"
    ConfuseDry = "confuse_dry"
    ConfuseSweet = "confuse_sweet"
    ConfuseBitter = "confuse_bitter"
    ConfuseSour = "confuse_sour"
    AttackUp = "attack_up"
    DefenseUp = "defense_up"
    SpeedUp = "speed_up"
    SpecialAttackUp = "special_attack_up"
    SpecialDefenseUp = "special_defense_up"
    CriticalHitRateUp = "critical_hit_rate_up"
    RandomStatUp = "random_stat_up"
    EvasionUp = "evasion_up"
    RestoreStats = "restore_stats"
    MachoBrace = "macho_brace"
    ExpShare = "exp_share"
    QuickClaw = "quick_claw"
    FriendshipUp = "friendship_up"
    CureAttract = "cure_attract"
    ChoiceBand = "choice_band"
    Flinch = "flinch"
    BugPower = "bug_power"
    DoublePrize = "double_prize"
    Repel = "repel"
    SoulDew = "soul_dew"
    DeepSeaTooth = "deep_sea_tooth"
    DeepSeaScale = "deep_sea_scale"
    CanAlwaysRunAway = "can_always_run_away"
    PreventEvolve = "prevent_evolve"
    FocusBand = "focus_band"
    LuckyEgg = "lucky_egg"
    ScopeLens = "scope_lens"
    SteelPower = "steel_power"
    Leftovers = "leftovers"
    DragonScale = "dragon_scale"
    LightBall = "light_ball"
    GroundPower = "ground_power"
    RockPower = "rock_power"
    GrassPower = "grass_power"
    DarkPower = "dark_power"
    FightingPower = "fighting_power"
    ElectricPower = "electric_power"
    WaterPower = "water_power"
    FlyingPower = "flying_power"
    PoisonPower = "poison_power"
    IcePower = "ice_power"
    GhostPower = "ghost_power"
    PsychicPower = "psychic_power"
    FirePower = "fire_power"
    DragonPower = "dragon_power"
    NormalPower = "normal_power"
    UpGrade = "up_grade"
    ShellBell = "shell_bell"
    LuckyPunch = "lucky_punch"
    MetalPowder = "metal_powder"
    ThickClub = "thick_club"
    Stick = "stick"

    def __str__(self):
        return self.value

    @classmethod
    def from_value(cls, value: str) -> "ItemHoldEffect":
        for name, member in ItemHoldEffect.__members__.items():
            if member.value == value:
                return member
        return ItemHoldEffect.NoEffect


@dataclass
class Item:
    """
    This represents an item type in the game.
    """

    index: int
    name: str
    sprite_name: str
    price: int
    type: ItemType
    battle_use: ItemBattleUse
    field_use: ItemFieldUse
    pocket: ItemPocket
    hold_effect: ItemHoldEffect
    parameter: int
    extra_parameter: int
    tm_hm_move_id: int | None

    def tm_hm_move(self) -> "Move | None":
        from modules.pokemon import get_move_by_index

        return get_move_by_index(self.tm_hm_move_id) if self.tm_hm_move_id is not None else None

    @classmethod
    def from_dict(cls, index: int, data: dict) -> "Item":
        if data["pocket"] == "poke_balls":
            item_type = data["type"]
        else:
            item_type = ItemType.from_value(data["type"])

        return Item(
            index=index,
            name=data["name"],
            sprite_name=data["name"].replace("'", "").replace(".", ""),
            price=data["price"],
            type=item_type,
            battle_use=ItemBattleUse.from_value(data["battle_use"]),
            field_use=ItemFieldUse.from_value(data["field_use"]),
            pocket=ItemPocket(data["pocket"]),
            hold_effect=ItemHoldEffect.from_value(data["hold_effect"]),
            parameter=data["parameter"],
            extra_parameter=data["extra_parameter"],
            tm_hm_move_id=data["tm_hm_move_id"],
        )


class PokeblockColour(Enum):
    NoColour = 0
    Red = 1
    Blue = 2
    Pink = 3
    Green = 4
    Yellow = 5
    Purple = 6
    Indigo = 7
    Brown = 8
    LiteBlue = 9
    Olive = 10
    Gray = 11
    Black = 12
    White = 13
    Gold = 14


class PokeblockType(Enum):
    Spicy = "spicy"
    Dry = "dry"
    Sweet = "sweet"
    Bitter = "bitter"
    Sour = "sour"


@dataclass
class Pokeblock:
    colour: PokeblockColour
    spicy: int
    dry: int
    sweet: int
    bitter: int
    sour: int
    feel: int

    @property
    def level(self):
        return max(self.spicy, self.dry, self.sweet, self.bitter, self.sour)

    @property
    def type(self):
        flavors = {
            PokeblockType.Spicy: self.spicy,
            PokeblockType.Dry: self.dry,
            PokeblockType.Sweet: self.sweet,
            PokeblockType.Bitter: self.bitter,
            PokeblockType.Sour: self.sour,
        }
        return max(flavors, key=flavors.get)


@dataclass
class ItemSlot:
    item: Item
    quantity: int

    def to_dict(self) -> dict:
        return {
            "item": self.item.name,
            "quantity": self.quantity,
        }


class ItemBag:
    def __init__(
        self,
        data: bytes,
        items_count: int,
        key_items_count: int,
        poke_balls_count: int,
        tms_hms_count: int,
        berries_count: int,
        encryption_key: int | None = None,
    ):
        self._data = data
        self._encryption_key = encryption_key
        self.items_size = items_count
        self.key_items_size = key_items_count
        self.poke_balls_size = poke_balls_count
        self.tms_hms_size = tms_hms_count
        self.berries_size = berries_count

    def __eq__(self, other):
        if isinstance(other, ItemBag):
            return other._data == self._data
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, ItemBag):
            return other._data != self._data
        else:
            return NotImplemented

    def _get_pocket(self, slot_offset: int, number_of_slots: int) -> list[ItemSlot]:
        result = []
        for index in range(number_of_slots):
            offset = (slot_offset + index) * 4
            item_index = unpack_uint16(self._data[offset : offset + 2])
            quantity = decrypt16(unpack_uint16(self._data[offset + 2 : offset + 4]), self._encryption_key)
            if item_index != 0 and quantity > 0:
                item = get_item_by_index(item_index)
                result.append(ItemSlot(item, quantity))
        return result

    @cached_property
    def items(self) -> list[ItemSlot]:
        return self._get_pocket(slot_offset=0, number_of_slots=self.items_size)

    @cached_property
    def key_items(self) -> list[ItemSlot]:
        offset = self.items_size
        return self._get_pocket(slot_offset=offset, number_of_slots=self.key_items_size)

    @cached_property
    def poke_balls(self) -> list[ItemSlot]:
        offset = self.items_size + self.key_items_size
        return self._get_pocket(slot_offset=offset, number_of_slots=self.poke_balls_size)

    @cached_property
    def tms_hms(self) -> list[ItemSlot]:
        offset = self.items_size + self.key_items_size + self.poke_balls_size
        return self._get_pocket(slot_offset=offset, number_of_slots=self.tms_hms_size)

    @cached_property
    def berries(self) -> list[ItemSlot]:
        offset = self.items_size + self.key_items_size + self.poke_balls_size + self.tms_hms_size
        return self._get_pocket(slot_offset=offset, number_of_slots=self.berries_size)

    def has_space_for(self, item: Item) -> bool:
        match item.pocket:
            case ItemPocket.Items:
                pocket = self.items
                pocket_size = self.items_size
            case ItemPocket.KeyItems:
                pocket = self.key_items
                pocket_size = self.key_items_size
            case ItemPocket.PokeBalls:
                pocket = self.poke_balls
                pocket_size = self.poke_balls_size
            case ItemPocket.TmsAndHms:
                pocket = self.tms_hms
                pocket_size = self.tms_hms_size
            case ItemPocket.Berries:
                pocket = self.berries
                pocket_size = self.berries_size
            case _:
                pocket = []
                pocket_size = 0

        if len(pocket) < pocket_size:
            return True

        # In FireRed/LeafGreen, you can always put 999 items in a stack. In RSE, this only works for berries.
        if context.rom.is_frlg or item.pocket == ItemPocket.Berries:
            stack_size = 999
        else:
            stack_size = 99

        return any(slot.item == item and slot.quantity < stack_size for slot in pocket)

    def pocket_for(self, item: Item) -> list[ItemSlot]:
        match item.pocket:
            case ItemPocket.Items:
                return self.items
            case ItemPocket.KeyItems:
                return self.key_items
            case ItemPocket.PokeBalls:
                return self.poke_balls
            case ItemPocket.TmsAndHms:
                return self.tms_hms
            case ItemPocket.Berries:
                return self.berries
            case _:
                raise RuntimeError(f"Invalid bag pocket: {str(item.pocket)}")

    def quantity_of(self, item: Item) -> int:
        return sum(slot.quantity for slot in self.pocket_for(item) if slot.item == item)

    def first_slot_index_for(self, item: Item) -> int | None:
        pocket = self.pocket_for(item)
        return next(
            (slot_index for slot_index in range(len(pocket)) if pocket[slot_index].item == item),
            None,
        )

    @property
    def number_of_repels(self) -> int:
        return sum(slot.quantity for slot in self.items if slot.item.name in ("Repel", "Super Repel", "Max Repel"))

    @property
    def number_of_balls_except_master_ball(self) -> int:
        return sum(slot.quantity for slot in self.poke_balls if slot.item.index != 1)

    @property
    def number_of_balls(self) -> int:
        """Returns the total number of Poké Balls, including Master Balls."""
        return sum(slot.quantity for slot in self.poke_balls)

    def to_dict(self) -> dict:
        return {
            "items": [s.to_dict() for s in self.items],
            "key_items": [s.to_dict() for s in self.key_items],
            "poke_balls": [s.to_dict() for s in self.poke_balls],
            "tms_hms": [s.to_dict() for s in self.tms_hms],
            "berries": [s.to_dict() for s in self.berries],
        }


class ItemStorage:
    def __init__(self, data: bytes, number_of_slots: int):
        self._data = data
        self.number_of_slots = number_of_slots

    def __eq__(self, other):
        if isinstance(other, ItemStorage):
            return other._data == self._data
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, ItemStorage):
            return other._data != self._data
        else:
            return NotImplemented

    @cached_property
    def items(self) -> list[ItemSlot]:
        result = []
        for index in range(self.number_of_slots):
            offset = index * 4
            item_index = unpack_uint16(self._data[offset : offset + 2])
            quantity = unpack_uint16(self._data[offset + 2 : offset + 4])
            if item_index != 0 and quantity > 0:
                item = get_item_by_index(item_index)
                result.append(ItemSlot(item, quantity))
        return result

    def has_space_for(self, item: Item) -> bool:
        if len(self.items) < self.number_of_slots:
            return True

        return any(slot.item == item and slot.quantity < 999 for slot in self.items)

    def first_slot_index_for(self, item: Item) -> int | None:
        for index, slot in enumerate(self.items):
            if slot.item.index == item.index:
                return index
        return None

    def quantity_of(self, item: Item) -> int:
        return sum(slot.quantity for slot in self.items if slot.item == item)

    def to_list(self) -> list[dict]:
        return [s.to_dict() for s in self.items]


def _load_items() -> tuple[dict[str, Item], list[Item], dict[int, Item]]:
    by_name: dict[str, Item] = {}
    by_index: list[Item] = []
    by_move_id: dict[int, Item] = {}
    with open(get_data_path() / "items.json", "r") as file:
        items_data = json.load(file)
        for index in range(len(items_data)):
            item = Item.from_dict(index, items_data[index])
            by_name[item.name] = item
            by_index.append(item)
            if item.tm_hm_move_id:
                by_move_id[item.tm_hm_move_id] = item
    return by_name, by_index, by_move_id


_items_by_name, _items_by_index, _items_by_move_id = _load_items()


def get_item_by_name(name: str) -> Item:
    return _items_by_name[name]


def get_item_by_index(index: int) -> Item:
    return _items_by_index[index]


def get_item_by_move_id(move_id: int) -> Item | None:
    return _items_by_move_id.get(move_id, None)


def get_item_bag() -> ItemBag:
    if state_cache.item_bag.age_in_frames == 0:
        return state_cache.item_bag.value

    offset = 0x310 if context.rom.is_frlg else 0x560
    items_count = ItemPocket.Items.capacity
    key_items_count = ItemPocket.KeyItems.capacity
    poke_balls_count = ItemPocket.PokeBalls.capacity
    tms_hms_count = ItemPocket.TmsAndHms.capacity
    berries_count = ItemPocket.Berries.capacity

    data_size = 4 * (items_count + key_items_count + poke_balls_count + tms_hms_count + berries_count)
    data = get_save_block(1, offset=offset, size=data_size)

    item_bag = ItemBag(data, items_count, key_items_count, poke_balls_count, tms_hms_count, berries_count)
    state_cache.item_bag = item_bag
    return item_bag


def get_item_storage() -> ItemStorage:
    if state_cache.item_storage.age_in_frames == 0:
        return state_cache.item_storage.value

    if context.rom.is_frlg:
        items_count = 30
        offset = 0x298
    else:
        items_count = 50
        offset = 0x498

    data = get_save_block(1, offset=offset, size=items_count * 4)
    item_storage = ItemStorage(data, items_count)
    state_cache.item_storage = item_storage
    return item_storage


def get_pokeblocks() -> list[Pokeblock]:
    if context.rom.is_rs:
        offset = 0x7F8
    elif context.rom.is_emerald:
        offset = 0x848
    else:
        return []

    data = get_save_block(1, offset=offset, size=40 * 8)
    result = []
    for index in range(40):
        block_data = data[index * 8 : index * 8 + 7]
        if block_data[0] > 0:
            result.append(Pokeblock(PokeblockColour(block_data[0]), *block_data[1:]))

    return result
