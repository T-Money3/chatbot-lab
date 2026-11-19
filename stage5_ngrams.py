"""
STAGE 5: Predicting the next word with n-grams
==============================================
Until now every reply came from a template YOU wrote. Now the bot will
GENERATE new sentences by learning which words tend to follow which words in
a text file (corpus.txt).

  Bigram  (n=2): looks at 1 word  to predict the next one.
  Trigram (n=3): looks at 2 words to predict the next one.

This is the simplest ancestor of the language models behind modern chatbots:
"given the words so far, what word probably comes next?"

Run it:   python stage5_ngrams.py
Special command inside the chat:   /peek school    (shows what the model learned)
"""

import random
from collections import Counter

from chat_loop import run_chat
from stage2_word_lists import clean_words
from stage3_important_word import find_important_word
from stage4_topics_memory import find_topic, get_reply as rules_reply

N = 3   # TODO 3: change to 3 (trigrams). What happens to the sentences?

# TODO 1 challenge: set this to True to always pick the MOST COMMON next word
# instead of a random one. (I left it False because True is boring, see below.)
PICK_MOST_COMMON = False


def load_corpus(path="corpus.txt"):
    """Read the text file and return a list of lines."""
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def build_model(lines, n=2):
    """Learn from the lines. Returns a dictionary:
         context (tuple of words)  ->  list of words that followed it

    For n=2 and the line "i like pizza", we learn:
         ("<start>",) -> ["i"]
         ("i",)       -> ["like"]
         ("like",)    -> ["pizza"]
         ("pizza",)   -> ["<end>"]
    """
    model = {}
    for line in lines:
        words = clean_words(line)
        tokens = ["<start>"] * (n - 1) + words + ["<end>"]
        for i in range(len(tokens) - (n - 1)):
            context = tuple(tokens[i : i + n - 1])
            next_word = tokens[i + n - 1]
            if context not in model:
                model[context] = []
            model[context].append(next_word)
    return model


def generate(model, n=2, seed=None, max_words=14):
    """Write a sentence one word at a time. If `seed` is given, start from a
    place where the seed word appears (so the bot 'riffs' on it)."""
    # choose a starting context
    starts = [c for c in model if seed is not None and seed in c]
    if starts:
        context = random.choice(starts)
    else:
        context = ("<start>",) * (n - 1)

    sentence = [w for w in context if w != "<start>"]

    while len(sentence) < max_words:
        options = model.get(context)
        if not options:
            break
        if PICK_MOST_COMMON:
            next_word = Counter(options).most_common(1)[0][0]
        else:
            next_word = random.choice(options)     # TODO 1: see the challenge below
        if next_word == "<end>":
            break
        sentence.append(next_word)
        context = tuple(list(context)[1:] + [next_word])

    return " ".join(sentence).capitalize() + "."


def peek(model, word):
    """Show the most likely next words after `word` (bigram models only)."""
    options = model.get((word,))
    if not options:
        return f"I never saw '{word}' in my corpus."
    top = Counter(options).most_common(5)
    pieces = [f"{w} ({count})" for w, count in top]
    return f"After '{word}' I usually see: " + ", ".join(pieces)


MODEL = build_model(load_corpus(), N)


def get_reply(user_input):
    # special command for exploring the model
    if user_input.startswith("/peek"):
        parts = user_input.split()
        if len(parts) < 2:
            return "Try:  /peek school"
        return peek(build_model(load_corpus(), 2), parts[1].lower())

    words = clean_words(user_input)
    important = find_important_word(words)

    # Known topics still get the Stage 4 treatment.
    # Otherwise, 60% of the time, try to generate a brand-new sentence.
    no_topic = find_topic(words) is None
    seen_it = important is not None and any(important in c for c in MODEL)
    if no_topic and seen_it and random.random() < 0.6:
        return generate(MODEL, N, seed=important)

    return rules_reply(user_input)     # fall back to everything from Stage 4


if __name__ == "__main__":
    run_chat(get_reply)


# ---------------------------------------------------------------------------
# YOUR TURN
# ---------------------------------------------------------------------------
# TODO 1 (CHALLENGE): `random.choice(options)` treats every option equally, but
#   `options` contains repeats, so common words ARE more likely. Try picking
#   the MOST COMMON next word every time instead (hint: Counter(options)
#   .most_common(1)). What happens to the bot? Why is it boring now?
#   It says the exact same sentence every time. With N = 2 and no seed I got
#   "A good friend would make today better." 3 times in a row. Every context
#   always leads to the same next word, so once the start is picked the whole
#   sentence is decided. There is no randomness left. With a seed it only
#   changes the first word, like "School can make today better." It also
#   only ever uses the most popular words so most of the corpus never shows up.
#
# TODO 2: Open corpus.txt and ADD 20+ lines in your bot's voice (jokes, advice,
#   catchphrases). Run it again. Your bot just learned a new personality
#   without you writing a single new if-statement.
#   Added 27 toast/cafeteria lines. Now it says things like "Practice is just
#   bread into steps." and "Food tastes better when the toast is ready." which
#   I never actually wrote.
#
# TODO 3: Set N = 3. Sentences should sound more natural but repeat the
#   corpus more. Why? (Hint: with 2 words of context, there are far fewer
#   possible next words.)
#   With N = 3 the model looks at 2 words at a time, and most 2 word pairs
#   only show up once in the corpus. I counted: 411 out of 485 contexts only
#   have ONE possible next word. So once it starts a line it usually has no
#   choice but to finish that exact line. When I generated 500 sentences, about
#   30% were exact copies of a corpus line (with N = 2 it was 0%). It only
#   makes something new when two lines share a pair of words, like "practice
#   is" + "is how", which gave "Practice is how your brain asking for something
#   new." The sentences sound more like real English because each word has to
#   fit with the 2 words before it, not just 1.
#   (/peek still uses a bigram model, so it works the same either way.)
#
# THINK: What would happen if corpus.txt had 10 MILLION lines instead of 38?
#   What if it had your whole class's chat history? What new problems appear?
#   With 10 million lines almost every pair of words would have lots of
#   possible next words, so even N = 3 or 4 could write new sentences that
#   sound pretty natural. But the dictionary would be huge and it would take
#   a long time to build and use a lot of memory (it rebuilds the model every
#   time you type /peek too). It still would not understand anything, it is
#   just guessing the next word from what it has seen.
#   With the class chat history it would talk like us, which is funny, but
#   it could repeat private stuff people said, people's names, or mean things
#   and bad words, since it copies whatever is in the text. Nobody agreed to
#   have their messages used either. You would have to clean the data first.
#
# SHOWCASE: Pick your best 3 minutes of conversation to show the class.
