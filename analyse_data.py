import json
from datetime import timedelta
from utils import time_str_to_timedelta
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import mplcyberpunk

# Load JSON data
with open('study_sessions.json', 'r') as file:
    study_data = json.load(file)

df = pd.DataFrame(study_data)

# Calculate total session length
total_study_session_length = timedelta()
for day in study_data:
    for session in day["sessions"]:
        total_study_session_length += time_str_to_timedelta(session["session_length"])

# Print total session length
print("Total hours spent studying:", total_study_session_length)

# Get total length of sessions per day
def get_total_session_length(row):
    total = timedelta()
    for session in row['sessions']:
        total += time_str_to_timedelta(session['session_length'])
    return float(total.total_seconds() / 3600)

df['total_session_length'] = df.apply(get_total_session_length, axis=1)
df['cumulative_session_length'] = df['total_session_length'].cumsum()

print(df[['day', 'total_session_length']])

plt.style.use("cyberpunk")
plt.rcParams["font.family"] = "serif"
fig, axes = plt.subplots(nrows = 2, ncols=1)

df.plot(ax=axes[0], legend=False, x='day', y='total_session_length', title='session hours per day', ylabel='hours')
df.plot(ax=axes[1], legend=False, x='day', y='cumulative_session_length', title='cumulative session hours', ylabel='hours')

mplcyberpunk.add_glow_effects(ax=axes[0])
mplcyberpunk.add_glow_effects(ax=axes[1])

plt.show()

# plot = df[['day', 'total_session_length']].plot("Studying Physics Everyday Until I Graduate University")
