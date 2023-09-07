# copy a file 
with open("sample.txt") as f:
    con=f.read()
with open("copy.txt", "w") as a:
    a.write(con)