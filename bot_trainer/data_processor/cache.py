from typing import Text
from rasa.core.agent import Agent
from cachetools.lru import LRUCache


class AgentCache:
    def set(self, bot: Text, agent: Agent):
        pass

    def get(self, bot: Text) -> Agent:
        pass

    def is_exists(self) -> Agent:
        pass


class InMemoryAgentCache(AgentCache):
    cache = LRUCache(maxsize=100)

    @staticmethod
    def set(bot: Text, agent: Agent):
        InMemoryAgentCache.cache.__setitem__(bot, agent)

    @staticmethod
    def get(bot: Text) -> Agent:
        return InMemoryAgentCache.cache.get(bot)

    @staticmethod
    def is_exists(bot: Text) -> Agent:
        return bot in InMemoryAgentCache.cache.keys()
