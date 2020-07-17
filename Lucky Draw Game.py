from random import randint

def generator():
    return randint(1,10)

def rand_guess():
    rand_no=generator()
    guess_left=3
    flag=0
    while guess_left>0:
        guess=int(input("Pick your number to "
                        "enter the lucky draw\n"))
        if guess==rand_no:
            flag=1
            break
        else:
            print("Wrong Guess!!")
        guess_left-=1
        if guess>rand_no:
            print("Maybe Less than what you entered")
        else:
            print("Maybe Greater")
    if flag == 1:
        return True
    else:
        return False

if __name__=="__main__":
    if rand_guess() is True:
        print("Congrats!! You Win.")
    else:
        print("Sorry,You Lost!")
