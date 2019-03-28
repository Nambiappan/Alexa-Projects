# Alexa-Projects
The project contains the Alexa Practice projects for Beginners ( Python - Flask Ask)

Project 1 : Alexa Word Game
Level : Beginner
Effort : 2 hour

To be honest, I spent more time to get this word game working as I am new to Python Programming and Alexa. I faced issues (see below) while installing the Flask-ask package in  my machine  and  then understaning the Alexa : Intent , Slot and Utterences.
Once I understood , it looked very simple program.

The App works as below :

	1. Me:  Alexa , Play Word Game
	2. Alexa  : Hello There, Would you like to play the word game
	3. Me. : Lets Play
	4. Alexa : The Word Starts with the letter  - {a...z}
	5. Me : Is it {....} ?
		If the guess is correct : 
			6. Alexa : Supper , you guessed it right. The word is {...}
		If the guess is InCorrect :
			7. Alex : Sorry It is correct. Do you want Clue ?
			8. Me : First Clue Please?
			9. Alex : { .....}  Ex : It is wild animal.
			10. Me : Is it {...} ?
				If the guess is correct : 
					11. Alexa : Supper , you guessed it right. The word is {...}
				If the guess is InCorrect :
					12. Alex : Sorry It is correct. Do you want  Clue ?
					13. Me : Second Clue Please?
					14. Alex : { .....}  Ex : It is an National Animal of India.
					15. Me : Is it {....} ?
					If the guess is correct : 
						16. Alexa : Supper , you guessed it right. The word is {...}
					If the guess is InCorrect :
						17. Alexa : Sorry Better luck next time. The Word is {.....}
		18. Me : I give up
		19.Alexa : The Word is {....}
		
Before jumping into action for the project , I would suggest you to go through the basics of 

1. Flask_Ask package and it is minimum required code structure.
2. Alexa - Launch Intent , Built-In Intent , Custom Intent , Fall Back Intent

	
Issues Faced:					
1. During installation of Flask-ask , I was getting the "python setup.py egg_info" failed with error code 1".  However this was resolved after degrading the PIP version 9.0.3. ( pip3 install pip=9.0.3)

2. Next error was related to Cryptograpy package version. The current version of cryptograpy was not supporting my code . Hence I had to degrade it to <2.2 which resolved my error. ( pips install cryptograpy< 2.2)

					
References :
1. https://flask-ask.readthedocs.io/
2. https://pythonprogramming.net/testing-deploying-alexa-skill-flask-ask-python-tutorial/?completed=/headlines-function-alexa-skill-flask-ask-python-tutorial/


