import datetime
import json
import os
import random
import re
import signal
import sys
import threading
import time

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
        self.sessions = {}

    def calculate_session_length(self, start, end):
        session_length = end - start
        if(self.break_length_str): 
            session_length -= self.break_length_delt
            for break_str in self.breaks.values():         
                break_time = datetime.timedelta(
                    hours=int(break_str[:2]), 
                    minutes=int(break_str[3:5]),
                    seconds=int(break_str[6:8]),
                )
                session_length -= break_time
        return session_length

    def track_study_session(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.data = json.load(file)

        self.start_time = datetime.datetime.now()
        self.day_number = len(self.data) + 1
        self.start_time_str = self.start_time.strftime("%I:%M:%S %p")

        # so basically, i need to check if another session is started on the same day as the latest entry
        # then i want to add the prompt that if another session is started, will it be part of the same one or a new one
        # if not, just make a new session
        # if so, add to the old session and indicate a break has been taken

        if len(self.data) != 0:
            if self.data[len(self.data) - 1]["date"] == self.start_time.strftime("%Y-%m-%d"):
                continue_response = None
                while (not (continue_response in valid_continue_responses)):
                    continue_response = input("Would you like to continue your previous session? [y/n]  ")
                # put if loop to check multiple sessions or break
                    self.multiple_sessions = True
                    self.day_number = len(self.data)
                    self.start_time = datetime.datetime.now()

        # temporarily removing break functionality for later modification

        # if self.data[len(self.data) - 1]["date"] == self.start_time.strftime(
        #     "%Y-%m-%d"
        # ):
        #     continue_response = None
        #     while(not (continue_response in valid_continue_responses)):
        #         continue_response = input(
        #             "Would You Like To Continue Your Previous Session? [y/n]:  "
        #         )
        #     if continue_response.lower() in ["y", "yes", ""]:
        #         self.curr_session_start_time = datetime.datetime.now() 
        #         self.start_time_str = self.data[len(self.data) - 1]["start_time"]
        #         hour_compensation = 0
        #         if self.start_time_str[9:11] == "PM":
        #             hour_compensation = 12
        #         elif (
        #             self.start_time_str[9:11] == "AM"
        #             and self.start_time_str[0:2] == "12"
        #         ):
        #             hour_compensation = -12
        #         self.start_time = datetime.datetime(
        #             self.start_time.year,
        #             self.start_time.month,
        #             self.start_time.day,
        #             int(self.start_time_str[:2]) + hour_compensation,
        #             int(self.start_time_str[3:5]),
        #             int(self.start_time_str[6:8]),
        #         )
        #         self.day_number = len(self.data)
        #         if self.data[len(self.data) - 1].get("breaks"):
        #             self.breaks = self.data[len(self.data) - 1]["breaks"]
        #         end_time = self.data[len(self.data) - 1]["end_time"]
        #         
        #         dt_endtime = datetime.datetime(
        #             self.start_time.year,
        #             self.start_time.month,
        #             self.start_time.day,
        #             int(end_time[:2]) + hour_compensation,
        #             int(end_time[3:5]),
        #             int(end_time[6:8]),
        #         )
        #         
        #         self.break_length_delt = datetime.datetime.now() - dt_endtime
        #         self.break_length_str = strfdelta(datetime.datetime.now() - dt_endtime)
        #         del self.data[len(self.data) - 1]
        # else: 
        #     # Reset Timer To Not Include Time Spent In Menu 
        #     self.start_time = datetime.datetime.now()

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

                print(
                    f"""
     ╱|、
    (˚ˎ 。7     Session in progress... 
     |、˜〵     Elapsed time: {session_duration_str}
     じしˍ,)ノ
                        """
                )
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

    if TERM_OPEN:
        print(f"Studying Physics Everyday Until I Graduate University | Day {session.day_number}")
        print(f"Session started at: {session.start_time_str}")        
        print(f"Session ended at: {end_time_str}")
        print(f"Session length: {session_length_str}\n")

#     if session.break_length_str:
#         if session.breaks:
#             re_obj = re.compile("break_*")
#             sorted_keys = list(filter(re_obj.match, session.breaks.keys()))
#             sorted_keys.sort(reverse=True)
#             max_break = sorted_keys[0]
#             curr_break = "break_" + str(int(max_break[6:]) + 1)
#         else:
#             curr_break = "break_1"
#         session.breaks[curr_break] = session.break_length_str
#         session_data = {
#             "day": session.day_number,
#             "start_time": session.start_time_str,
#             "breaks": session.breaks,
#             "end_time": end_time_str,
#             "session_length": session_length_str,
#             "date": session.start_time.strftime("%Y-%m-%d"),
#         }
#     else:
#         session_data = {
#             "day": session.day_number,
#             "start_time": session.start_time_str,
#             "end_time": end_time_str,
#             "session_length": session_length_str,
#             "date": session.start_time.strftime("%Y-%m-%d"),
#         }

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

    if TERM_OPEN:
        print(affirmations[random.randint(0, len(affirmations) - 1)])
    
    # TEMPORARY TO MESS AROUND WITH DICT STRUCTURE
    # copy_to_clipboard(session_data)

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
    session.track_study_session()

if __name__ == "__main__":
    main()
