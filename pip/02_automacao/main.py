import pyautogui as auto
import time

def main():
    auto.PAUSE = 0.5
    auto.press("win")
    auto.write("edge")
    auto.press("enter")
    auto.hotkey("alt", "space")
    auto.press("x")
    auto.write("github.com")
    auto.press("enter")
  
    auto.write("Flávio é o Cara do Python KKKK, Aula de Automação com Python.")

if __name__ == "__main__":
    main()