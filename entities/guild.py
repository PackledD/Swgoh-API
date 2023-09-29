import os
import ujson as json
from entities.player import Player
from swgoh_api import SwgohAPI


class Guild(object):
    def __init__(self, data, use_cache=True):
        self.id = data["guild_id"]
        self.name = data["name"]
        self.players = self.__create_players(data["members"], use_cache)
        self.__data = data

    @staticmethod
    def __create_players(data, use_cache):
        # !!!
        if use_cache:
            return [SwgohAPI().load_player_from_cache(mem["name"]) for mem in data]
        return [SwgohAPI().load_player_from_url(mem["ally_code"]) for mem in data]

    def get_units(self, unit_name):
        lst = {}
        for player in self.players:
            unit = player.get_unit(unit_name)
            if unit:
                lst[player] = unit
        return lst

    def get_units_with_cond(self, unit_name, require):
        lst = {}
        for player in self.players:
            unit = player.get_unit_with_cond(unit_name, require)
            if unit:
                lst[player] = unit
        return lst

    def get_player_by_code(self, code):
        for player in self.players:
            if player.id == code:
                return player
        return None

    def get_code_by_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return None

    def save(self, path="."):
        path += f"/{self.name}"
        os.makedirs(f"{path}/players", exist_ok=True)
        with open(f"{path}/data.json", "w") as f:
            json.dump(self.__data, f, indent=2)
        for player in self.players:
            player.save(f"{path}/players/")

    def add_player(self, code):
        player = Player(SwgohAPI.load_player_from_url(code))
        if player:
            self.players.append(player)
        return player is not None

    def remove_player(self, code):
        player = self.get_player_by_code(code)
        res = player is not None
        if player:
            self.players.remove(player)
        return res
