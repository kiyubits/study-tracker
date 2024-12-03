import json
from datetime import timedelta
from utils import time_str_to_timedelta

# Load JSON data
with open('study_sessions.json', 'r') as file:
    study_data = json.load(file)

# Calculate total session length
total_study_session_length = timedelta()
for day in study_data:
    for session in day["sessions"]:
        total_study_session_length += time_str_to_timedelta(session["session_length"])

# Print total session length
print("Total hours spent studying physics:", total_study_session_length)

# Load JSON data
with open('coding_sessions.json', 'r') as file:
    code_data = json.load(file)

# Calculate total session length
total_code_session_length = timedelta()
for day in code_data:
    for session in day["sessions"]:
        total_code_session_length += time_str_to_timedelta(session["session_length"])

# Print total session length
print("Total hours spent coding:", total_code_session_length)
