import subprocess
from shutil import which

CLIPBOARD = ""


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


def copy_to_clipboard(text: str):
    """Copies to the first found clipboard."""
    if CLIPBOARD == "wl-clipboard":
        subprocess.Popen(["wl-copy", text], stdout=subprocess.PIPE)
    elif CLIPBOARD == "xclip":
        proc = subprocess.Popen(["xclip", "-sel", "clip"], stdin=subprocess.PIPE)
        proc.communicate(input=bytes(text, "utf-8"))
    else:
        proc = subprocess.Popen(["xsel", "-b"], stdin=subprocess.PIPE)
        proc.communicate(input=bytes(text, "utf-8"))


if __name__ == "__main__":
    find_clipboard()
    copy_to_clipboard("clipboard test")
