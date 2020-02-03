'''
Created on 3 feb. 2020

@author: jramonga
'''
import tweepy
from abc import ABC, abstractmethod
class Bird(ABC):
    __consumer_key = "1UiJJJMJ1FrdrsXt6E49mPiSk"
    __consumer_secret = "bOXLt76589fcdBRBdTjTQEtarLID92Byva3n5L83CJ5sQub3Ry"
    __access_token = "1217805358871273472-xrQDA3hsoHlcEAFnleP2ySSALFZBJ7"
    __access_token_secret = "UiiYkTna0EJKPfglPqqWK6ofMlpYAc1VNuzl6ZbIlL65x"
    __color = "none"
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """
    def __init__(self):
        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret)
        auth.set_access_token(self.__access_token, self.__access_token_secret)
        self.api = tweepy.API(auth)
        self.color = "none"
    @abstractmethod
    def isAlive(self) -> bool:
        pass
    @abstractmethod
    def getFriends(self) -> list:
        return list()

"""
Concrete Products provide various implementations of the Product interface.
"""