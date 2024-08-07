import datetime
import json
import os
import random
import signal
import sys
import threading
import time

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


TERM_OPEN = True


class StudySession:
    def __init__(self, filename):
        self.filename = "study_sessions.json"
        self.data = []
        self.halt = False
        self.day_number = 0
        self.start_time_str = None
        self.self_time = 0
        self.progress_thread = None

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

        def display_session_progress():
            while not self.halt:
                # Clear the screen
                os.system("clear")

                # Calculate the current session duration
                current_time = datetime.datetime.now()
                session_duration = current_time - self.start_time
                hours, remainder = divmod(session_duration.total_seconds(), 3600)
                minutes, seconds = divmod(remainder, 60)
                session_duration_str = (
                    f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
                )

                print(
                    f"""
     ╱|、
    (˚ˎ 。7     Session in progress... {self.day_number} 
     |、˜〵     Elapsed time: {session_duration_str}
     じしˍ,)ノ
                        """
                )
                time.sleep(1)

        self.progress_thread = threading.Thread(target=display_session_progress)
        # progress_thread.daemon = True
        self.progress_thread.start()

        input()
        self.halt = True
        progress_thread.join()
        processEnd(self)


def processEnd(session: StudySession):
    global TERM_OPEN
    if TERM_OPEN:
        print(
            f"Studying Physics Everyday Until I Graduate University | Day {session.day_number}"
        )
        print(f"Session started at: {session.start_time_str}")

    end_time = datetime.datetime.now()
    end_time_str = end_time.strftime("%I:%M:%S %p")
    if TERM_OPEN:
        print(f"Session ended at: {end_time_str}")

    session_length = session.calculate_session_length(session.start_time, end_time)

    hours, remainder = divmod(session_length.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    session_length_str = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    if TERM_OPEN:
        print(f"Session length: {session_length_str}\n")

    session_data = {
        "day": session.day_number,
        "start_time": session.start_time_str,
        "end_time": end_time_str,
        "session_length": session_length_str,
        "date": session.start_time.strftime("%Y-%m-%d"),
    }

    session.data.append(session_data)

    with open(session.filename, "w") as file:
        json.dump(session.data, file, indent=4)

    if TERM_OPEN:
        print(affirmations[random.randint(0, len(affirmations) - 1)])



def main():

    session = StudySession("study_sessions.json")

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
