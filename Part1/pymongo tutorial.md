# Fundamental C.R.U.D functions of persistent storage

C - Create

R - Read

U - Update

D - Delete

Before we go through the CRUD details, we shall connect to a client/cluster first
```
import pymongo

client = pymongo.MongoClient(<MongoDB server here>)
```
For this ~~cheatsheet~~ example, our database will be consumables, collection be food, and documents be banana.
### Create

In MongoDB, creating a database/collection has the same function as routing to it.

 **Creating/Connecting to a database within a client**
```
Consumables_database = client.get_database('Consumables') 
```
In the above code snippet, `Consumable_database` is merely a variable placeholder in the pymongo command line... You can call it whatever you want as long as it's easy to understand. For me I follow the convention <databasename>_database so that it's easier to understand.
  
  As for `client.get_database('Consumables')`, Consumables is the name of the database you want to create/connect to.
  
   **Creating/Connecting to a collection within a database**
  ```
  Fruits_collection = Consumables_database.get_collection('Fruits')
  ```
  The naming convention follows similarly for the earlier snippet, nothing much to explain here.
  Remember I am only creating one collection for this example, you can create as many collections as you want within a database. So lets   say you wanna make a drinks collection just do `Drinks_collection = Consumables_database.get_collection('Drinks')`
  
   **Adding documents into a collection**
  To insert documents into a collection, we use the following function:
  ```
  Fruits_collection.insert_one({"Item" : "Banana", "Weight" : 300, "Price" : 3, "Colour" : "Yellow", "Length" : 10})
  ```
  If you want to insert multiple documents instead you can just use `.insert_many(data1, data2, data3, etc)`.                             You realise that documents come in the form of dictionaries. If you don't already know yet, dictionaries are like arrays but instead of having a single element in each index of the array, dictionaries have a key-value pair representing an element in the dictionary.
  
  Inserting just one document into the collection seems readible enough. But when you want to insert multiple documents at once, it may become too hard to read and therefore we can use the alternative:
  Assign multiple documents into an array, separated by commas. Then just `insert_many(array)`
  
  For example:
  **Creating an array to be inserted all at once into the fruits collection**
  ```
  manystuff = [{
    "Item" : "Banana",
    "Weight" : 300,
    "Price" : 3,
    "Colour" : "Yellow",
    "Length" : "10cm" #Dynamic schema! :o
    }, {
    "Item" : "Apple",
    "Weight" : 50,
    "Price" : 0.30,
    "Radius" : "5cm" #Dynamic schema! :o
    }, {
    "Item" : "Grapes",
    "Weight" : 100,
    "Price" : 10 ,
    "Colour" : "Green",
    "Bundle_Quantity" : 42

    }]
```
**Inserting all those documents into the fruits collection**
```
fruits_collection.insert_many(manystuf)
```

weww this is tiring
  
  
  
  
