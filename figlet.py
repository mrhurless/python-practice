"""
In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
    *Zero if the user would like to output text in a random font.
    *Two if the user would like to output text in a specific font, in 
    which case the first of the two should be -f or --font, and the second of the two should be the name of the font.

Prompts the user for a str of text.

Outputs that text in the desired font.

"""
import sys
from pyfiglet import Figlet
from random import randint
import getopt

fig_font = ''

#load font list
f = Figlet()
fonts = f.getFonts()

if len(sys.argv) == 3:
    # Remove 1st argument from the
    # list of command line arguments
    argumentList = sys.argv[1:]
 
    # Options
    options = "f:"
    
    # Long options
    long_options = ["font"]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-f", "--font"):
                if argumentList[1] in fonts:
                    fig_font=argumentList[1]
                else:
                    print("Invalid Usage")
                    sys.exit()
            else:
               print("Invalid Usage")
               sys.exit()
             
    except getopt.error as err:
        print("Invalid Usage")
        sys.exit()

elif len(sys.argv) == 1:
    #determine length of list
    count = 0
    for i in fonts:
        count += 1

    fig_font = fonts[randint(0,count)]
    # print('random font: ' + rand_font)

else:
    print("Invalid Usage")
    sys.exit()

text = input("Input: ").strip()

f = Figlet(font=fig_font)

print(f.renderText(text)) 