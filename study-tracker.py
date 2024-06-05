import datetime
import json
import os
import threading
import time
import random

def calculate_session_length(start, end):
    session_length = end - start
    return session_length

def track_study_session():
    start_time = datetime.datetime.now()
    day_number = datetime.date.today() - datetime.date(2024, 5, 13) 
    start_time_str = start_time.strftime('%I:%M:%S %p')

    def display_session_progress():
        while True:
            # Clear the screen
            os.system('clear')

            # Calculate the current session duration
            current_time = datetime.datetime.now()
            session_duration = current_time - start_time
            hours, remainder = divmod(session_duration.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            session_duration_str = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

            print(f"""
 ╱|、
(˚ˎ 。7     Session in progress... 
 |、˜〵     Elapsed time: {session_duration_str}
 じしˍ,)ノ
                    """)
            time.sleep(1)  

    progress_thread = threading.Thread(target=display_session_progress)
    progress_thread.daemon = True  
    progress_thread.start()

    input()

    affirmations = [
        "You did really well today!",
        "Good job today :)",
        "Keep going, you're improving everyday!",
        "I hope you had a good session hehe",
        "You are filled with determination.",
        "Well done! You deserved this.",
        "やった！",
        "Study hard what interests you the most in the most undisciplined, irreverent and original manner possible.",
        "The first principle is that you must not fool yourself and you are the easiest person to fool."
    ]

    print(f"Doing Physics Everyday Until I Graduate University | Day {day_number.days}")
    print(f"Session started at: {start_time_str}")
    end_time = datetime.datetime.now()
    end_time_str = end_time.strftime('%I:%M:%S %p')
    print(f"Session ended at: {end_time_str}")

    session_length = calculate_session_length(start_time, end_time)

    hours, remainder = divmod(session_length.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    session_length_str = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    print(f"Session length: {session_length_str}\n")

    session_data = {
        "day": day_number.days,
        "start_time": start_time_str,
        "end_time": end_time_str,
        "session_length": session_length_str,
        "date": start_time.strftime('%Y-%m-%d')
    }

    file_name = 'study_sessions.json'

    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
    else:
        data = []

    data.append(session_data)

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

    print(affirmations[random.randint(0, len(affirmations) - 1)])

if __name__ == "__main__":
    track_study_session()

