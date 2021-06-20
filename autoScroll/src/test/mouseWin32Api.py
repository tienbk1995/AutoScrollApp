import win32api, time
#Button key

LEFTMOUSE = 0x01
RIGHTMOUSE = 0x02
SCROLLMOUSE = 0x04
BACKSPACE = 0x08
TABSPACE = 0x09
ENTERKEY = 0x0D
VK_CANCEL = 0x03

while 1:
    print (win32api.GetKeyState(VK_CANCEL))
    time.sleep(2)