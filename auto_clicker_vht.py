import time
import threading
from pynput.mouse import Listener as MouseListener, Button, Controller
from pynput.keyboard import Listener as KeyListener, KeyCode, Key

#### For fixing incorrect mouse coordinates in Windows 10 ####
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)
##############################################################

delay = 0.2
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')
default_mode = "Key.f1"
modes = {
    "Key.f1": [[1361, 759], [1185, 738]],
    "Key.f2": [[404, 541], [541, 847]],
    "Key.f3": [[1049, 649]],
    "Key.f4": [],
    "Key.f5": [],
    "Key.f6": [],
    "Key.f8": [],
    "Key.f9": [],
    "Key.f10": [],
    "Key.f11": [],
    "Key.f12": [],
    "c": [],
}
# Modes
# F1 - Xai luc chien
# F2 - Lag chien bao
# F3 - Boss cong hoi
# c - Custom mode


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.recording = False
        self.running = False
        self.program_running = True
        self.index = 0
        self.numOfCoordinates = 0
        self.mode = default_mode
        print('Mode {0} selected by default'.format(default_mode))

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def start_recording(self):
        print("Recording mouse's coordinates")
        self.recording = True

    def stop_recording(self):
        if self.recording == True:
            print("Stopped recording mouse's coordinates")
        self.recording = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def set_mode(self, mode):
        self.mode = mode

    def run(self):
        while self.program_running:
            self.index = 0
            self.numOfCoordinates = len(modes[self.mode])
            while self.running:
                if self.numOfCoordinates > 0:
                    mouse.position = (
                        modes[self.mode][self.index][0], modes[self.mode][self.index][1])
                    mouse.click(self.button)
                    self.index = self.index + 1
                    if self.index == self.numOfCoordinates:
                        self.index = 0
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.stop_recording()
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
        mouseListener.stop()
    elif key == KeyCode(char='r'):
        if click_thread.recording:
            click_thread.stop_recording()
        elif click_thread.running == False:
            modes['c'].clear()
            click_thread.start_recording()
    elif key == Key.f1 or key == Key.f2 or key == Key.f3 or key == Key.f4 or key == Key.f5 or key == Key.f6 or key == Key.f8 or key == Key.f9 or key == Key.f10 or key == Key.f11 or key == Key.f12:
        # Key.f7 is not used since it already has a function assigned in Firefox
        click_thread.stop_clicking()
        click_thread.stop_recording()
        print('Mode {0} selected'.format(key))
        click_thread.set_mode(format(key))
    elif key == KeyCode(char='c'):
        click_thread.stop_recording()
        click_thread.stop_clicking()
        print('Mode {0} selected'.format(key.char))
        click_thread.set_mode(format(key.char))


def on_click(x, y, button, pressed):
    if click_thread.recording and not pressed:
        print('Added a new coordinate at {0}'.format((x, y)))
        modes['c'].append([x, y])


mouseListener = MouseListener(on_click=on_click)
mouseListener.start()


with KeyListener(on_press=on_press) as listener:
    listener.join()
