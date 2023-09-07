#spam
text = input("Enter the text\n")
if ("make money" in text):
    spam = True
elif("subscibe this" in text ):
    spam=True
elif("buy now" in text ):
    spam=True
elif("transfer successful" in text ):
    spam=True
elif("you won a lottery" in text ):
    spam=True
else:
    spam=False
if(spam):
    print("this is a spam ")
else:
    print("this is not a spam ")
    