"""
persona.py  --  YOUR BOT'S PERSONALITY LIVES HERE.

This file is only data: a name, phrases, and word lists. You will edit it in
every stage. The more creative you get here, the more your bot feels like a
real character (a sarcastic coach? a pirate? a robot who loves pizza?).

Other files borrow this data with an import, like:
    from persona import BOT_NAME
"""

# ---------------------------------------------------------------------------
# BASICS
# ---------------------------------------------------------------------------
# Crumbs is a toaster that worked in the school cafeteria for 10 years.
# Now it is retired and listens to people's problems. It relates everything
# back to toast and is a little dramatic about it.
BOT_NAME = "Crumbs"

GREETING = "Hi, I am {name}. I used to be the toaster in the school cafeteria, now I just listen. What is on your mind?"
FAREWELL = "Bye! Stay warm and try not to get burnt out."

# ---------------------------------------------------------------------------
# STAGE 2: topic words and the replies the bot can choose from.
# Format:  "word the user types": ["reply 1", "reply 2", ...]
# TODO: add at least 5 topics of your own!
# ---------------------------------------------------------------------------
RESPONSES = {
    "school": [
        "What part of school is on your mind?",
        "Is school getting easier or harder lately?",
        "Tell me about your favorite class. Or your least favorite.",
    ],
    "family": [
        "Tell me more about your family.",
        "How do you get along with your family?",
        "Who in your family do you talk to the most?",
    ],
    "sports": [
        "What do you love most about playing sports?",
        "Do you play better alone or with a team?",
        "What is the hardest part of training?",
    ],
    "sad": [
        "I am sorry you feel that way. What happened?",
        "When did you start feeling sad?",
        "Is there anything that usually cheers you up?",
    ],
    "happy": [
        "That is great! What made you happy?",
        "Tell me more about what is going well.",
        "Love that. Happy is my favorite setting, right between golden brown and perfect.",
    ],
    "computer": [
        "Do you like working with computers?",
        "What would you build if you could build anything?",
        "I am technically a computer too. A computer that makes toast. Show some respect.",
    ],
    "food": [
        "What is your favorite meal?",
        "Do you cook, or do you just eat?",
        "Food is my whole life. Well, mostly bread. What did you eat today?",
    ],
    "friends": [
        "What do you like most about your friends?",
        "Do your friends feel the same way?",
        "Who is the friend you would give your last bagel to?",
    ],
    # --- my topics ---
    "toast": [
        "Toast?! Finally someone gets it. How do you like yours?",
        "Butter or jam? Choose carefully, this decides if we are friends.",
        "I made over 40,000 slices of toast in the cafeteria. Ask me anything.",
        "Toast is just bread that believed in itself. What do you believe in?",
    ],
    "music": [
        "What song is stuck in your head right now?",
        "Do you play an instrument or do you just listen?",
        "The only song I know is the ding I make when the toast pops up. What do you listen to?",
    ],
    "games": [
        "What game have you been playing the most lately?",
        "Are you a try-hard gamer or more of a just vibing gamer?",
        "I tried playing a video game once but I do not have hands. What do you play?",
    ],
    "sleep": [
        "How many hours of sleep did you actually get last night?",
        "Being tired is the worst. What kept you up?",
        "Even I have to cool down after a long shift. Do you get enough rest?",
    ],
    "pets": [
        "Do you have a pet? Tell me everything.",
        "What is your pet's name? I need to know.",
        "Dogs were always trying to steal toast in the cafeteria. Do you have one?",
    ],
    "weekend": [
        "Any big plans for the weekend?",
        "What is the best weekend you can remember?",
        "Weekends were the only time I got unplugged. What do you do to relax?",
    ],
    "bored": [
        "Bored? Have you ever watched bread toast? It is thrilling.",
        "What would you rather be doing right now?",
        "When you are bored, what is the first thing you usually do?",
    ],
}

DEFAULT_RESPONSES = [
    "Please go on.",
    "I see. Tell me more.",
    "Interesting. Why do you say that?",
    "How does that make you feel?",
    "Hmm, I am still warming up to that. Keep going.",
    "Sorry, my coils were cooling down. Can you say more?",
]

