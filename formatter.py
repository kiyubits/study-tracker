from datetime import datetime
import json

with open('study_sessions.json', 'r') as file:
    old_data = json.load(file)

# Function to convert time strings to datetime objects
def parse_time(date_str, time_str):
    return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %I:%M:%S %p")

# Function to convert a session into the new format
def convert_to_new_format(old_data):
    new_data = []
    
    for day_data in old_data:
        day = day_data["day"]
        date = day_data["date"]
        start_time = day_data["start_time"]
        end_time = day_data["end_time"]
        session_length = day_data["session_length"]
        
        # Parse session time as datetime objects
        start_datetime = parse_time(date, start_time)
        end_datetime = parse_time(date, end_time)
        
        # Create the new session object
        session = {
            "start_time": start_datetime.strftime("%I:%M:%S %p"),
            "end_time": end_datetime.strftime("%I:%M:%S %p"),
            "session_length": session_length
        }
        
        # Find if the day is already in new_data
        existing_day = next((d for d in new_data if d["day"] == day), None)
        
        if existing_day:
            # Append session to existing day
            existing_day["sessions"].append(session)
        else:
            # Create a new day entry
            new_data.append({
                "day": day,
                "date": date,
                "sessions": [session]
            })
    
    return new_data

# Convert old format data to new format
new_data = convert_to_new_format(old_data)

# Output the new data

with open('new_data.json', 'w') as f:
    json.dump(new_data, f, indent = 4)

