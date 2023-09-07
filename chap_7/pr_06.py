 # rename a file 
import os
oldname= "sample2.txt"
new = "renamed_by_python.txt"
with open(oldname) as a:
    content = a.read()
with open(new,"w") as a:
    a.write(content)
os.remove(oldname)