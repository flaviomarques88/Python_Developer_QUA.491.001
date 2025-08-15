import pyautogui as auto
import time

def main():
    auto.PAUSE = 0.5
    auto.hotkey("win", "r")
    auto.write("cmd")
    auto.press("enter")
    auto.write("cd C:")
    auto.press("enter")
    auto.write("cd Python_Developer_QUA.491.001")
    auto.press("enter")
    auto.write("git add .")
    auto.press("enter")
    auto.write("git config --global user.name flaviomarques88")
    auto.press("enter")
    auto.write("git config --global user.email flaviomarques2012@gmail.com")
    auto.press("enter")
    auto.write("git commit -m Commit do Curso Python Developer do dia 14/08/2025")
    auto.press("enter")
    auto.write("git push")
    auto.press("enter")

if __name__ == "__main__":
    main()