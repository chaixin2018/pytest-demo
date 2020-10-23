"""
------------------------------------
@Time :
@Auth :
@File : keyboard.py
@IDE  : PyCharm
@Motto:
------------------------------------
"""

# 模拟按键
import win32api
import win32con
import time


class KeyBoard(object):
    """模拟按键"""
    # 键盘码
    vk_code = {
        'enter': 0x0D,
        'tab': 0x09,
        'ctrl': 0x11,
        'v': 0x56,
        'a': 0x41,
        'x': 0x58
    }
    @staticmethod
    def key_down(key_name):
        """按下键"""
        key_name = key_name.lower()
        try:
            win32api.keybd_event(KeyBoard.vk_code[key_name], 0, 0, 0)
        except Exception as e:
            print('未正确的按下{}键'.format(key_name))
            print(e)

if __name__ == '__main__':
    keyBoard = KeyBoard
    keyBoard.key_down("f")
