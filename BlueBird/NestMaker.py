'''
Created on 3 feb. 2020

@author: jramonga
'''
import tweepy, Bird
from abc import ABC, abstractmethod

class NestMaker(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """
    @abstractmethod
    def __init__(self):
       pass
    @abstractmethod
    def breed_blueBird(self) -> Bird:
        super()
        pass
    @abstractmethod
    def breed_blackBird(self) -> Bird:
        super()
        pass
    def any_method(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """
        # Call the factory method to create a Product object.
        bird = self.breedBird()
        return bird
    @abstractmethod
    def getHome(self):
        pass
"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""
