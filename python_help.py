movie = {"name": "Deadpool", "length": 108, "release": {"year": 2016,
                                                        "month": 2, "day": 11}, "cast": ["Ryan Reynolds", "Karan Soni", "Ed Skrein"]}"
# how to access data from a dict

movie["name"]
# returns Deadpool

movie["release"]
# returns {"year": 2016,"month": 2, "day": 11}

movie["cast"][0]
# returns Ryan Reynolds


###################################
# some basic commands for pymongo #
###################################
client = MongoClient('mongodb://mongo:27017/')
db = client.media  # media is the acutal name of the db
collection = db.movies  # movies is the actual name of the collection
collection.insert_one("ANY JSON")  # inserts the json into the collection
collection.find_one("ANY JSON")  # returns the last object
# returns a generator object with alle objects. Use a for loop to iterate
collection.find("ANY JSON")

for object in collection.find():
    print(object)
