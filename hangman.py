class Hangman(object):  
    
    def __init__(self, level=5, non_ascii=False, dictionary=r'C:\Users\Salma\Documents\GitHub\randomwords.'):
        self.level = level
        self.non_ascii = non_ascii
        self.dictionary = dictionary 
            
     
    def play(self):
        play = True
        while play: 
            
            #Import the word to be guessed from another file.
            import random
            word = random.choice([word for word in open('randomwords.py')]) 
            word = word.lower().strip() #Makes the word lowercase and gets rid of extra spaces (using strip()) so we don't have to worry about that later.
            #print(word) #Reveal the word before playing by uncommenting this line.
            
            #Dealing with the level.
            if len(word) >= self.level: #If the length of the word is greater than or equal to the level then continue playing.
                pass
            else: #If the length of the word is shorter than the level then restart the play by importing another longer word.
              continue
            
            #Dealing with the Ascii and non-Ascii characters.
            if self.non_ascii == False:
                if all(ord(letters) < 128 for letters in word):
                    pass
                else: 
                    continue
            elif self.non_ascii == True:
                pass
            
            #Setup before game starts.
            tries = 6
            usedletters = [] #Append correct and incorrect letters to this list.
            board = ['-----\n|   |\n|   \n|   \n|   \n|   \n|   \n',
                     '-----\n|   |\n|   0\n|   \n|   \n|   \n|   \n',
                     '-----\n|   |\n|   0\n|   |\n|   \n|   \n|   \n',
                     '-----\n|   |\n|   0\n|  /|\n|   \n|   \n|   \n',
                     '-----\n|   |\n|   0\n|  /|\ \n|  \n|   \n|   \n',
                     '-----\n|   |\n|   0\n|  /|\ \n|  /\n|   \n|   \n',
                     '-----\n|   |\n|   0\n|  /|\ \n|  / \ \n|   \n|   \n']
            x = board[0]
            print(x)
            guessline = '' #The line above the dashes that we will be making edits to during the game.
            #Print number of dashes corresponding to letters in word.
            dashes = (len(word))*'- '
            print(dashes)
            
            #Playing game.
            while tries != 0:
                guess = input('Guess a letter:').lower()
                if (len(guess) != 1): #If guess is longer than one letter or character.
                    print("'" + guess + "'" + " is not a valid input. One letter at a time...")
                    print(x)
                    print(guessline)
                    print(dashes)
                elif guess in usedletters: #If you've already guessed that letter.
                    print("You have already guessed '" + guess + "'!")
                    print(x)
                    print(guessline)
                    print(dashes)                
                elif guess in word: #if guess is in the word.
                    print('Correct!')
                    print(x)
                    usedletters.append(guess) 
                    for guess in word: 
                        guessline = (''.join((a + ' ') if a in usedletters else '  ' for a in word))
                    print(guessline)
                    print(dashes) 
                    check = str(guessline.replace(' ', '').strip()) #Checking if guessline is equal to word.
                    if check == word:
                        print('You win! :)')
                        break #Should prompt user to play again once it breaks here.                
                elif guess not in word: 
                    usedletters.append(guess)
                    tries -= 1
                    print('Wrong!')
                    x = board[(len(board)-1) - tries]
                    print(x)
                    print(guessline)
                    print(dashes)
            if tries == 0: #Once you lose the game.
                print('You lost! :(')
                print('The correct answer is: ' + word)
            
            
            playagain = input('Another game? (y/n)').lower() #Prompting user if they want to play again. 
            while (playagain != 'y') and (playagain != 'n'):
                print('That is not a valid input.')
                playagain = input('Another game? (y/n)').lower()
            if playagain == 'n':
                break
            elif playagain == 'y': 
                play = True
    

if (__name__ == '__main__'):
    hangman = Hangman()
        
h = Hangman()
h = Hangman(level=3, non_ascii = False)
h.play()