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


class RunningMonster(Monster):
    def move(self):
        print(f"{self.name} біжить.")

    def use_charm(self):
        self.charm.use_quick_regen(self)


class FlyingMonster(Monster):
    def move(self):
        print(f"{self.name} літає.")

    def use_charm(self):
        self.charm.use_strong_strike(self)


class FlyingRunningMonster(RunningMonster, FlyingMonster):
    def move(self):
        print(f"{self.name} може бігати та літати.")


class Charm(ABC):
    @abstractmethod
    def use_quick_regen(self, monster):
        pass

    @abstractmethod
    def use_strong_strike(self, monster):
        pass

    @abstractmethod
    def become_immortal(self, monster):
        pass


class QuickRegenCharm(Charm):
    def use_quick_regen(self, monster):
        print(f"{monster.name} використовує швидке відновлення сили.")

    def become_immortal(self, monster):
        pass

    def use_strong_strike(self, monster):
        pass


class StrongStrikeCharm(Charm):
    def use_quick_regen(self, monster):
        pass

    def use_strong_strike(self, monster):
        print(f"{monster.name} використовує посилений удар.")

    def become_immortal(self, monster):
        pass


class ImmortalityCharm(Charm):
    def use_quick_regen(self, monster):
        pass

    def use_strong_strike(self, monster):
        pass

    def become_immortal(self, monster):
        print(f"{monster.name} стає безсмертним.")


