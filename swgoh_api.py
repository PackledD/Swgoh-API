from utils.singleton import singleton
from loaders.guild_loader import GuildLocalLoader, GuildRemoteLoader
from loaders.player_loader import PlayerLocalLoader, PlayerRemoteLoader
from entities.unit import Unit


@singleton
class SwgohAPI(object):
    def __init__(self):
        self.__local_guild_loader = GuildLocalLoader()
        self.__remote_guild_loader = GuildRemoteLoader()
        self.__local_player_loader = PlayerLocalLoader()
        self.__remote_player_loader = PlayerRemoteLoader()

    def load_guild_from_cache(self, guild_name):
        return self.__local_guild_loader.load(guild_name)

    def load_guild_from_url(self, guild_id):
        return self.__remote_guild_loader.load(guild_id)

    def load_player_from_cache(self, player_name):
        return self.__local_player_loader.load(player_name)

    def load_player_from_url(self, ally_code):
        return self.__remote_player_loader.load(ally_code)
