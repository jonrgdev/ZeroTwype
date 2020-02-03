import tweepy
'''
Created on 21 ene. 2020

@author: jramonga
'''
from NestMaker import NestMaker
from Birds import *
from abc import ABC, abstractmethod
     
class BlueBreeder(NestMaker):
    def breed_blueBird(self) -> BlueBird:
        self.color = "blue"
        return BlueBird(self)
    
class BlackBleeder(NestMaker):
        
    def breed_blackBird(self) -> BlackBird:
        self.color="black"
        return BlackBird(self)