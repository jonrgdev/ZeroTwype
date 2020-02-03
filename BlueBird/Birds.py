'''
Created on 3 feb. 2020

@author: jramonga
'''
from Bird import Bird
import tweepy
from tweepy import binder

class BlueBird(Bird):
    user = object
    
    def isAlive(self) -> bool:
        return True
    
    def getFriends(self) -> list:
        return list()
    
    def getHome(self) -> binder.bind_api:
        return self.api.home_timeline()
    
    def getType(self) -> str:
        return self.color
    
    def setUser(self, user):
        self.user = self.api.get_user(user)
    
class BlackBird(Bird):

    def isAlive(self) -> bool:
        return False
    def getFriends(self, userName) -> list:
        user = self.api.get_user(userName)
        print(user.screen_name)
        print(user.followers_count)
        friends = user.friends()
        for friend in friends:
            print(friend.screen_name)
        
    