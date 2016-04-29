# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/

print("Welcome to the internet quiz!Answers are all in lower case")
level_userinput = input("Please choose a difficult level: easy, medium or difficult \n")



number_of_blanks = ["___1___","___2___", "___3___", "___4___", "___5___"]

mode_easy = "LAN stands for ___1___. WAN stands for ___2___. LAN covers ___3___ areas. WAN covers ___4___ areas. Both constitute different type of ___5___."
mode_medium = "Speed of LAN is around ___1___ mbps while speed of WAN is around ___2___ mbps. LAN uses ___3___ technology and WAN uses ___4___ technology. LAN have higher ___5___ transfer rate."
mode_difficult="LAN Layer 2 component is ___1___. Layer 1 component is ___2___. For WAN, layer 3 component is ___3___. The most ___4___ computer is the one not connected to any network. LAN's are ___5___ than WAN's."

easy_answers = ["local area network", "wide area network", "small", "large", "network"]
medium_answers = ["1000", "150", "ethernet", "frame relay", "data"]
difficult_answers = ["switches", "repeaters", "routers", "secure", "safer"]

def difficulty_level(level_userinput): #gets the difficulty level the user inputs and prints the question according to the level desired
    if level_userinput == "easy":
        print("easy level")
        return mode_easy
    elif level_userinput == "medium":
        print("medium Level")
        return mode_medium
    elif level_userinput == "difficult":
        print("difficult level")
        return mode_difficult

print(difficulty_level(level_userinput))

def answer(level_userinput): #select the list of answers according to the difficulty level desired
    if difficulty_level(level_userinput) == "easy":
        return easy_answers
    elif difficulty_level(level_userinput) == "medium":
        return medium_answers
    elif difficulty_level(level_userinput) == "difficult":
        return difficult_answers
        
def check_prompt(user_answer, answer, ans_index): #checks if the entered answer is correct or not by comparing with list of answers
    
        if user_answer == answer[ans_index]:
            return "Correct"
            
        else:
            return "Incorrect"
			
def compile_quiz(): #compiles all the different parts and displays the game and multiple levels of questions based on user input and allows to try multiple times comparing with check and answer functions
	quiz = difficulty_level(level_userinput)
	if quiz == mode_easy:
		answer = easy_answers
	elif quiz == mode_medium:
		answer = medium_answers
	elif quiz == mode_difficult:
		answer = difficult_answers
	answer_count=0
	blank_count=0
	print("How many tries you want")
	tries = input()
	tries = int(tries)
		
	while blank_count<len(number_of_blanks):
		while answer_count<len(answer):
				user_answer = input("answer for blank"+ number_of_blanks[blank_count] + "?")
				ans = check_prompt(user_answer, answer, answer_count)
				if ans == "Incorrect":
					count = 1
					while count<tries:
						print("Try again")
						user_answer = input("answer for blank"+ number_of_blanks[blank_count] + "?")
						ans = check_prompt(user_answer, answer, answer_count)
						if ans == "Correct":
							break
						count +=1
					print("Incorrect")
					answer_count+=1
					blank_count+=1
					
				elif ans == "Correct":
					print("Correct answer! next question...")
					quiz = quiz.replace(number_of_blanks[blank_count], user_answer)
					print(quiz)
					blank_count += 1
					answer_count += 1
					break
	return "Correct answers are" + str(answer)
                
        



			
print(compile_quiz())