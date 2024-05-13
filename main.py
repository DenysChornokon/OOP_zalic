from abc import ABC, abstractmethod


class Monster(ABC):
    def __init__(self, name, movement_type, charm):
        self.name = name
        self.movement_type = movement_type
        self.charm = charm

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def use_charm(self):
        pass


