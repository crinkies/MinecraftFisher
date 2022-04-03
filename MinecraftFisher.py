import pyautogui
import threading
import keyboard
import time
import os
'''
License:MIT
Author:github.com/crinkies
'''
quitFishing = False
running = False
fish = 0
new_line = "#"*50+"\n"
w1,h1 = pyautogui.size()
w2=round(w1//1.5)#1.5-2
h2=round(h1//1.5)

def main():
    os.system('mode 50, 12')
    new_thread(hotkeys)
    print(f"{new_line}"
          "#        Minecraft Fisher (Java Version)         #\n"
          "#              Turn subtitles on                 #\n"
          "#   Options > Music & Sounds > Show Subtitles    #\n"
          "#                                                #")
    body()

    
def body():
    print(f"{new_line}"
    "    Hold Ctrl-'Z' to start, Ctrl-'X' to stop.\n"
    f"{new_line}")

def new_thread(threads):
    x = threading.Thread(target=threads)
    x.start()
    
def click(x,y):
    global fish
    fish+=1
    pyautogui.click(button='right')
    time.sleep(.5)
    pyautogui.click(button='right')
    os.system('cls')
    body()
    print(f"> Detected: ({x}, {y})\n> Caught fish: {fish}")

    
def fisher():
    global running
    running = True
    while not quitFishing:
        if quitFishing:
            break
        try:
            x, y = pyautogui.locateCenterOnScreen('images\\bobber1.png', region=(w2,h2,w1,h1), confidence=0.8)
            click(x,y)
            time.sleep(3)
        except:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('images\\bobber2.png', region=(w2,h2,w1,h1), confidence=0.8)
            click(x,y)
            time.sleep(3)
        except:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('images\\bobber3.png', region=(w2,h2,w1,h1), confidence=0.8)
            click(x,y)
            time.sleep(3)
        except:
            pass
        finally:
            os.system('cls')
            body()
            print("> No detection")
            time.sleep(1)
                

def hotkeys():
    while not quitFishing:
        if quitFishing:
            break
        time.sleep(.3)
        if keyboard.is_pressed('ctrl+z'):
            global running
            if running == False:
                print("> Starting...\n")
                time.sleep(1)
                os.system('cls')
                os.system('mode 50, 8')
                body()
                pyautogui.click(button='right')
                new_thread(fisher)
            else:
                os.system('cls')
                body()
                print("> Already running")
                time.sleep(1)
                pass
            while keyboard.is_pressed('ctrl+z'):
                pass
        elif keyboard.is_pressed('ctrl+x'):
            exit_app()
            while keyboard.is_pressed('ctrl+x'):
                pass
        else:
            pass
    
def exit_app():
    global quitFishing
    quitFishing = True
    time.sleep(3)
    os.system('cls')
    os.system('mode 50, 12')
    print(f"{new_line}"
    "#                                                #"
    "#                   Goodbye                      #"
    "#                                                #"
    f"\n{new_line}"
    f"          You caught a total of {fish} fish"
    f"\n{new_line}")
    raise SystemExit

main()
