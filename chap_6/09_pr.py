words = ['sanjay' ,'puneeth','hemanth']
with open("D:\work\python\chap_6\sample.txt") as f :
    content = f.read()

for word in words:
    content=content.replace(word,"kj")
    with open("sample.txt","w") as f :
        f.write(content)

