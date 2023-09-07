words = ['sanjay' ,'puneeth','hemanth']
with open("D:\work\python\chap_7\sample.txt") as f :
    content = f.read()

for word in words:
    content=content.replace(word,"$%^*&^*&(*#$%#)")
    with open("sample.txt","w") as f :
        f.write(content)

