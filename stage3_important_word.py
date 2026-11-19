"""
STAGE 3: Find the important word and riff on it
===============================================
Dr. Sbaitso and ELIZA could keep talking about almost anything with a simple
trick: pick one important word out of your sentence and ask about it.

Plan:
  1. If the user mentions a topic we know -> use the Stage 2 reply.
  2. Otherwise find the "important" word and plug it into a template:
         "Tell me more about {word}."

Run it:   python stage3_important_word.py
"""

import random

from chat_loop import run_chat
from persona import RESPONSES, DEFAULT_RESPONSES, STOP_WORDS, RIFF_TEMPLATES
from stage2_word_lists import clean_words   # reuse your Stage 2 function!

last_template = None   # CHALLENGE: remember the last template so we don't repeat it


def find_first_word(words):
    """VERSION 1: the first word that is not a boring stop word."""
    for word in words:
        if word not in STOP_WORDS:
            return word
    return None


# TODO 1 (VERSION 2): "first word" is not always the best word.
#   Change the function so it returns the LONGEST word that is not a stop
#   word. Longer words are often more specific ("homework" vs "bad").
#   Hint: keep a variable called `best` and update it inside the loop.
def find_longest_word(words):
    """VERSION 2: the LONGEST word that is not a stop word."""
    best = None
    for word in words:
        if word not in STOP_WORDS:
            if best is None or len(word) > len(best):
                best = word
    return best


# TODO 2 (VERSION 3): invent your own scoring. For example: +2 points if
#   the word is a key in RESPONSES, +1 point per letter over 5, -1 point
#   if it appears in the first position. Highest score wins.
def score_word(word, position, total):
    """VERSION 3: my own scoring system.
       - start with 1 point per letter (longer words are usually more specific)
       - +5 if it is a topic the bot knows (a key in RESPONSES)
       - -3 if it ends in "ed" or "ly" (usually a verb or adverb like
         "assigned" or "totally", not the thing the person is talking about)
       - +2 if it is the last word (people tend to end on the main thing)
       - -1 if it is the first word
    """
    score = len(word)
    if word in RESPONSES:
        score += 5
    if word.endswith("ed") or word.endswith("ly"):
        score -= 3
    if position == total - 1:
        score += 2
    if position == 0:
        score -= 1
    return score


def find_important_word(words):
    """Return the most important word in the list, or None if there is none.
    Uses my scoring (VERSION 3). If two words tie, the first one wins.
    """
    best = None
    best_score = 0
    for i in range(len(words)):
        word = words[i]
        if word in STOP_WORDS:
            continue
        score = score_word(word, i, len(words))
        if best is None or score > best_score:
            best = word
            best_score = score
    return best


def get_reply(user_input):
    global last_template
    words = clean_words(user_input)

    # Step 1: known topic?
    for word in words:
        if word in RESPONSES:
            return random.choice(RESPONSES[word])

    # Step 2: riff on the important word
    important = find_important_word(words)
    if important is not None:
        # only pick from templates that were NOT used last time
        choices = []
        for t in RIFF_TEMPLATES:
            if t != last_template:
                choices.append(t)
        template = random.choice(choices)
        last_template = template
        return template.format(word=important)

    # Step 3: nothing useful
    return random.choice(DEFAULT_RESPONSES)


if __name__ == "__main__":
    run_chat(get_reply)


# ---------------------------------------------------------------------------
# YOUR TURN
# ---------------------------------------------------------------------------
# TODO 3: Add 5+ templates of your own to RIFF_TEMPLATES in persona.py.
#         Make them sound like YOUR bot's personality.
#   Added 6 toaster themed ones in persona.py.
#
# TODO 4: Add 10+ stop words to STOP_WORDS. Try typing sentences and watch for
#         boring words the bot riffs on ("Tell me more about really...").
#   Added a bunch (hi, hey, lol, idk, stuff, thing, want, think, today...).
#   Before that it kept saying stuff like "Tell me more about idk."
#
# CHECKPOINT: type "my teacher assigned a gigantic project".
#   Which word did your bot pick? Is that the word YOU would have picked?
#   Version 1 picked "teacher" (first non stop word).
#   Version 2 picked "assigned". "assigned" and "gigantic" are both 8 letters
#   and it keeps the first one it finds, so it riffed on the worst word.
#   Version 3 (my scoring) picks "project": project = 7 + 2 for being last = 9,
#   gigantic = 8, teacher = 7, assigned = 8 - 3 for "ed" = 5.
#   "project" is the word I would have picked, that is what the sentence is
#   actually about.
#
# CHALLENGE: The bot sometimes uses the same template twice in a row. Keep a
#   variable called `last_template` and make sure the bot picks a different one.
#   Done: get_reply makes a list of every template except last_template and
#   picks from that, then saves the one it used.
