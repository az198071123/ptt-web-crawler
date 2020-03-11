import sys


def get_cur_info():
    # print(sys._getframe().f_code.f_lineno)
    print(sys._getframe().f_back.f_lineno)

    # print(sys._getframe().f_back.f_code.co_code)


get_cur_info()
