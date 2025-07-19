information={
    "a": 89,
    "v":88,
    "p":27
}
print("a-",information["a"])
print("v-",information["v"])
print("p-",information["p"])
print(information.items())#show the item / list
print(information.keys())#show only keys
print(information.values())#show only values
information.update({"a":98})#update and add new keys 
print(information)
print(information.get("a2"))#find the key or if no key than print none