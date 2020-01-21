'''
Created on 21 ene. 2020

@author: jramonga
'''

class AdminBird(object):
    __dataContainer = dict()

    def __init__(self, query):
        if(type(query) == dict.__class__):
            self.__dataContainer = query
        else:
            return -1
    
    def setDataContainer(self, query):
        if(type(query) == dict.__class__):
            self.__dataContainer = query
        else:
            return -1
    
    def getDataContainer(self):
        return self.__dataContainer
    
    def saveData(self, insertData):
        return self.__dataContainer.insert_one(insertData);
    
    def findData(self, findingQuery):
        return self.__dataContainer.find(findingQuery)
    