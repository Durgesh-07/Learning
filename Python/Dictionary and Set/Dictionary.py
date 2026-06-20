dist = {
    "key" : "value", # only value can be updated not Key
    "name" : "apnacollege",
    "subjects" : ["python","C","Java"],
    86 : 10.12,
    "age" : 19,
    "is_adult" : True,
    12.99 : 94
}
print(dist)
dist["is_adult"] = False
dist[86] = "Movie"
print(dist)
dist["Surname"] = "Chouhan"
print(dist)
info = {}
print(info)
info["name"] = "Durgesh"
info["surname"] = "Chouhan"
print(info)