import tweepy
import sys

import BirdBreeder, NestMaker, ClientBird
from BirdBreeder import BlueBreeder
from ClientBird import CreateBird
'''
Object behaivour definition
'''
import Birds

if __name__ == '__main__' :
    blueBird = CreateBird(Birds.BlueBird())
    home = blueBird.isAlive()
    print("Is alive: ", home)
    print(blueBird.setUser("Maluma"))
    '''
    print("isAlive" + blueBird.isAlive())
    '''
    blackBird = CreateBird(Birds.BlackBird())
    blackBird.getFriends("Maluma")
        