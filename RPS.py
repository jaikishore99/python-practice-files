import sys
user1=input("U1 = what is your name ?")
user2=input("U2 = what is your name ?")
user1_answer=input("%s, do you want to chose rock,paper or scissors ?" % user1)
user2_answer=input("%s, do you want to chose rock,paper or scissors ?" % user2)
def compare(u1, u2):
    if u1 == u2:
        return("draw match!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins !")
        else:
            return("Paper wins !")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors wins !")
        else:
            return("Rock wins !")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins !")
        else:
            return("Scissors wins !")
    else:
        return("Invalid input! you have not entred rock , paper , scissors , try again.")
print(compare(user1_answer, user2_answer))                        