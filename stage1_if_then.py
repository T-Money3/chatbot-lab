"""
STAGE 1: if / elif / else
=========================
Goal: a bot that reacts to a few things you type.

Run it:   python stage1_if_then.py
Quit it:  type  bye
"""

from safety import check_safety   # a safety net added by your teacher. Leave it.

BOT_NAME = "Crumbs"   # TODO 1: give your bot a name

print(f"{BOT_NAME}: Hi, I am a retired cafeteria toaster. What is on your mind? (type 'bye' to leave)")

while True:
    # .lower() turns "HELLO" into "hello" so we only have to check one spelling
    user_input = input("You: ").lower()

    safety_message = check_safety(user_input)
    if safety_message:
        print(f"{BOT_NAME}: {safety_message}")
        continue

    if user_input == "bye":
        print(f"{BOT_NAME}: Goodbye. Take care.")
        break
    elif "hello" in user_input or "hi" in user_input:
        print(f"{BOT_NAME}: Hello! How are you feeling today?")
    elif "sad" in user_input:
        print(f"{BOT_NAME}: I am sorry to hear that. Why do you feel sad?")
    elif "school" in user_input:
        print(f"{BOT_NAME}: Tell me more about school.")
    # TODO 2: add at least 3 more `elif` rules about topics YOU choose.
    # TODO 3: make one of your rules react to TWO different words (use `or`).
    elif "toast" in user_input or "bread" in user_input:
        print(f"{BOT_NAME}: Toast?! Finally someone gets it. How do you like yours?")
    elif "music" in user_input or "song" in user_input:
        print(f"{BOT_NAME}: What song is stuck in your head right now?")
    elif "tired" in user_input or "sleep" in user_input:
        print(f"{BOT_NAME}: How much sleep did you actually get last night?")
    elif "game" in user_input:
        print(f"{BOT_NAME}: What game have you been playing the most lately?")
    elif "dog" in user_input:
        print(f"{BOT_NAME}: Dogs always tried to steal toast in the cafeteria. What is your dog's name?")
    else:
        print(f"{BOT_NAME}: Please go on.")


# ---------------------------------------------------------------------------
# BUG HUNT (do this after your TODOs)
# ---------------------------------------------------------------------------
# Run the bot and type:   this is hard
# Why does the bot say "Hello!"?  (Hint: what does `"hi" in "this"` give you?)
# Write your guess here:
#   `in` checks if the text shows up ANYWHERE inside the string, not just as its
#   own word. "this" is t-h-i-s, so "hi" is inside it and `"hi" in "this is hard"`
#   is True. The hello rule is the first elif so it wins before the bot even
#   checks anything else. Same thing happens with "nothing", "history", "which",
#   etc. Also "game" would match "endgame" and "dog" would match "hotdog".
# We will fix this properly in Stage 2 by breaking the sentence into WORDS.
