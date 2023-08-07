
import time
import webbrowser
import pip
time.sleep(1)

def install(package):
    if hasattr(pip, 'main'):
            pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

try:
    import pyautogui
except ModuleNotFoundError:
    install('pyautogui')
time.sleep(5)
#pyautogui.moveTo(1890, 20, duration = 1)

try:
    import pyautogui
    chrome_path = "C://Program Files (x86)//Google//Chrome//Application//Chrome.exe %s"
    #webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get(chrome_path).open("www.youtube.com", new = 0)
    time.sleep(10)
    pyautogui.moveTo(800, 125, duration=1)
    pyautogui.click()
    pyautogui.hotkey("ctrlleft", "a")
    pyautogui.typewrite(["Backspace"])
    typewrite = pyautogui.typewrite("CrowdStrike")
    pyautogui.typewrite(["Enter"])
    time.sleep(5)
    pyautogui.moveTo(800, 600, duration=1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.typewrite('f')
    #for i in range(100):
        #pyautogui.press("volumeup")
    pyautogui.press("volumedown")
except webbrowser.Error as e:
    print(e)

