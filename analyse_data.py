import json
from datetime import timedelta
from utils import time_str_to_timedelta

# Load JSON data
with open('study_sessions.json', 'r') as file:
    data = json.load(file)

# Calculate total session length
total_session_length = timedelta()
for day in data:
    for session in day["sessions"]:
        total_session_length += time_str_to_timedelta(session["session_length"])

# Print total session length
print("Total hours spent studying physics:", total_session_length)

