
platform = 'Unknown'

try:
    import ctypes.windll as windll
    platform = 'Windows'
except ImportError:
    try:
        from appscript import *
        platform = 'Mac OS X'
    except ImportError:
        try:
            import gconf
            platform = 'gconf'
        except ImportError:
            print('Unknown platform')


def set_background_image(image):
    if platform == 'Windows':
        windll.user32.SystemParametersInfoW(0x14, 0, image, 0x2)
    elif platform == 'Mac OS X':
        app('System Events').desktops.picture.set(image)
    elif platform == 'gconf':
        conf = gconf.client_get_default()
        conf.set_string('/desktop/gnome/background/picture_filename', image)
    else:
        print('Unknown platform')