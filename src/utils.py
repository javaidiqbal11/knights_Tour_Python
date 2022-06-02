import platform
from screeninfo import screeninfo as _screeninfo


def center_tkinter_windows(win):
    win.update_idletasks()

    if platform.system() == 'Windows':
        import ctypes
        from screeninfo import Enumerator
        ctypes.windll.user32.SetProcessDPIAware()
        monitors = _screeninfo.get_monitors(Enumerator.Cygwin)
    else:
        monitors = _screeninfo.get_monitors()

    current_monitor = monitors[0]

    for m in reversed(monitors):
        if m.x <= win.winfo_x() <= m.width + m.x and m.y <= win.winfo_y() <= m.height + m.y:
            current_monitor = m

    screen_width = current_monitor.width
    screen_height = current_monitor.height
    width = win.winfo_width()
    height = win.winfo_height()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
