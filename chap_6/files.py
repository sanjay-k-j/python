# use open function
f=open('D:\work\python\chap_6\sample.txt','r') # by defalut reads
#data = f.read()
data = f.read(5) # only 5 characters
print(data)
f.close()