# read lines 
f = open("D:\work\python\chap_6\sample.txt")
# reads first line 
data = f.readline()
print(data)

# read second line

data = f.readline()
print(data)

# read 3rd lind

data = f.readline()
print(data)

# read 4th line

data = f.readline()
print(data)

f.close()
# in binary mode we should use "rb" to read