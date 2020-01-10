import random    
import sys
def main(): # This runs the functions instructions and colors. 
    instructions()
    colors()
    
def instructions(): # This contains the instructions for the game.
    print """
    This is a mastermind game. The goal is to figure out the code. The code will be made of 4 different colors. 
    You have to figure out the different colors and what order they are in. You have 10 attempts to guess the code. You start by typing in 
    4 color either a combination of colors or the same colors. Types in one color then press enter. Make sure nothing is capitalized and that there are no spaces.
    Your color options are blue, black, yellow, orange, purple, brown, red, and pink. The program will then tell you white or green. 
    White means that color is in the code somewhere. Green means that you have the right color in the right spot. If you see nothing the color is not in the code.
    You might what to grab a piece of paper and a pencil top help you figure out the code. Also you might what to write down the colors. 
    
    Type in a color to begin.
    """ # These are the instructions for the game.
      
def colors():# This provides the programing code for the game. It creates the code for the game, it allows the player to guess, and it compares the player's guess to the code. It tells the player whether they are right and help them along the way if they are wrong. 
    a = 9 # This creates the variable a to be used later. This helps countdown how many turns that player has to guess.  
    code = [ '', '', '', ''] # This creates the list code.
    colors = ['blue', 'black', 'yellow', 'orange', 'purple', 'brown', 'red', 'pink'] # This is the list of colors the program can choice from.
    l = 0 # This creates the variable l for later use. This helps the while loop to end.
    j = 0 # This creates the variable j for later use. This helps creates the list code.
    while l != 4: # This nested while loop creates the code for the game and makes it so the colors in the code will not repeat.           
            d = 0 # # This creates the variable j for later use. This helps to end the while loop.
            while d != 1:
                x = random.randint(0, 7) # This assigns the variable x a random number between 0 and 7 including 0 and 7.  
                if colors[x] != code[0] and colors[x] != code[1] and colors[x] != code[2] and colors[x] != code[3]: # This if statement make it so the colors will not repeat in the code. it compares the color to all the parts of the code to make sure it doesn't repeat.
                  code[j] = colors[x] # This recreates the list code.
                  l += 1 # This allows l to add 1 to itself. It helps to end the first while loop.
                  d = 1 # This allows d to add 1 to itself. It helps to end the second while loop.
                  j += 1 # This allows j to add 1 to itself. It helps to create the list code.              
    color = code[0] + code[1] + code[2] + code[3] # This creates the variable color which has the code stored in it. 
    guesses = ['', '', '', ''] # This creates the list guesses.
    for i in range (10): # This for loop run most of the game it allows the player 10 chances to guess the code.
        m = 0 # This creates the variable m for later use. This helps creates the list guesses.
        for i in range(4):# This for loop allows the player to guess the code. It stores the player's guess in the list guesses and store the players guesses in the variable guess.
            k = 0 # This creates the variable k for later use so the for loop can go through the list guesses.
            guess = raw_input() # This allows the player to write their guess of what color is in the code.
            guesses[m] = guess # This recreates the list guesses.
            m += 1 # This allows m to add 1 to itself. This help creates the list guesses.  
        guess = guesses[0] + guesses[1] + guesses[2] + guesses[3] # This creates the variable guess which holds the player's guesses.  
        print("") 
        for i in range (4): # This nested for loops compares the players guesses to the code. 
            x = 0 # This creates the variable x for later use so the for loop can go through the list code. 
            for i in range(4):
               if guess == color: # This if statement compares the variable guess and colors. If guess is equal color it will say "You win!" and it will tell the player the code. Then it will exit out of the game.
                   print('You win! the code was ' + code[0] + ' ' + code[1] + ' ' + code[2] + ' ' + code[3] + '.')
                   sys.exit()
               if guesses[k] == code[x]: # This if statement compares the lists guesses and code. If  guesses is equal to code it will go to two more if statements. 
                   if k == x: # This if statement compares the variables k and x. If they are the same it will print green and end this for loop. 
                       print('green')
                       break
                   if k != x:# This if statement compares k and x. if k and x isn't equal it will print white and end this for loop. 
                       print('white')
                       break
               x += 1 # This allows x to add 1 to itself letting the for loop go through the list code. 
            k += 1 # This allows k to add 1 to itself letting the for loop go through the list guesses. 
        print('You have ' + str(a) + ' more time to guess the code') # This tells the player how many more times they have to guess.
        a -= 1 # This counts down how many turns the player has left. 
        guesses = ['', '', '', '']# This resets the list guesses
    print('You did not figure out the code. The code is ' + code[0] + ' ' + code[1] + ' ' + code[2] + ' ' + code[3] + '.') # If the player can't not figure out the code in 10 guesses then it will print "You did not figure out the code." and it will show the player what the code was. 