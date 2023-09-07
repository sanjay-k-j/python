# k="bdgdgii\n fjf\tnjk f\f fdjd\'d ddd sanjay ajay"
# print(k)
# k=input("Enter yoour name ")
# print("Good morning "+k)

letter=''' Dear <|Name|>,
You are selected!
Date: <|DATE|>
'''
name=input("Enter your name")
date=input("enter date ")
let=letter.replace("Name",name)
let=let.replace("DATE",date)
print(let)