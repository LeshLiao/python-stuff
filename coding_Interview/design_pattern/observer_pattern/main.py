from abc import ABC, abstractmethod


class IObservable(ABC):

    @abstractmethod
    def add_subscriber(self, observer):
        pass

    @abstractmethod
    def remove_subscriber(self, observer):
        pass

    @abstractmethod
    def update(self, message):
        pass


class PodcastA(IObservable):

    def __init__(self):
        self._subscribers = set()

    def add_subscriber(self, observer):
        self._subscribers.add(observer)
        return

    def remove_subscriber(self, observer):
        self._subscribers.remove(observer)
        return

    def update(self, message):
        for observer in self._subscribers:
            observer.update(message)


class IObserver(ABC):

    @abstractmethod
    def update(self, message):
        """"""


class Audience(IObserver):

    def update(self, message):
        print("Audience is listening: ", message)
        return


class Student(IObserver):

    def update(self, message):
        print("Student is listening: ", message)


if __name__ == "__main__":
    podcast = PodcastA()
    a = Audience()
    s = Student()

    podcast.add_subscriber(a)
    podcast.add_subscriber(s)
    podcast.update("Welcome to my podcast!")

    podcast.remove_subscriber(a)
    podcast.update("Today we are going to talk about...")
