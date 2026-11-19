"""
STAGE 2: Break the sentence into a list of words
================================================
Stage 1's bug: "hi" matched inside "this". The fix: split what the user types
into a LIST of whole words, then look each word up in a DICTIONARY of topics
(see RESPONSES in persona.py).

Run it:   python stage2_word_lists.py
"""

import random
import string

from chat_loop import run_chat
from persona import RESPONSES, DEFAULT_RESPONSES


def clean_words(text):
    """Turn 'I LOVE School!!' into the list ['i', 'love', 'school']."""
    text = text.lower()
    for ch in string.punctuation:       # remove . , ! ? and friends
        text = text.replace(ch, "")
    return text.split()                 # split on spaces -> list of words


def get_reply(user_input):
    """The bot's brain: take the user's text, return a reply (a string)."""
    words = clean_words(user_input)

    # TODO 2: What if the user mentions TWO topics ("school and sports")?
    # Right now the bot only answers the FIRST one. Could you collect
    # all the topics in a list instead, and then pick one at random?
    topics = []
    for word in words:
        if word in RESPONSES and word not in topics:
            topics.append(word)

    if len(topics) > 0:
        topic = random.choice(topics)
        return random.choice(RESPONSES[topic])

    return random.choice(DEFAULT_RESPONSES)


if __name__ == "__main__":
    # (This line means: only start chatting when you run THIS file directly.
    #  Later stages import functions from this file, and we don't want the
    #  chat to start by accident when they do.)
    run_chat(get_reply)


# ---------------------------------------------------------------------------
# YOUR TURN
# ---------------------------------------------------------------------------
# TODO 1: Open persona.py and add at least 5 new topics to RESPONSES, each with
#         3+ replies. Run the bot and test every one.
#
# CHECKPOINT: type "this is hard". Does the bot still say "Hello"? (It should
#             not. Why is that fixed now?)
#   No, now it gives a default reply like "Please go on." clean_words turns the
#   sentence into ['this', 'is', 'hard'] and then `word in RESPONSES` checks if
#   the WHOLE word is a key in the dictionary. "this" is not a key, and "hi" is
#   never looked for inside other words anymore, so the bug is gone.
#
# THINK: type "I love my mom". The bot ignores "mom". Why? How could we teach
#        it that "mom" belongs with "family"? (Stage 4 answers this.)
#   "mom" is not a key in RESPONSES, only "family" is, and the bot only matches
#   exact keys. It has no idea mom and family are related. To fix it we could
#   make a list of words for each topic (mom, dad, sister...) and if any of
#   them show up, use the family replies.
