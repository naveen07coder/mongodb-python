import pymongo

new_client = pymongo.MongoClient('mongodb://localhost:27017/')

new_db = new_client["sample_database"]

new_col = new_db["Cricket"]

players = [
            {"_id": 1, "Name": "Dhoni", "Position": "Captain"},

            {"_id": 2, "Name": "Kholi", "Position": "Aggressive"},

            {"_id": 3, "Name": "Jadeja", "Position": "spotter"},

            {"_id": 4, "Name": "Sachin", "Position": "God of cricket"},

            {"_id": 5, "Name": "RL Rahul", "Position": "V Captain"}
        ]

# print("\nInserting all the documents in collection\n")
# add = new_col.insert_many(players)
# print(add)


print("\nPrinting all documents in collection\n")
find = new_col.find_one()
for i in new_col.find():
    print(i)


print("\nFinding by using query\n")
new_query = {"Position": "Captain"}
doc = new_col.find(new_query)
for i in doc:
    print(i)


print("\nFinding all similar value by using query\n")
new_query = {"Position": {"$gt": "C"}}
doc = new_col.find(new_query)
for i in doc:
    print(i)


print("\nFinding by using query by sorting\n")
doc = new_col.find().sort("Name")
for i in doc:
    print(i)


print("\nFinding by using query by sorting Descending Order\n")
doc = new_col.find().sort("Name", -1)
for i in doc:
    print(i)


print("\nDelete one doc and print others\n")
new_que = {"Name": "Sachin"}
new_col.delete_one(new_que)

for i in new_col.find():
    print(i)


print("\nDelete all\n")
new_del = {"Name": {"$regex": "^Sachin"}}
x = new_col.delete_many(new_del)
print(x.deleted_count, " Documents deleted")


# print("\nRemove all the items\n")
# n_dell = new_col.delete_many({})
# print(n_dell.deleted_count, " Removed items!")

new_col.drop()
print("\nTable Dropped\n")

print("\n\n\nNew Table Created and updating\n")

import pymongo

new_client = pymongo.MongoClient('mongodb://localhost:27017/')

new_db = new_client["sample_database"]

new_col = new_db["Cricket"]

players = [
            {"_id": 1, "Name": "Dhoni", "Position": "Captain"},

            {"_id": 2, "Name": "Kholi", "Position": "Aggressive"},

            {"_id": 3, "Name": "Jadeja", "Position": "spotter"},

            {"_id": 4, "Name": "Sachin", "Position": "God of cricket"},

            {"_id": 5, "Name": "RL Rahul", "Position": "V Captain"}
        ]

print("\nInserting all the documents in collection\n")
add = new_col.insert_many(players)

new_val = {"Name" : "Dhoni"}
new_coll = {"$set": {"Name": "Dhoni07"}} #Dhoni to Dhoni07

new_col.update_one(new_val, new_coll)

print("\nUpdating all items\n")
for i in new_col.find():
    print(i)

print("\nListing Limits of inserted list\n")
rlim = new_col.find().limit(3)
for i in rlim:
    print(i)