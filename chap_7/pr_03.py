# line number 
cont = True
i=1
with open("log.txt") as f :
    
    while cont:
        cont = f.readline()
        if "python" in cont.lower():
            print(f"python is present in the line {i}")
            
        i+=1
        