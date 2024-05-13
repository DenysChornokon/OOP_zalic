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

    def use_charm(self):
        self.charm.become_immortal(self)


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


monsters = []
monsters.append(RunningMonster("Монстер_1", "бігає", QuickRegenCharm()))
monsters.append(FlyingMonster("Монстер_2", "літає", StrongStrikeCharm()))
monsters.append(FlyingRunningMonster("Монстер_3", "бігає та літає", ImmortalityCharm()))
monsters.append(FlyingMonster("Монстер_4", "літає", StrongStrikeCharm()))
monsters.append(RunningMonster("Монстер_5", "бігає", QuickRegenCharm()))


for monster in monsters:
    monster.move()
    monster.use_charm()
