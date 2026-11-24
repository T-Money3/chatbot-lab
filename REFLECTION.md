# My Chatbot: Reflection & Submission

**Name:** Turner C.  Period: __AI_____  **Bot name:** Crumbs

> Write in your own words. Short, specific answers beat long, vague ones. Refer to what **your** bot actually did.

---

## How to turn this in

1. Fill in this file (replace the blanks and the `[...]` prompts). Save it.
2. Make sure your best work is saved in `persona.py`, `corpus.txt`, and your stage files.
3. **Commit and push** your work:
   - Click the **Source Control** icon (left sidebar) → type a message like `Finished chatbot lab` → **Commit** → **Sync Changes**.
   - Or in the Terminal: `git add .` then `git commit -m "Finished chatbot lab"` then `git push`
4. Submit the **link to your repository** (the web address of your repo on GitHub) to your teacher, in the place they tell you.
   - Your repo must be one your teacher can open: either add your teacher as a collaborator, or ask which they prefer.
   - Don't put personal information (full name, address, phone, school ID) in your bot or your corpus.

**Stage checkpoints your teacher saw (teacher initials):**
Stage 1 ____  Stage 2 ____  Stage 3 ____  Stage 4 ____  Stage 5 ____

---

## Part 1: Meet my bot

**Personality in one sentence:** Crumbs is a retired school cafeteria toaster that now listens to people's problems and turns almost everything into a toast joke.

**Something I'm proud of in `persona.py` or `corpus.txt`:** The 27 toast lines I added to `corpus.txt`, like "toast is just bread that believed in itself" and "do not let one bad day burn the whole loaf". The bot mixes them with the original lines and makes new ones I never wrote, like "Food tastes better when the toast is ready."

**A real conversation.** Paste at least 8 lines of chat with your finished bot (copy from the Terminal):

```
Crumbs: Hi, I am Crumbs. I used to be the toaster in the school cafeteria, now I just listen. What is on your mind? (type 'bye' to leave)
You: hi
Crumbs: Please go on.
You: i had a really long day
Crumbs: Hard day feel shorter.
You: my teacher assigned a gigantic project
Crumbs: What part of school is on your mind?
You: im so tired
Crumbs: How many hours of sleep did you actually get last night?
You: i like my toast with butter
Crumbs: Toast?! Finally someone gets it. How do you like yours?
You: I am nervous about the dance
Crumbs: Why do you say you are nervous about the dance?
You: my dog ate my homework
Crumbs: Is school getting easier or harder lately?
You: we won our basketball game though so im happy
Crumbs: Do you play better alone or with a team?
You: what do you think about computers
Crumbs: What would you build if you could build anything?
You: bye
Crumbs: Bye! Stay warm and try not to get burnt out.
```

---

## Part 2: What I learned (answer all)

1. **The "hi in this" bug (Stage 1).** In your own words, why did the bot say "Hello!" to "this is hard", and how did splitting the sentence into a list of words fix it?

   In Stage 1 the bot checked `"hi" in user_input`, and `in` on a string looks for those letters anywhere, not just as a whole word. "this" has "hi" inside it (t-HI-s), so the hello rule was true, and since it was the first `elif` it won before any other rule got checked. In Stage 2, `clean_words` splits the sentence into a list like `['this', 'is', 'hard']` and the bot checks if each whole word is a key in the RESPONSES dictionary. "this" is not "hi", so the bug went away.

2. **Important word (Stage 3).** Which method does your bot use to pick the important word (first word, longest word, or your own scoring)? Give one example sentence where it picked a **good** word and one where it picked a **bad** word. Why?

   My bot uses my own scoring. Every word that isn't a stop word gets 1 point per letter, +5 if it's a topic in RESPONSES, -3 if it ends in "ed" or "ly", +2 if it's the last word, and -1 if it's the first word. Highest score wins.
   - **Good:** "my teacher assigned a gigantic project" picked **project** (7 + 2 = 9) over gigantic (8), teacher (7) and assigned (8 - 3 = 5). That's what the sentence is really about. The longest-word version picked "assigned", which was the worst choice.
   - **Bad:** "i went to the mall yesterday" picked **yesterday** and said "Let's talk about yesterday. What happened?" The important word is "mall", but "yesterday" is long and it's last, so it got 11 points and mall only got 4. Long words aren't always the important ones. I could fix this one by adding time words like "yesterday" and "tomorrow" to STOP_WORDS.

