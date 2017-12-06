# hugotbot.py
from nltk.chat.util import Chat, reflections

pairs = [
		[r'(.*)(blue)', ["Wrong!"]],
		[ r'(red|green|yellow|white|black)', ["%1  is fine. Good-bye."]],
		[ r'(.*)', ["I'm sorry the person who programmed me failed art class and doesn't know that color %1"]]
]

def hugot_bot():
    print("Whats your favorite color?")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    hugot_bot()
