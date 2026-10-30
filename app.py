import os
import socket
import subprocess


def _fix_xauth():
    home = os.path.expanduser("~")
    src = os.environ.get("XAUTHORITY", os.path.join(home, ".Xauthority"))
    dst = os.path.join(home, ".Xauthority")
    try:
        out = subprocess.run(
            ["xauth", "-f", src, "list"], capture_output=True, text=True
        ).stdout
        cookie = None
        for line in out.splitlines():
            parts = line.split()
            if len(parts) >= 3 and parts[1] == "MIT-MAGIC-COOKIE-1":
                cookie = parts[2]
                break
        if cookie:
            host = socket.gethostname()
            for name in (host + "/unix:0", host + ":0"):
                subprocess.run(
                    ["xauth", "-f", dst, "add", name, "MIT-MAGIC-COOKIE-1", cookie],
                    capture_output=True,
                )
            os.environ["XAUTHORITY"] = dst
    except Exception:
        pass


_fix_xauth()

import pyautogui
import time

time.sleep(5)
for i in range(100):
    pyautogui.write("ooooooooooooooooooooo") 
    pyautogui.press("enter")
    time.sleep(0.01)
