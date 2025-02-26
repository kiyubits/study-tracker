import datetime
import json
import os
import random
import re
import signal
import sys
import threading
import time

from greeter import *
from color_output import *
from system_operations import copy_to_clipboard, find_clipboard
from utils import strfdelta, time_str_to_timedelta


affirmations = [
    "You did really well today!",
    "Good job today :)",
    "Keep going, you're improving everyday!",
    "I hope you had a good session hehe",
    "You are filled with determination.",
    "Well done! You deserved this.",
    "やった！",
    "Study hard what interests you the most in the most undisciplined, irreverent and original manner possible.",
    "The first principle is that you must not fool yourself and you are the easiest person to fool.",
]

valid_continue_responses = [
    "y", 
    "yes", 
    "", 
    "n", 
    "no"
]

TERM_OPEN = True
INIT = False

class StudySession:
    def __init__(self, filename):
        self.filename = "study_sessions.json"
        self.data = []
        self.halt = False
        self.day_number = 0
        self.start_time_str = None
        self.start_time = None
        self.progress_thread = None
        self.break_length_delt = None
        self.break_length_str = None
        self.curr_session_start_time = None
        self.multiple_sessions = False
        self.sessions = []

    def run_session(self):
        clear()
        # if ret == -1 not a valid input 
        while True:
            ret = greeter()
            time.sleep(0.3)
            clear()
            if (ret > 0):
                break

        if ret == 1:
            self.track_study_session()
        elif ret == 2:
            # start new session
            print("")
        elif ret == 3:
            processEnd(self)

    def calculate_session_length(self, start, end):
                session_length = end - start
                return session_length

    def track_study_session(self):
                if os.path.exists(self.filename):
                    with open(self.filename, "r") as file:
                        self.data = json.load(file)

                self.start_time = datetime.datetime.now()
                self.day_number = len(self.data) + 1
                self.start_time_str = self.start_time.strftime("%I:%M:%S %p")

                if len(self.data) != 0:
                    if self.data[len(self.data) - 1]["date"] == self.start_time.strftime("%Y-%m-%d"):
                        self.multiple_sessions = True
                        self.sessions = self.data[len(self.data) - 1]["sessions"]
                        self.day_number = len(self.data)
                        self.start_time = datetime.datetime.now()

                def display_session_progress():
                    global INIT
                    INIT = True
                    if (self.curr_session_start_time): 
                        calc_start_time = self.curr_session_start_time
                    else: 
                        calc_start_time = self.start_time

                    while not self.halt:
                        # Clear the screen
                        os.system("clear")

                        # Calculate the current session duration
                        current_time = datetime.datetime.now()
                        session_duration = current_time - calc_start_time
                        session_duration_str = strfdelta(session_duration)

                        print(colored_output(
                            f"""
             ╱|、
            (˚ˎ 。7     Session in progress... 
             |、˜〵     Elapsed time: {session_duration_str}
             じしˍ,)ノ
                        [Return] -> quit
                                """
                        ))
                        time.sleep(1)

                self.progress_thread = threading.Thread(target=display_session_progress)
                self.progress_thread.start()

                input()
                self.halt = True
                self.progress_thread.join()
                processEnd(self)


def processEnd(session: StudySession):
    # Ensure that prompting has completed before sessions file
    if(not INIT): 
        return

    end_time = datetime.datetime.now()
    end_time_str = end_time.strftime("%I:%M:%S %p")
    session_length = session.calculate_session_length(session.start_time, end_time)
    session_length_str = strfdelta(session_length)

    if session.multiple_sessions:
        session_data = {
            "start_time": session.start_time_str,
            "end_time": end_time_str,
            "session_length": session_length_str,
        }
        session.data[len(session.data) - 1]["sessions"].append(session_data)
    else:
       session_data = {
            "day": session.day_number,
            "date": session.start_time.strftime("%Y-%m-%d"),
            "sessions": [
                { 
                    "start_time": session.start_time_str,
                    "end_time": end_time_str,
                    "session_length": session_length_str,
                }
            ]
        }   
        
       session.data.append(session_data)

    with open(session.filename, "w") as file:
        json.dump(session.data, file, indent = 4)

    sessions = session.data[len(session.data) - 1]["sessions"]

    if TERM_OPEN:
        print(f"Studying Physics Everyday Until I Graduate University | Day {session.day_number}\n")
       
        total_session_length = datetime.timedelta()

        for i, s in enumerate(sessions, start = 1):
            print(f"Session {i}: {s["start_time"]} - {s["end_time"]} ({s["session_length"]})")
            total_session_length += time_str_to_timedelta(s["session_length"])

        print(f"Total time spent studying today: {total_session_length}\n")
            
        print(affirmations[random.randint(0, len(affirmations) - 1)])

        # get most recent day for clipboard

        clipboard_data = {
            "day": session.day_number,
            "sessions": sessions,
            "total_time": total_session_length,
        }

        copy_to_clipboard(clipboard_data)

def main():
    session = StudySession("study_sessions.json")
    find_clipboard()

    # sent to program when terminal is closed
    def sig_hup_handler(sig, *_):
        global TERM_OPEN
        session.halt = True
        session.progress_thread.join()
        # Ensure we don't try to print to a closed terminal
        TERM_OPEN = False
        processEnd(session)
        sys.exit(0)

    def sig_int_handler(sig, *_):
        session.halt = True
        processEnd(session)
        sys.exit(0)

    signal.signal(signal.SIGHUP, sig_hup_handler)
    signal.signal(signal.SIGINT, sig_int_handler)
    session.run_session()

if __name__ == "__main__":
    main()
