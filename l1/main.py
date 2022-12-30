import time
import warnings
from pywinauto.keyboard import send_keys
from pywinauto.application import Application
warnings.simplefilter('ignore', category=UserWarning)

app = Application().start(cmd_line=r"E:\S HITACHI\4\качество\putty_portable.exe")
time.sleep(5)
app = Application().connect(title="Настройки PuTTY")
window = app.PuTTYConfigBox
window.set_focus()
window[u"Имя Хоста(или IP-адрес): Edit"].type_keys("tty.sdf.org")
window["Соединиться"].click()

app = Application().connect(title="tty.sdf.org - PuTTY")
window = app.top_window()
send_keys("enimaelish{ENTER}RZn3GYVszcPsVA{ENTER}{BACKSPACE}")
