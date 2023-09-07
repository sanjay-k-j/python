#methods
myDict = {
    "key" : "value",
    "sanjay" :"K J" ,
    "sachin" : 100,
    "list" :[32,344,45435],
    "rcb":{"abd":"superman"}
}
print(list(myDict.keys()))
print(myDict.values())
print(myDict.items()) #prints all (key,values ) in the dictionary
updateDict={
    "fsfs":342332,
    "sanjay k j ":"atla",
    "sanjay":"jagadeesh"
    }
#update the library by using another dictionary
myDict.update(updateDict)
myDict.update({1:3})
print(myDict)
#both are same 
print(myDict.get("sanjay")) 
print(myDict["sanjay"]) 

print(myDict.get("sanjay2")) #returns none
#print(myDict["sanjay2"]) #throws a error 