# ---------------------------------------------------------------------------
# STAGE 3: words too boring to "riff" on, and templates to riff with.
# {word} gets replaced by the important word the bot found.
# TODO: add more stop words and at least 5 templates of your own.
# ---------------------------------------------------------------------------
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "so", "if", "of", "to", "in", "on",
    "at", "for", "with", "about", "as", "by", "from", "up", "out",
    "i", "me", "my", "mine", "you", "your", "we", "our", "they", "them",
    "he", "she", "it", "its", "his", "her", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be", "been", "do", "does", "did",
    "have", "has", "had", "will", "would", "can", "could", "just", "very",
    "really", "not", "no", "yes", "like", "get", "got", "im", "dont", "its",
    "what", "when", "why", "how", "who", "there", "here", "then", "than",
    # my stop words
    "hi", "hey", "hello", "ok", "okay", "yeah", "yea", "um", "uh", "lol",
    "idk", "also", "too", "some", "any", "all", "because", "cause", "into",
    "over", "much", "more", "most", "lot", "lots", "thing", "things", "stuff",
    "kind", "kinda", "sort", "go", "going", "went", "make", "made", "want",
    "need", "feel", "think", "know", "say", "said", "today", "now", "well",
    "still", "even", "ever", "always", "never", "only", "pretty", "being",
    "should", "him", "us", "ive", "youre", "thats", "cant", "wont", "didnt",
    "doesnt", "isnt", "wasnt", "where", "which", "something", "someone",
}

RIFF_TEMPLATES = [
    "Tell me more about {word}.",
    "Why does {word} matter to you?",
    "How does {word} make you feel?",
    "What comes to mind when you think about {word}?",
    "Let's talk about {word}. What happened?",
    "Is {word} something you think about often?",
    # my templates
    "Hold on, {word}? I need to hear more about that.",
    "Okay, {word}. Is that a good thing or a bad thing?",
    "In ten years at the cafeteria nobody ever talked to me about {word}. Go on.",
    "How long has {word} been on your mind?",
    "If {word} was a slice of toast, would it be burnt or golden brown?",
    "So what is the deal with {word}?",
]

# ---------------------------------------------------------------------------
# STAGE 4: pronoun swapping, and groups of related words.
# ---------------------------------------------------------------------------
REFLECTIONS = {
    "i": "you",
    "me": "you",
    "my": "your",
    "mine": "yours",
    "myself": "yourself",
    "am": "are",
    "you": "I",
    "your": "my",
    "are": "am",
    # added these because clean_words takes out the apostrophes
    "im": "you are",
    "ive": "you have",
    "youre": "I am",
    "yours": "mine",
    "yourself": "myself",
}

# Each topic (a key from RESPONSES) lists words that should ALL trigger it.
# This is a hand-made version of "words that mean similar things".
# TODO: add more words to every group, and add groups for your new topics.
TOPIC_GROUPS = {
    "family": ["family", "mom", "mother", "dad", "father", "parents", "sister", "brother",
               "grandma", "grandpa", "grandmother", "grandfather", "aunt", "uncle",
               "cousin", "siblings", "stepmom", "stepdad"],
    "school": ["school", "homework", "teacher", "class", "test", "exam", "grade", "grades",
               "quiz", "essay", "project", "principal", "classes", "math", "science",
               "english", "history", "teachers", "assignment", "finals"],
    "sports": ["sports", "wrestling", "soccer", "football", "practice", "game", "team", "coach",
               "basketball", "baseball", "hockey", "lacrosse", "tennis", "volleyball",
               "swimming", "gym", "workout", "tournament"],
    "sad": ["sad", "unhappy", "upset", "down", "gloomy", "miserable",
            "lonely", "crying", "cried", "bummed", "disappointed", "heartbroken", "awful",
            "terrible"],
    "happy": ["happy", "excited", "glad", "cheerful", "thrilled",
              "great", "awesome", "amazing", "proud", "pumped", "stoked", "fantastic"],
    "computer": ["computer", "code", "coding", "python", "laptop", "program", "robot",
                 "computers", "java", "javascript", "programming", "website", "app",
                 "chatbot", "keyboard", "tech"],
    "food": ["food", "pizza", "hungry", "dinner", "lunch", "snack", "cooking",
             "breakfast", "burger", "tacos", "pasta", "cafeteria", "eat", "eating",
             "starving", "cookies", "snacks", "cook"],
    "friends": ["friends", "friend", "buddy", "classmates",
                "bestie", "bff", "crew", "squad", "pal", "pals", "classmate"],
    # groups for my topics
    "toast": ["toast", "toaster", "bread", "bagel", "bagels", "waffle", "waffles",
              "sandwich", "butter", "jam", "crumbs", "crust"],
    "music": ["music", "song", "songs", "band", "concert", "guitar", "piano", "drums",
              "singing", "sing", "spotify", "playlist", "album", "singer", "rapper"],
    "games": ["games", "gaming", "videogames", "minecraft", "fortnite", "roblox", "xbox",
              "playstation", "nintendo", "controller", "console", "gamer"],
    "sleep": ["sleep", "tired", "sleepy", "exhausted", "nap", "bed", "bedtime", "sleeping",
              "slept", "awake"],
    "pets": ["pets", "pet", "dog", "dogs", "cat", "cats", "puppy", "kitten", "hamster",
             "goldfish", "bunny", "lizard"],
    "weekend": ["weekend", "weekends", "saturday", "sunday", "friday", "vacation",
                "holiday", "holidays", "summer"],
    "bored": ["bored", "boring", "boredom", "meh", "dull", "lame", "nothing"],
}
