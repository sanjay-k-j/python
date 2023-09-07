# identical files
with open("copy.txt") as f:
    f1 = f.read()
with open("sample.txt") as f:
    f2 = f.read()
if f1==f2:
    print("Files are identical ")
else:
    print("files are not identical ") 