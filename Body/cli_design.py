from pyfiglet import Figlet
import os

def design():
    os.system('CLS')
    f=Figlet(font='slant')
    print (f.renderText('DESKTOP Assistant'))
    