import pymongo

# connection to db
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
print(client.list_database_names())

# create db called outerspace
outerspace = client['outerspace']

# create collection in db
planets = outerspace.planets

# create one record in collection
planets.insert_one({'name': 'Earth', 'color': 'blue'})
print(client.list_database_names())

# create many records in collection
planets.insert_many([{'name': 'Mars', 'color': 'red'},
                    {'name': 'Saturn', 'color': 'yellow'},
                    {'name': 'Pluto', 'color': 'brown'}])

# find one document
# print(planets.find_one({'color':'blue'}))
# find more than one document
for document in planets.find():
    print(document)
print()
# update one document
planets.update_one({'name': 'Earth'},{"$set": {"color":"purple", "moons": "1"}})
# update more than one document
# filter, update = {'name': 'Mars'}, {"$set": {"moons":"2"}}
# planets.update_many(filter, update)

for document in planets.find():
    if "name" in document:
        filter = {"name":document["name"]}
        update = {"$set": {"moons":""}}
        planets.update_one(filter, update)

for document in planets.find():
    print(document)
print()
planets.delete_one({"name":"Pluto"})
for document in planets.find():
    print(document)
outerspace.drop_collection(planets)
client.drop_database(outerspace)
