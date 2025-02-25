a simple study tracker in python that makes the terminal show a screen to indicate a session is in progress.

# Future Improvements

- make the data analysis method include more stuff
  - allow for graphs? it would be kinda cool to with with math/statistics packages
- polybar module?

# Requirements
- python 3+
- One of the following clipboards in order to use the session copy feature: 
    - Wayland
        - wl-clipboard
    - X11
        - xsel 
        - xclip

# How To Run

you just need to run it like any python file, and i don't think extra packages are needed

```python3 study-tracker.py``` (or equivalent)

press `enter` after entering a session to end it.

json data is appended to `study_sessions.json` automatically. you may want to change the initial starting date to make the day number valid for when you started your grind :)

as a minor note, if you skip a day, it'll still continue incrementing the days, but it will be shown in the data that you skipped a day, you'll have to be the judge on that one

rn i think i could make the study session screen a bit cooler, maybe with cooler ascii art or smth animated? also i wanna flesh out the analyse data script to be more detailed, like most hours studied in a week, or day that i tend to study most, etc. but all of that's doable as long as the data exists in the first place
