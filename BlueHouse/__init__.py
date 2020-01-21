import pymongo


client = pymongo.MongoClient("mongodb+srv://jonrg:eureka1@cluster0-zwqau.gcp.mongodb.net/test?retryWrites=true&w=majority")

if __name__ == '__main__':
    
    mydb = client["sample_airbnb"]
    dbTable = mydb["listingsAndReviews"]
    
    query = {"listing_url:":"https://www.airbnb.com/rooms/10009999"}
    resultQuery = dbTable.find_one()
    for elem in resultQuery:
        print(elem)
    
    newTuple = mydb["newCol"]
    tmpData = {"name":"james", "last_name":"bond"}
    ret = newTuple.insert_one(tmpData);
    
    print(ret.inserted_id)
    print("FIN")
    
    client.close()
