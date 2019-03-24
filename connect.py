from pymongo import MongoClient
# instead of localhost you have to use the name of the container
client = MongoClient('mongodb://mongo:27017/')
movie1 = {"name": "Deadpool", "length": 108, "release": {"year": 2016,
                                                         "month": 2, "day": 11}, "cast": ["Ryan Reynolds", "Karan Soni", "Ed Skrein"]}
movie2 = {"name": "Titanic", "length": 194, "release": {"year": 1998, "month": 1,
                                                        "day": 8}, "cast": ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"]}
movie3 = {"name": "Star Wars", "length": 121, "release": {"year": 1997, "month": 2,
                                                          "day": 9}, "cast": ["Mark Hamil", "Harrison Ford", "Carrie Fisher"]}

serie1 = {"name": "Breaking Bad", "release": {"year": 2008, "month": 1,
                                              "day": 20}, "cast": ["Bryan Cranston", "Aaron Paul", "Anna Gunn"]}
