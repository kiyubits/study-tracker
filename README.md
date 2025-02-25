
<h1>
    <p align="center">
        📖 Study Tracker
    </p>
</h1>

Study Tracker is a simple study tracker in python that makes the terminal show a screen to help the user keep track of their study session.  
The tool helps to keep track of your studies, and your success. The user gets a short but concise.  

```
Studying Physics Everyday Until I Graduate University | Day 288
Session 1: 01:37:55 PM - 01:53:19 PM (00:15:23)
Session 2: 10:54:00 PM - 11:26:01 PM (00:32:01)
Total time spent studying today: 0:47:24 
```

Giving the user a quick overview of what they achived today. This started as a solo project by the head dev [kiyubits](https://github.com/kiyubits). 
But has now received updates from multiple devs, be it crossplatform support (comming soon), or a splash screen.   

# 🚀 Future Improvements

- make the data analysis method include more stuff
  - allow for graphs? it would be kinda cool to with with math/statistics packages
- polybar module?
- cross platform (clipboard support for windows) [#23](https://github.com/kiyubits/study-tracker/issues/23)
- Mac Idle Mode [#21](https://github.com/kiyubits/study-tracker/issues/21)
- Mac "loginctl" clipboard issues [#20](https://github.com/kiyubits/study-tracker/issues/20)

# 🔗 Requirements
- python 3+
- One of the following clipboards in order to use the session copy feature: 
    - Wayland
        - wl-clipboard
    - X11
        - xsel 
        - xclip

# ⚙️How To Run

This is a simple python project, and should run without any dependencies, (python 3.x+) is needed. Just run:  
```python3 study-tracker.py``` (or equivalent)

press `enter` after entering a session to end it.

json data is appended to `study_sessions.json` automatically. you may want to change the initial starting date to make the day number valid for when you started your grind :)

as a minor note, if you skip a day, it'll still continue incrementing the days, but it will be shown in the data that you skipped a day, you'll have to be the judge on that one

rn i think i could make the study session screen a bit cooler, maybe with cooler ascii art or smth animated? also i wanna flesh out the analyse data script to be more detailed, like most hours studied in a week, or day that i tend to study most, etc. but all of that's doable as long as the data exists in the first place


## 📃 License
This project uses the XYZ-License it can be found in the LICENSE file
