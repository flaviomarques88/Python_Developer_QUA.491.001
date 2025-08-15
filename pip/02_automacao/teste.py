import pyautogui as auto
import time

def main():
    auto.PAUSE = 0.5
    auto.hotkey("win", "r")
    auto.write("powershell")
    auto.press("enter")
    auto.write("ping google.com.br -t ")
    auto.press("enter")

    
 
 


if __name__ == "__main__":
    main()