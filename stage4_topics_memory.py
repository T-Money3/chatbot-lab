"""
STAGE 4: Related words, pronoun swapping, and memory
====================================================
Three upgrades that make the bot feel a lot smarter:

  A. TOPIC GROUPS   "mom", "dad", "sister" all mean the topic "family".
  B. REFLECTION     "I hate my homework" -> "Why do you say you hate your homework?"
  C. MEMORY         Remember earlier important words and circle back to them.

Run it:   python stage4_topics_memory.py
"""

import random

from chat_loop import run_chat
from persona import RESPONSES, DEFAULT_RESPONSES, RIFF_TEMPLATES, REFLECTIONS, TOPIC_GROUPS
from stage2_word_lists import clean_words
from stage3_important_word import find_important_word

remembered = []     # important words from earlier in the conversation
brought_up = []     # CHALLENGE 1: old words the bot already circled back to

# CHALLENGE 2: mood tracker
mood_counts = {"sad": 0, "happy": 0}
last_mood = None


# ---------------------------------------------------------------------------
# A. Topic groups (this is a hand-made version of "words that mean similar things")
# ---------------------------------------------------------------------------
def find_topic(words):
    """Return the topic name (a key of RESPONSES) if any word belongs to a
    group in TOPIC_GROUPS, otherwise None."""
    for topic, group in TOPIC_GROUPS.items():
        for word in words:
            if word in group:
                return topic
    return None


# ---------------------------------------------------------------------------
# B. Reflection
# ---------------------------------------------------------------------------
def reflect(words):
    """Swap perspective: ['i', 'am', 'sad'] -> 'you are sad'."""
    # TODO 1: Right now this just glues the words back together unchanged.
    #   Build a new list called `swapped`. For each word: if it is a key in
    #   REFLECTIONS, add REFLECTIONS[word]; otherwise add the word itself.
    #   Then return " ".join(swapped).
    swapped = []
    for word in words:
        if word in REFLECTIONS:
            swapped.append(REFLECTIONS[word])
        else:
            swapped.append(word)
    return " ".join(swapped)


# ---------------------------------------------------------------------------
# CHALLENGE 2: mood tracker
# ---------------------------------------------------------------------------
def update_mood(topic):
    """Count sad vs happy topics. If the mood flips from the last time,
    return a comment about it. Otherwise return None."""
    global last_mood
    mood_counts[topic] += 1
    comment = None
    if last_mood == "sad" and topic == "happy":
        comment = (f"Ooh, things are turning around! That is {mood_counts['sad']} sad "
                   f"and {mood_counts['happy']} happy so far.")
    elif last_mood == "happy" and topic == "sad":
        comment = (f"Uh oh, we went from golden brown to burnt real quick. That is "
                   f"{mood_counts['sad']} sad and {mood_counts['happy']} happy so far.")
    last_mood = topic
    return comment


# ---------------------------------------------------------------------------
# The brain
# ---------------------------------------------------------------------------
def get_reply(user_input):
    words = clean_words(user_input)
    important = find_important_word(words)

    # C. Memory: save this turn's important word for later
    if important is not None:
        remembered.append(important)

    # TODO 2 (memory callback): every so often, bring up something from earlier.
    #   Fill in the blank so the bot picks a RANDOM old word (not just the first).
    if len(remembered) >= 3 and random.random() < 0.25:
        # remembered[:-1] leaves out the word from THIS turn.
        # CHALLENGE 1: also skip words we already brought up, and the word the
        # user just said (in case they said it earlier too).
        choices = []
        for w in remembered[:-1]:
            if w not in brought_up and w != important and w not in choices:
                choices.append(w)
        if len(choices) > 0:
            old_word = random.choice(choices)
            brought_up.append(old_word)
            return f"Earlier you mentioned {old_word}. Does that connect to this?"

    # Topic groups first
    topic = find_topic(words)
    if topic is not None:
        reply = random.choice(RESPONSES[topic])
        if topic == "sad" or topic == "happy":
            comment = update_mood(topic)
            if comment is not None:
                return comment + " " + reply
        return reply

    # Reflection: when the user is talking about themselves
    if ("i" in words or "my" in words) and len(words) >= 3:
        return f"Why do you say {reflect(words)}?"

    # Riff on the important word
    if important is not None:
        return random.choice(RIFF_TEMPLATES).format(word=important)

    return random.choice(DEFAULT_RESPONSES)


if __name__ == "__main__":
    run_chat(get_reply)


# ---------------------------------------------------------------------------
# YOUR TURN
# ---------------------------------------------------------------------------
# TODO 3: Expand TOPIC_GROUPS in persona.py. Add 5+ words to every group and
#         create groups for your own topics (don't forget matching RESPONSES!).
#   Done. Every group has 5+ new words and I made groups for toast, music,
#   games, sleep, pets, weekend, and bored. I made sure no word is in two
#   groups, because find_topic just returns the first group it finds.
#
# CHECKPOINT: type "I am nervous about the dance". Is the reply grammatical?
#   Yes: "Why do you say you are nervous about the dance?" reflect() swaps
#   i -> you and am -> are, and none of the words are in a topic group, so
#   it gets to the reflection rule.
#   Now type "I hate my homework". Why did you get a DIFFERENT kind of reply?
#   (Hint: look at the ORDER of the rules in get_reply. Order matters!)
#   It said something like "What part of school is on your mind?" because
#   "homework" is in the school group, and the topic group check comes BEFORE
#   the reflection check in get_reply. The first rule that matches returns, so
#   reflection never runs. (Sometimes you also get the "Earlier you mentioned"
#   line instead, since memory is checked even before topics.)
#
# THINK (this is the big idea behind word2vec): you just typed lists of words
#   that "mean the same thing" BY HAND. What if a program could LEARN those
#   groups by reading millions of sentences? Your teacher will discuss this.
#   It would look at which words show up around each word. "mom" and "dad"
#   both show up next to stuff like "my ___ said" or "picked me up", so the
#   program would figure out they are similar without anyone telling it.
#   That would cover way more words than I could ever type, including slang
#   and misspellings. The downside is it learns whatever is in the text, even
#   if it's wrong or biased.
#
# CHALLENGE 1: Don't let the memory callback repeat the same old word twice.
#   Done with the brought_up list.
# CHALLENGE 2: Add a mood tracker: count how many "sad" topics vs "happy"
#   topics came up, and have the bot comment when the conversation turns.
#   Done with mood_counts and update_mood().
