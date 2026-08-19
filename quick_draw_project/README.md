# Project: Quick Draw

- Build a game that tests the player's reaction time. The idea is simple: the program tells the player to "get ready," waits for a random, unpredictable amount of time, then suddenly says "DRAW!" The player must respond as fast as they can, and the program measures how long they took.

# You'll use two built-in tools to make this work:

1. The **random** module, to make the wait time unpredictable so the player can't cheat by timing it.
2. The **time** module, to pause the program and to measure how many seconds elapsed.

# 🪜 How to approach this

- Tell the player to get ready. Print a message and warn them that "DRAW!" could appear at any moment.
- Wait a random amount of time. Pick a random number of seconds (say, between 2 and 5) and pause using time.sleep().
- Record the start moment. Just before you prompt the player, capture the current time with time.time().
- Capture the player's response. Use input() so the program waits for them to press Enter.
- Measure and report. Capture the time again, subtract the start time, and print how many seconds they took.

# A few details worth knowing:

- random.uniform(2, 5) returns a random decimal between 2 and 5, so the delay feels natural and varied.
- time.sleep(seconds) pauses your whole program for that many seconds.
- time.time() returns the current time as a number of seconds; subtracting two readings gives you the elapsed time.

# 💡 Key Insight

- Measuring "before" and "after" with time.time() is a pattern you'll use far beyond games — it's exactly how programmers measure how long any piece of code takes to run, which is the first step in making slow programs faster.