import sys
import random
from pyfiglet import Figlet


def main():
    if not (len(sys.argv) == 1 or len(sys.argv) == 3):
        sys.exit('Invalid usage')
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        selected_font = random.choice(fonts)
    elif len(sys.argv) == 3:
        command, selected_font = sys.argv[1:]
        if not (command == '-f' or command == '--font') or selected_font not in fonts:
            sys.exit('Invalid usage')
    figlet.setFont(font=selected_font)
    str = input('Input: ')
    print('Output:')
    print(figlet.renderText(str))


if __name__ == '__main__':
    main()
