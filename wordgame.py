import random

wordlist = {
    "Lion":{
    "Clue1":"It is Wild Animal",
    "Clue2":"It is King of Forest"
    },
    "Tiger":{
    "Clue1":"It is Wild Animal",
    "Clue2":"National animal of India"
    },
    "Tortoise":{
    "Clue1":"It goes very slowly",
    "Clue2":"It won the race against Hare"
    },
    "Aeroplane":{
    "Clue1":"It is transport",
    "Clue2":"It flies in the Air"
    },
}


def game(selectword,clues,cluegiven):
    guess= receiveinput()
    if checkuserinput(selectword,guess)=="True":
        print("Super you guessed it right. It is - "+guess)
    else:
        print("Sorry it is incorrect")
        cluereq = wantclue()
        if cluereq == "True":
            #print("want clue  -give clue")
            if int(cluegiven) < 2:
                print("The Clue is- " + clues[int(cluegiven)])
                cluegiven=int(cluegiven)+1
                game(selectword,clues,cluegiven)
            else:
                print("Sorry you could not get it right. The word is - "+selectword)
        elif cluereq == "False":
            #print("want clue false -call game again")
            game(selectword,clues,cluegiven)
        else:
            #print("don't know what user wants -give clue")
            game(selectword,clues,cluegiven)


def receiveinput():
    return input("Enter your guess = ")

def wantclue():
    wantclue1 =input("Do you want clue - y/n = ")
    if wantclue1 == "y":
        return "True"
    elif wantclue1 == "n":
        return "False"
    else:
        return "True"

def checkuserinput(selectword,guess):
    if selectword == guess:
        return "True"
    else:
        return "False"




selectword = random.choice(list(wordlist.keys()))
cluekeys= wordlist.get(selectword)
clue1= cluekeys.get("Clue1")
clue2= cluekeys.get("Clue2")
clues=[clue1,clue2]

print("The Word starts with the letter - > " + selectword[0])
game(selectword,clues,0)
