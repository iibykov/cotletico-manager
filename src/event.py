from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def event_action(self) -> str:
        pass

    @abstractmethod
    def message(self) -> str:
        pass


class ChanceState(State):

    def event_action(self) -> str:
        return 'ОПАСНЫЙ МОМЕНТ    +1 опасный момент в статистику'

    def message(self) -> str:
        return 'опасный момент'


class GoalState(State):

    def event_action(self) -> str:
        return 'ГОООООЛ  + 1 гол в статистику'

    def message(self) -> str:
        return 'ГОООООЛ'


class RejectGoalState(State):

    def event_action(self) -> str:
        return 'VAR  - 1 гол из статистики'

    def message(self) -> str:
        return 'ГОООООЛ'


class CornerState(State):

    def event_action(self) -> str:
        return 'Угловой  + 1 угловой в статистику команды'

    def message(self) -> str:
        return 'Угловой'


class FoulState(State):

    def event_action(self) -> str:
        return 'ФОЛ  + 1 фол в статистику команды'

    def message(self) -> str:
        return 'ФОЛ'


class YellowState(State):

    def event_action(self) -> str:
        return 'ЖЕЛТАЯ КАРТОЧА  + 1 ЖК в статистику команды'

    def message(self) -> str:
        return 'ЖК'


class Event:
    def __init__(self, state: State, type=None, time=0, chances=0, goals=0):
        self._state = state
        self.type = type
        self.time = time
        self.chances = chances
        self.goals = goals

    def change_state(self, state: State) -> None:
        self._state = state

    def event_action(self) -> None:
        self._execute('event_action')

    def message(self) -> None:
        self._execute('message')

    def _execute(self, operation: str) -> None:
        try:
            func = getattr(self._state, operation)
            print(func())
        except AttributeError:
            print('Не корректная команда')

