# game 
def game():
    return 3435665
score = game()
with open("highscore.txt") as f :
    H_score = f.read()
if H_score =="":
    with open("highscore.txt","w") as f :
        f.write(str(score))
elif score > int(H_score) :
    with open("highscore.txt","w") as f :
        f.write(str(score))