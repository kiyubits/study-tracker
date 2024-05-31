a simple study tracker in python that makes the terminal show a screen to indicate a session is in progress.

# Future Improvements

- make the data analysis method include more stuff
  - allow for graphs? it would be kinda cool to with with math/statistics packages
- polybar module?

# Personal Goals

i'm personally using this to keep track of my study sessions and i wanted to keep the data somewhere for accountability, so might as well keep it here lol. my daily habit is studying physics everyday, just going through a textbook and learning its cool concepts, including exercises because those are super helpful at reinforcing understanding

right now i'm working on `Griffiths, Schroeter - Introduction to Quantum Mechanics Third Edition`

books i want to work on in the future
- `Arken, Weber, Harris - Mathematical Methods for Physicists: A Comprehensive Guide`
- `Neilsen, Chuang - Quantum Computation and Quantum Information`

stuff i want to learn
- quantum computing (this may take its time, wanna get to the point where i'm making quantum circuits to take some kind of measurements)
  - specifically, VQE algorithms to measure energy states. i wanna measure this using mathematical models!!! 
- vector calculus
- fourier analysis
- complex analysis
- statistical mechanics
- path integrals
- quantum field theory
- general relativity (black holes, parallel dimension stuff? i'm more invested into quantum stuff but knowledge of this is surely useful)
- quantum chemistry (this might seem farfetched, but i wanna expand my quantum expertise lol)
- computer science concepts (this is on the table)

some of this stuff i'll probably learn during uni, but i find that going through it in my own time, and at my own pace works so much better for me, especially for these topics which i needa spend a lotta time on

# How To Run

you just need to run it like any python file, and i don't think extra packages are needed

```python3 study-tracker.py``` (or equivalent)

press `enter` after entering a session to end it.

json data is appended to `study_sessions.json` automatically. you may want to change the initial starting date to make the day number valid for when you started your grind :)

rn i think i could make the study session screen a bit cooler, maybe with cooler ascii art or smth animated? also i wanna flesh out the analyse data script to be more detailed, like most hours studied in a week, or day that i tend to study most, etc. but all of that's doable as long as the data exists in the first place