3. **Reflection and rule order (Stage 4).** What does `reflect()` do? Why did `I hate my homework` get a different kind of reply from `I am nervous about the dance`?

   `reflect()` swaps the point of view of the sentence. It goes through each word and if the word is in the REFLECTIONS dictionary it swaps it (i -> you, my -> your, am -> are), so "I am nervous about the dance" turns into "you are nervous about the dance" and the bot asks "Why do you say you are nervous about the dance?"
   "I hate my homework" got "What part of school is on your mind?" instead because "homework" is in the school topic group, and in `get_reply` the topic check comes before the reflection check. The first rule that matches returns a reply, so reflection never ran. "nervous" and "dance" aren't in any topic group, so that sentence made it down to the reflection rule.

4. **N-grams (Stage 5).** In your own words, what does the bot store in its model, and how does it use that to write a sentence? What changed when you used `N = 3` instead of `N = 2`, or when you added lines to `corpus.txt`?

   The model is a dictionary. Each key is the context (the last word for N = 2, or the last 2 words for N = 3) and the value is a list of every word that came right after it in `corpus.txt`. The list keeps repeats, so a word that showed up more often is more likely to get picked. To write a sentence it starts at `<start>` (or at a spot with my important word in it), uses `random.choice` to pick the next word from the list, slides the context over, and keeps going until it hits `<end>` or 14 words.
   With **N = 2** it made lots of new sentences but a lot of them made no sense ("Practice is just bread into steps."). With **N = 3** the sentences sounded more normal but it mostly just copied lines from the corpus. I counted and 411 out of 485 contexts only had one possible next word, so it usually had no choice. When I generated 500 sentences with N = 3, about 30% were exact copies of a corpus line, and with N = 2 none were. **Adding lines** to `corpus.txt` gave the bot my toaster personality without writing any new code, and gave it more options so the mixed sentences got more interesting.

---

## Part 3: Thinking like an engineer

5. **Where my bot fails.** Describe one thing it gets wrong or one reply that makes no sense. What would you need to change to fix it?

   It only uses the first topic group it finds, in the order they're listed in TOPIC_GROUPS, not the one that matters most. In my conversation, "my dog ate my homework" got "Is school getting easier or harder lately?" because school comes before pets in the dictionary. Same with "we won our basketball game though so im happy", which got a sports reply, so my mood tracker never counted the "happy". To fix it, I'd change `find_topic` to collect every matching topic in a list (like I did in Stage 2) and then pick one, or give feeling topics like happy and sad priority since those are usually what the person cares about most.

6. **Does it understand?** Your bot can keep a conversation going. Does it *understand* what you say? Explain what you think is different between what your bot does and what a person does.

   No. It doesn't know what any of the words mean. It looks for words in my lists, swaps pronouns, and fills in templates, and in Stage 5 it just picks a next word based on what came after that word in a text file. When I said "my dog ate my homework" it asked about school and totally missed the joke. When it says "Earlier you mentioned project", it picked that word at random, not because it saw a connection. A person understands what you mean and why you're saying it, remembers the whole conversation, and answers from their own experience. My bot is just matching patterns, it only seems like it's listening.

7. **Hand-made vs. learned.** In Stage 4 you typed lists of related words by hand (`mom`, `dad`, `sister` → family). Our class discussed how word2vec could learn those groups automatically. What is the advantage of learning them from lots of text? What could go wrong?

   The advantage is that it could learn way more words than I could ever type, including slang, misspellings, and new words, just by noticing which words get used in the same kinds of sentences. I only came up with around 7 to 20 words per group. What could go wrong: it learns whatever is in the text, including stereotypes and bias. Also, words that get used in the same spots aren't always similar. "happy" and "sad" both come after "I feel", so it might group them together, which would totally break my mood tracker. You also can't easily see why it put two words together.

8. **If I had more time**, the next feature I would add is: having the bot remember your name and use it later in the conversation, like "Earlier you mentioned project, Sam. Does that connect to this?" and I would start by: checking each message for the words "my name is", saving the word right after them in a variable, and adding some templates in `persona.py` with a `{name}` spot in them.

---

## Part 4: Honest process notes

- **Help I used** (classmates, teacher, websites, or AI tools), I used Claude when I didn't know how to push something to GitHub or know what to do for uploading certain things.
- **The hardest bug I fixed** and how I found it: In Stage 3 the longest-word version picked "assigned" for "my teacher assigned a gigantic project" instead of "project". "assigned" and "gigantic" are both 8 letters and the code keeps the first one it finds. I found it by printing the score for every word in the sentence, and I used the same printout to check that my scoring version picks "project".
- **Which stage was hardest, and why:** Stage 5. The model is a dictionary of lists keyed by tuples, which is harder to picture than the earlier stages, and it wasn't obvious why N = 3 kept copying lines. It made sense after counting that 411 of the 485 contexts only have one possible next word.
