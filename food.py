import pymongo
# Install dnspython package through the terminal in Gitpod:                      | pip install dnspython
# Install pymongo package through the terminal in Gitpod:                        | pip install pymongo
# Check for the version of MongoDB (as well as whether it is in your workspace): | mongod --version

### CREATE

# Connected to a client
client = pymongo.MongoClient("mongodb+srv://gracesong146:Rhododendron25@pobaeto-9y9dv.mongodb.net/test?retryWrites=true&w=majority")

# Connecting/Creating a database
consumables = client.get_database('consumables')

# Connecting/creating a collection in a database
fruits = consumables.get_collection('fruits')

# Insert one document into a collection
fruits.insert_one({"Item":"Banana", "Price": 300, "weight": 300, "length": 10, "Colour" : "Yellow"})
manystuff = [{
  "Item" : "Apple",
  "Weight" : 50,
  "Price" : 0.30,
  "Radius" : "5cm" #Dynamic schema! :o
  }, {
  "Item" : "Grapes",
  "Weight" : 100,
  "Price" : 10.00 ,
  "Colour" : "Green",
  "Bundle_Quantity" : 42

  }]
fruits.insert_many(manystuff)


### READ

## xxx.list_xxx_names() Would return the list of databases/collections in an array. Listing all documents in a collection
# List down all databases in a client
databases = client.list_database_names()
print(databases)

'''List down all collections in a database'''
collections = consumables.list_collection_names()
print(collections)

'''List down all documents in a collection'''
documents = fruits.find()
# print('Listing documents in the fruits collection...')
# for stuff in documents:
#     print(stuff)

'''Listing specific documents in a collection'''
# What if you want to just view fruits that are yellow colour?
# We use specific queries in the .find() method like so:
Yellow_fruits = fruits.find({"Colour" : "Yellow"})
print('Listing documents in the fruits collection that are Yellow...')
for fruits in Yellow_fruits:
  print(fruits)

'''Tables for conditionals/queries'''
# table for conditionals/queries that you can utilise to get exactly what data you want to find. :)

# | Conditional	| Purpose
# -----------------------------------------
# | $eq	        | Equals to
# | $gt	        | Greater than
# | $gte	    | Greater than or equal to
# | $lt	        | Less than
# | $lte	    | Less than or equal to
# | $ne	        | Not equal
# | $in	        | In a specific list
# | $nin	    | Not in a specific list
# | $or	        | Logical OR
# | $and	    | Logical AND
# | $exists	    | Matches documents which has the named field

### UPDATE

# Updating one document
print("Updating...")
fruits.update_one({"Item" : "Banana"} , {"$set" : {"Item" : "Awesome_Banana"}})

# Updating many documents
print("Updating many...")
fruits.update_many({"Price" : {"$lte" : 3.00}} , {"$set" : {"Price" : 4.00}})

for stuff in documents:
    print(stuff)

### DELETE

# Deleting one document
print("Deleting...")
fruits.delete_one({"Item" : "Banana"})

# Deleting many documents
print("Deleting many...")
fruits.delete_many({"Item" : "Banana"})

for stuff in documents:
    print(stuff)
