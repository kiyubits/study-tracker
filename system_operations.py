import subprocess
from shutil import which
import os

CLIPBOARD = ""

# if os.name == 'nt':
#    CLIPBOARD = "clip"

def find_clipboard():
    """Uses loginctl to obtain the top most user's session number
    and finds the currently used protocol from it"""
    global CLIPBOARD
    user_id = (
        subprocess.Popen("loginctl", stdout=subprocess.PIPE)
        .communicate()[0]
        .decode("utf-8")
    )

    stripped_id = user_id.partition("\n")[2].split()[0]
    cmd = ["loginctl", "show-session", stripped_id, "-p", "Type"]

    protocol = (
        subprocess.Popen(cmd, stdout=subprocess.PIPE)
        .communicate()[0]
        .decode("utf-8")
        .replace("\n", "")
    )
    if protocol == "Type=wayland":
        CLIPBOARD = "wl-clipboard"
    elif which("xsel"):
        CLIPBOARD = "xsel"
    else:
        CLIPBOARD = "xclip"


def copy_to_clipboard(input: dict):
    """Formats and copies to the first found clipboard."""
#     if('breaks' in input.keys()): 
#         breaks_list = [f'{key}: {value}\n' for key, value in input["breaks"].items()]
#         break_strings = ''.join(str(string) for string in breaks_list)
#     else:
#         break_strings = ''
    
    formatted_text = f"Studying Everyday Until I Graduate University | Day {input['day']}\n"

    for i, session in enumerate(input["sessions"], start = 1):
        formatted_text += f"Session {i}: {session['start_time']} - {session['end_time']} ({session['session_length']})\n"

    formatted_text += f"Total time spent studying today: {input['total_time']}"

    if CLIPBOARD == "wl-clipboard":
        subprocess.Popen(["wl-copy", formatted_text], stdout=subprocess.PIPE)
    elif CLIPBOARD == "xclip":
        proc = subprocess.Popen(["xclip", "-sel", "clip"], stdin=subprocess.PIPE)
        proc.communicate(input=bytes(formatted_text, "utf-8"))
    else:
        proc = subprocess.Popen(["xsel", "-b"], stdin=subprocess.PIPE)
        proc.communicate(input=bytes(formatted_text, "utf-8"))

