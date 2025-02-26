<h1>
    <p align="center">
        📖 Study Tracker
    </p>
</h1>

***"Study Tracker"*** is a simple study tracker cli built in python. To help 
you keep track of your studying progress. 

# ⚙️ Requirements

- Python 3+
- One of the following clipboards (to use clipboard functionality)
    - Wayland
        - wl-clipboard
    - X11
        - xsel
        - xclip

# 🚀 How To Run

Since this is basically a python script you just need to execute
```sh
python3 study-tracker.py # (or equivalent)
```
If you want to exit a session you press ```Enter```.

After you finish the session, the data is appended to study_session.json automatically.
You may want to change the inital starting date to ake the day number valid for when 
you started your grind 😃.

> [!NOTE]
> If you skip a day, the program will still continue incrementing the days,
> but it will be shown in the data that you skipped a day, you'll have to be the judge on that one.

# 🎯 Future Improvements 

- make the data analysis method include more cool stuff [Add more data analysis features #3](https://www.github.com/kiyubits/study-tracker/issues/3).
    - allow for graphs? it would be kinda cool to do with math/statistics packages.
- make a polybar module? [Status Bar Module #2](https://www.github.com/kiyubits/study-tracker/issues/2).
- Fix Windows clipboard compatibility [Can't Run on Windows #23](https://www.github.com/kiyubits/study-tracker/issues/23).
- Fix the Mac idle mode bug [Mac Idle Mode #21](https://www.github.com/kiyubits/study-tracker/issues/21).
- Fix "loginctl" issue for Mac (clipboard) [Can't run on mac because of loginctl #20](https://www.github.com/kiyubits/study-tracker/issues/20).
... 

## Lincense
This project uses the XYZ-License it can be found in the LINCESE file.
