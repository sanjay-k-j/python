#write a dictionary
hindiWords ={
    "dabba":"box",
    "vastu":"object",
    "panka" : "fan"
}

print("the options are : ",hindiWords.keys())
key=input("Enter the word : ")
print(key+ " means " ,hindiWords.get(key))
