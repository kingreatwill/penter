"""
# https://docs.python.org/zh-cn/3/library/windows.html
msilib  安装文件相关
msvcrt  MS VC++ runtime 相关
winreg 注册表相关
winsound  声音播放接口
"""

import winsound
# Play Windows exit sound.
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

# Probably play Windows default sound, if any is registered (because
# "*" probably isn't the registered name of any sound).
winsound.PlaySound("*", winsound.SND_ALIAS)