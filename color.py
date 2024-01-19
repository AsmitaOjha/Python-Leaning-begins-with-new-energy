BLACK = '\u001b[30m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
RED = '\u001b[31m'
WHITE = '\u001b[37m'
BLUE = '\u001b[34m'
CYAN = '\u001b[36m'
RESET = '\u001b[0m'

# print(WHITE, "This will be in white 🤍")
# print(GREEN, "This will be in green")
# print(CYAN, "This wil be cyan😇")
# print(YELLOW, "Yellow😏😏")
# print(RED, "You are my 💐🤍")
def colour_print(text: str, effects: str)->None:
    '''
    print 'text' using the ANSI sequences to change color, etc
    :param text: The text to print.
    :param effect:The effect we want. One of the constants defined at the start of this module.
    '''
    output_string = "{0}{1}{2}".format(effects, text, RESET)
    print(output_string)

colour_print("Hello, good evening",RED)
colour_print("Hello, good evening",CYAN)