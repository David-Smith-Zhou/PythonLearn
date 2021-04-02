# -*- coding: utf-8 -*-
import inspect
import time


class Util:
    level_verbose = "Verbose"
    level_info = "Info"
    level_debug = "Debug"
    level_warning = "Warning"
    level_error = "Error"

    # def __init__(self):
    @classmethod
    def log_v(cls, msg: str):
        cls.log(cls.level_verbose, msg)

    @classmethod
    def log_i(cls, msg: str):
        cls.log(cls.level_info, msg)

    @classmethod
    def log_d(cls, msg: str):
        cls.log(cls.level_debug, msg)

    @classmethod
    def log_w(cls, msg: str):
        cls.log(cls.level_warning, msg)

    @classmethod
    def log_e(cls, msg: str):
        cls.log(cls.level_error, msg)

    @classmethod
    def log(cls, level: str, msg: str):
        print("[" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "]"
              + "[File:" + inspect.stack()[2].filename
              + "][" + inspect.stack()[2].function + ": " + str(inspect.stack()[2].lineno)
              + "][" + level
              + "]: " + msg)


def main():
    Util.log_v("1")
    Util.log_i("2")
    Util.log_d("3")
    Util.log_w("4")
    Util.log_e("5")


if __name__ == '__main__':
    main()
