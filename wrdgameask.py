import os
import logging
from flask import Flask
from flask_ask import Ask, statement, question, session,logger
import json
import requests
import time
import unidecode
import random


app = Flask(__name__)
ask=Ask(app,"/word_game")

wordlist= json.load(open("words.json"))

@app.route('/')
def homepage():
    return "Hi there , How are you doing?"

@ask.launch
def start_skill():
    welcome_message = "Hello there , would you like to play the word game?"
    return question(welcome_message)

@ask.intent("AMAZON.YesIntent")
def start_game():
    selectword = random.choice(list(wordlist.keys()))
    cluekeys= wordlist.get(selectword)
    gameword = selectword[0]
    session.attributes['selectword'] = selectword
    session.attributes['clue1'] = cluekeys.get("Clue1")
    session.attributes['clue2'] = cluekeys.get("Clue2")
    session.attributes['cluegiven'] = 0
    gameword_msg ="The word starts with the letter {}".format(gameword)
    return question(gameword_msg)

@ask.intent("AnswerIntent", convert={'WordSlot':str})
def play_game(WordSlot):
    logger.info('*********************************** *********** wordslot contains the value {} **********************'.format(WordSlot))
    if WordSlot.title() == session.attributes['selectword']:
        return statement("Super you guessed it right. It is - "+ session.attributes['selectword'] )
    else:
        else_msg ="Sorry it is incorrect word. Do you want clue"
        return question(else_msg)

@ask.intent("FirstClueIntent")
def give_firstclue():
    clue_msg ="Here is first clue .  {}".format(session.attributes['clue1'])
    return question(clue_msg)

@ask.intent("SecondClueIntent")
def give_secondclue():
    clue_msg ="Here is second clue .  {}".format(session.attributes['clue2'])
    return question(clue_msg)

@ask.intent("GiveUpIntent")
def give_up():
    giveup_msg ="Well tried . Better luck next time. The word is   {}".format(session.attributes['selectword'])
    return question(giveup_msg)

@ask.intent("AMAZON.NoIntent")
def no_intent():
    bye_text =" Thanks bye bye, Have a wonderfull day"
    return statement(bye_text)

if __name__ =="__main__":
    app.run(debug=True,host='0.0.0.0', port=8080)
