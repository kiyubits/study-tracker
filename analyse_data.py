import json
from datetime import datetime, timedelta

# Load JSON data
with open('study_sessions.json', 'r') as file:
    data = json.load(file)

# Function to convert time string to timedelta
def time_str_to_timedelta(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return timedelta(hours=hours, minutes=minutes, seconds=seconds)

# Calculate total session length
total_session_length = timedelta()
for session in data:
    total_session_length += time_str_to_timedelta(session['session_length'])

# Print total session length
print("Total hours spent studying physics:", total_session_length)

