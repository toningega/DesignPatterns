from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the Subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the Subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class WeatherStation(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)
        print(observer.background_story)


    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """
        list_of_weather_options = ['rain','sunshine','snow','dry','foggy','icy','hurricane']

        print("\nSubject: finding out what the weather will be")
        self._state = list_of_weather_options[randint(0,len(list_of_weather_options)-1)]

        print(f"Subject: the weather is changing: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by Subjects.
    """
    background_story = ' '

    @abstractmethod
    def update(self, Subject: Subject) -> None:
        """
        Receive update from Subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class Tonin(Observer):
    background_story = ' Do I need a umbrella?'

    def update(self, Subject: Subject) -> None:
        if Subject._state == 'rain':
            print("Tonin: Wow, I think I better bring an umbrella")
        if Subject._state == 'sunshine':
            print("Tonin: Where did I leave my glasses")
        if Subject._state == 'hurricane':
            print("Tonin: Fuck")


class ConcreteObserverB(Observer):
    background_story = '''Im driving so I want to know if it's dangerous'''
    def update(self, Subject: Subject) -> None:
        if Subject._state == 'icy' or Subject._state == 'snow':
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    Subject = WeatherStation()

    observer_a = Tonin()
    Subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    Subject.attach(observer_b)

    Subject.some_business_logic()
    Subject.some_business_logic()

    Subject.detach(observer_a)

    Subject.some_business_logic()