import random, time, copy
from termcolor import cprint
class bcolours:
  ResetAll     = '\033[0m'
  Default      = "\033[39m"
  Black        = "\033[30m"
  Red          = "\033[31m"
  Green        = "\033[32m"
  Yellow       = "\033[33m"
  Blue         = "\033[34m"
  Magenta      = "\033[35m"
  Cyan         = "\033[36m"
  LightGray    = "\033[37m"
  DarkGray     = "\033[90m"
  LightRed     = "\033[91m"
  LightGreen   = "\033[92m"
  LightYellow  = "\033[93m"
  LightBlue    = "\033[94m"
  LightMagenta = "\033[95m"
  LightCyan    = "\033[96m"
  White        = "\033[97m"
#Introduction to the game minesweeper.
print()
print('\033[93mHi, welcome to my minesweeper game! I hope you enjoy playing it.\033[97m')
print('================================================================')
print("\033[32mHave fun!\033[97m")
print() 
#Sets up the game.
def reset():
    print('''
MAIN MENU
=========
\033[36m>>>\033[97m For the rules and goals:\ntype '\033[33mI\033[97m'\n
\033[36m>>>\033[97m To play right now:\ntype '\033[32mP\033[97m'
''')
    choice = input('Enter letter here:\033[93m ').upper()
    
    if choice == 'I':
        print("\033[H\033[J")
        #This part of the code will access a different file and print whatever is inside that file, in a print statement.
        print("\033[97m")
        print(open('instructions.txt.', 'r').read())
        input('Press [\033[32menter\033[97m] when ready to play. ')

        time.sleep(1.5)
        print("\033[H\033[J")
        a = 1
        #prints a loading screen for the player/user with two pretty flowers.
        while a < 10:
          print('\033[32m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!            ', "\033[93m", a, "\033[32m", a,'\033[96mGame will be starting in\033[32m', a, "\033[93m", a, "\033[32m", "            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",)       
      
          print("\n                                  \033[32m!!!!!!!!!!!!!\033[96m              \033[31m***\033[96m10s\033[31m***   \033[32m          !!!!!!!!!!!!!")

          print("""
      \n\n\033[97m





                      \033[31m,\033[97m'   \033[31m,\033[97m'        \033[31m,\033[97m'                  \033[31m,\033[97m'   \033[31m,\033[97m'          \033[31m,\033[97m'
                  \033[31m,\033[97m'          \033[31m,\033[97m'                     \033[31m,\033[97m'           \033[31m,\033[97m'                                     
                        \033[31m,\033[97m'                                 \033[31m,\033[97m'
                      \033[31m,\033[97m'        \033[31m,\033[97m'                       \033[31m,\033[97m'         \033[31m,\033[97m'
              \033[35m.,.\033[31m         ,\033[97m'                    \033[35m .,.\033[31m         ,\033[97m'
            \033[35m.`.`.`.\033[31m   ,\033[97m'\033[31m      ,\033[97m'               \033[35m.`.`.`.\033[31m  ,\033[97m'\033[31m       ,\033[97m'
            \033[35m.`.`.`.`.\033[31m   ,\033[97m'\033[31m  ,\033[97m'                 \033[35m.`.`.`.`.\033[31m   ,\033[97m'\033[31m  ,\033[97m'
            \033[35m.`.`.`.`.\033[31m                          \033[35m.`.`.`.`.\033[31m
            \033[35m.`.`.`.`.\033[31m  ,\033[97m'\033[31m     ,\033[97m'               \033[35m.`.`.`.`.\033[31m  ,\033[97m'\033[31m     ,\033[97m'
            \033[35m\\`.`.`.\033[31m      ,\033[97m'                   \033[35m\\`.`.`.\033[31m      ,\033[97m'\033[31m
             \033[35m/\.,.\033[31m   ,\033[97m'\033[31m     ,\033[97m'                  \033[35m/\.,.\033[31m   ,\033[97m'\033[31m     ,\033[97m'
            \033[32m///                                \033[32m///
          :::                                :::
          :::                                :::
        ///                                ///
        :::                                :::
        :::                                :::           
        :::                                :::
       ///                                 ///
     :::                                  :::
     ///                                 ///
     :::                                :::
\033[92m/   /  /        / /   /  /        / /   /  /        / /   /  /        / /   /  /        / /   /  /        / /   /  /  / / /
:   :  :        :   /  / :   :  :        :   /  / :   :  :        :   /  / :   :  :        :   /  / :   :  :        : / / :
/:  /   :     /  :  :  : /:  /   :     /  :  :  : /:  /   :     /  :  :  : /:  /   :     /  :  :  : /:  /   :     / : / : :
 /: : : / /    ::   :  :  :     /  / / /  /: : : / /    ::   :  :  :     /  / / / /: : : / /    ::   :  :  : /  / / / : : : 
:: / :: :    / :  /  /  / /   :  : : : :: / :: :    / :  /  /  / /   :  : : :  :: / :: :    / :  /  /  / /   :  : : : / / /
/ ::  /  : : :  : :  :  : : : / : : : / ::  /  : : :  : :  :  : : : /   : : : / ::  /  : : :  : :  :  : : : /   : : : : : :
 //  :  / / /  / /  /  / / / :  / / /   //  :  / / /  / /  /  / / / : / / /  //  :  / / /  / /  /  / / / :   / / / / / : ///
: : : :  : : : :  : : : :  : : : :  : : : :  : :  :  : : :  :  : : :  :  : : :  : : :  : : :  : : :  : : :  : : :  : : : :::
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")
          a += 1
          time.sleep(1)
          print("\033[H\033[J")




    #Player doesn't want to see the rules/instructions and just wants to play the game.    
    elif choice != 'P':
        print("\033[H\033[J")
        reset()



    time.sleep(1.5)
    print("\033[H\033[J")

    a = 1
    #same thing as line56
    while a < 10:
      print('\033[32m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!            ', "\033[93m", a, "\033[32m", a,'\033[96mGame will be starting in\033[32m', a, "\033[93m", a, "\033[32m", "            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",)       
      
      print("\n                                  \033[32m!!!!!!!!!!!!!\033[96m              \033[31m***\033[96m10s\033[31m***   \033[32m          !!!!!!!!!!!!!")
      
      
      
      
      print("""
      \n\n\033[97m





                      \033[31m,\033[97m'   \033[31m,\033[97m'        \033[31m,\033[97m'                  \033[31m,\033[97m'   \033[31m,\033[97m'          \033[31m,\033[97m'
                  \033[31m,\033[97m'          \033[31m,\033[97m'                     \033[31m,\033[97m'           \033[31m,\033[97m'                                     
                        \033[31m,\033[97m'                                 \033[31m,\033[97m'
                      \033[31m,\033[97m'        \033[31m,\033[97m'                       \033[31m,\033[97m'         \033[31m,\033[97m'
              \033[35m.,.\033[31m         ,\033[97m'                    \033[35m .,.\033[31m         ,\033[97m'
            \033[35m.`.`.`.\033[31m   ,\033[97m'\033[31m      ,\033[97m'               \033[35m.`.`.`.\033[31m  ,\033[97m'\033[31m       ,\033[97m'
            \033[35m.`.`.`.`.\033[31m   ,\033[97m'\033[31m  ,\033[97m'                 \033[35m.`.`.`.`.\033[31m   ,\033[97m'\033[31m  ,\033[97m'
            \033[35m.`.`.`.`.\033[31m                          \033[35m.`.`.`.`.\033[31m
            \033[35m.`.`.`.`.\033[31m  ,\033[97m'\033[31m     ,\033[97m'               \033[35m.`.`.`.`.\033[31m  ,\033[97m'\033[31m     ,\033[97m'
            \033[35m\\`.`.`.\033[31m      ,\033[97m'                   \033[35m\\`.`.`.\033[31m      ,\033[97m'\033[31m
             \033[35m/\.,.\033[31m   ,\033[97m'\033[31m     ,\033[97m'                  \033[35m/\.,.\033[31m   ,\033[97m'\033[31m     ,\033[97m'
            \033[32m///                                \033[32m///
          :::                                :::
          :::                                :::
        ///                                ///
        :::                                :::
        :::                                :::           
        :::                                :::
       ///                                 ///
     :::                                  :::
     ///                                 ///
     :::                                :::
\033[92m/   /  /        / /   /  /        / /   /  /        / /   /  /        / /   /  /        / /   /  /        / /   /  /  / / /
:   :  :        :   /  / :   :  :        :   /  / :   :  :        :   /  / :   :  :        :   /  / :   :  :        : / / :
/:  /   :     /  :  :  : /:  /   :     /  :  :  : /:  /   :     /  :  :  : /:  /   :     /  :  :  : /:  /   :     / : / : :
 /: : : / /    ::   :  :  :     /  / / /  /: : : / /    ::   :  :  :     /  / / / /: : : / /    ::   :  :  : /  / / / : : : 
:: / :: :    / :  /  /  / /   :  : : : :: / :: :    / :  /  /  / /   :  : : :  :: / :: :    / :  /  /  / /   :  : : : / / /
/ ::  /  : : :  : :  :  : : : / : : : / ::  /  : : :  : :  :  : : : /   : : : / ::  /  : : :  : :  :  : : : /   : : : : : :
 //  :  / / /  / /  /  / / / :  / / /   //  :  / / /  / /  /  / / / : / / /  //  :  / / /  / /  /  / / / :   / / / / / : ///
: : : :  : : : :  : : : :  : : : :  : : : :  : :  :  : : :  :  : : :  :  : : :  : : :  : : :  : : :  : : :  : : :  : : : :::
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      """)
      a += 1
      time.sleep(1)
      print("\033[H\033[J")


    


    #Populates the grid. Basically what happens is these zero's don't have any variables right now but when they get put into the grid some of them will get mines on them well others will give you points!
    populator = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for n in range (0, 10):
        placeBomb(populator)

    for y in range (0, 9):
        for x in range (0, 9):
            value = l(y, x, populator)
            if value == '*':
                updateValues(y, x, populator)
    #Sets the variable grid to a grid of blank spaces, because nothing is yet known about the grid.
    values = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    #prints the grid so the player can see the grid.
    printBoard(values)
    #Start timer.
    startTime = time.time()
    #This is when the game starts and the player can play.
    play(populator, values, startTime)
#Gets the value of each box inside the grid, so when the player inputs the cordinates the program will know what they're saying.
def l(y, x, populator):
    return populator[y][x]
#Places the miens around the grid to make the game a challenge for the user.
def placeBomb(populator):
    y = random.randint(0, 8)
    x = random.randint(0, 8)
    #Checks if there's a bomb in the randomly generated location. If not, it puts one there. If there is, it tries a new box to try placing a mine there.
    currentRow = populator[y]
    if not currentRow[x] == '*':
        currentRow[x] = '*'
    else:
        placeBomb(populator)
#In this loop it adds 1's in around box around the mine (not the whole grid just the box's around the mine)
def updateValues(yn, x, populator):
    #Prints 1's on the top of the box the mine is in.
    if yn-1 > -1:
        y = populator[yn-1]
        if x-1 > -1:
            if not y[x-1] == '*':
                y[x-1] += 1

        if not y[x] == '*':
            y[x] += 1

        if 9 > x+1:
            if not y[x+1] == '*':
                y[x+1] += 1
    #Prints 1's in the box's beside the box that has a mine in it.   
    y = populator[yn]
    if x-1 > -1:
        if not y[x-1] == '*':
            y[x-1] += 1

    if 9 > x+1:
        if not y[x+1] == '*':
            y[x+1] += 1
    #Prints 1's in the box's under the box that has mine in it.
    if 9 > yn+1:
        y = populator[yn+1]
        if x-1 > -1:
            if not y[x-1] == '*':
                y[x-1] += 1

        if not y[x] == '*':
            y[x] += 1

        if 9 > x+1:
            if not y[x+1] == '*':
                y[x+1] += 1
#When a zero is found, all the squares around it are opened. Minesweeper does this to save time for the player/user.
def zeroProcedure(y, x, values, populator):
    #Goes through the row above the box the user has just opened with a 0 in it. Does this till it hits a 1, 2 or mine.
    if y-1 > -1:
        row = values[y-1]
        if x-1 > -1: row[x-1] = l(y-1, x-1, populator)
        row[x] = l(y-1, x, populator)
        if 9 > x+1: row[x+1] = l(y-1, x+1, populator)
    #Goes through the row beside the box the user has just opened with a 0 in it. Does this till it hits a 1, 2 or mine.
    row = values[y]
    if x-1 > -1: row[x-1] = l(y, x-1, populator)
    if 9 > x+1: row[x+1] = l(y, x+1, populator)
    #Goes through the row under the box the user has just opened with a 0 in it. Does this till it hits a 1, 2 or mine.
    if 9 > y+1:
        row = values[y+1]
        if x-1 > -1: row[x-1] = l(y+1, x-1, populator)
        row[x] = l(y+1, x, populator)
        if 9 > x+1: row[x+1] = l(y+1, x+1, populator)
#Checks known grid for 0s.
def checkZeros(values, populator, y, x):
    oldGrid = copy.deepcopy(values)
    zeroProcedure(y, x, values, populator)
    if oldGrid == values:
        return 
    while True:
        oldGrid = copy.deepcopy(values)
        for x in range (9):
            for y in range (9):
                if l(x, y, values) == 0:
                    zeroProcedure(x, y, values, populator)
        if oldGrid == values:
            return
#Places a marker wherever the player thinks there is one (eg. mE4), if a player puts that in it will place a red flag showing that shows that's where th eplayer thinks there is a mine.
def marker(y, x, values):
    values[y][x] = '\033[31m???\033[97m'
    printBoard(values)
#prints the grid so the player can see the grid.
def printBoard(populator):
    print("\033[H\033[J")
    print('    \033[96mA   B   C   D   E   F   G   H   I')
    print('  \033[97m???????????????????????????????????????????????????????????????????????????????????????????????????????????????')
    for y in range (0, 9):
        print(y,'???',l(y,0,populator),'???',l(y,1,populator),'???',l(y,2,populator),'???',l(y,3,populator),'???',l(y,4,populator),'???',l(y,5,populator),'???',l(y,6,populator),'???',l(y,7,populator),'???',l(y,8,populator),'???')
        if not y == 8:
            print('  ???????????????????????????????????????????????????????????????????????????????????????????????????????????????')
    print('  ???????????????????????????????????????????????????????????????????????????????????????????????????????????????')
#Let's the player choose their cordinates, so they can progress/play the game.
def choose(populator, values, startTime):
    #Defiens the variables of the cordinates for the player.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    #Loops this part of the code in case the program has an invalid entry.
    #This part of the code also prints what the player can do and how to input a flag or open a box.
    while True:
        chosen = input('\033[97m\n  \033[36m>>>\033[97m Choose a box\033[93m ???\033[97m (eg. \033[32mE4)\n  \033[36m>>>\033[97m If you want to make a marker to where you think a mine is type (eg. \033[31mmE4\033[97m)\n\n  Type here:\033[32m').lower()
        #Checks/makes sure the box they have entered is a valid box or if it's not.
        print("\033[94m")
        if len(chosen) == 3 and chosen[0] == 'm' and chosen[1] in letters and chosen[2] in numbers:
            x, y = (ord(chosen[1]))-97, int(chosen[2])
            marker(y, x, values)
            play(populator, values, startTime)
            break
        elif len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers: return (ord(chosen[0]))-97, int(chosen[1])
        else: choose(populator, values, startTime)    
#This is basically where the gameplay comes together. By that I mean this is where the user gets to do stuff.
def play(populator, values, startTime):
    #When the player chooses a box to open, it allows them to do so.
    x, y = choose(populator, values, startTime)
    #Gets the value fo the box the palyer wanted to open, basically checks to see what's in there, whether that be 0, 1, 2 or a mine.
    v = l(y, x, populator)
    #If the player opens a box and hits a mine, it'll end the game.
    if v == '*':
        printBoard(populator)
        print('  \033[31mYou Lose\033[97m!')
        #Gives the player their time it took them to lose.
        print('  \033[33mTime\033[97m:\033[32m ' + str(round(time.time() - startTime)) + '\033[97ms') 
        #Offers the player if they ant to play the game again. 
        playAgain = input('  Play again? (\033[32mY\033[97m/\033[31mN\033[97m): ').lower()
        if playAgain == 'y':
            print("\033[H\033[J")
            reset()
                    else:
            #Gives the player a sentimental text sayign bye and their always welcome to come back.
            print("\n  \033[36mAw that's too bad. Hope you have a wonderful day, come back at any time bye!")
            time.sleep(2)
            print("\033[H\033[J")
            time.sleep(.50)
            quit()
            
    #Puts that value into the known grid (grid).
    values[y][x] = v
    #Runs checkZeros() if that value is a 0 or else.
    if v == 0:
        checkZeros(values, populator, y, x)
    printBoard(values)
    #Checks to see if you have won.
    squaresLeft = 0
    for x in range (0, 9):
        row = values[x]
        squaresLeft += row.count(' ')
        squaresLeft += row.count('???')
    if squaresLeft == 10:
        printBoard(populator)
        print('You win!')
        #Print time it took the player to win the game.
        print('Time: ' + str(round(time.time() - startTime)) + 's')
        #Offers the player the option to play again!
        playAgain = input('Play again? (Y/N): ')
        playAgain = playAgain.lower()
        if playAgain == 'y':
            print("\033[H\033[J")
            reset()
        #If the player doesn't want tqo playa agin it'll give the same sentimental text.    
        else:
            print("Aw that's too bad. Hope you have a wonderful day, come back at any time bye!")
            time.sleep(1.5)
            quit()
    #Repeats the game if the player wanted to play the game again!!!
    play(populator, values, startTime)
#restarts the game and gives the grid new values.
reset()

