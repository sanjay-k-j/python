# read a file using with statement 
with open('D:\work\python\chap_6\sample.txt') as f:
    v=f.read()
    print(v)
# no need to write f.close()