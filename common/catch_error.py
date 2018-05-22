import traceback

"""
def run_with_ignorance(*funcs):
    for f in funcs:
        try:
            f()
            print('\033[1;32m' + f.__name__ + '-----success!!!' + '\033[0m')
        except Exception as ex:
            print(f.__name__ + '---error:', ex)
        #except Exception:
            #traceback.print_exc()
run_with_ignorance(start_working1,stw_selct_all,working)

def catch_error(func):
    def inner_wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            print('\033[1;32m' + func.__name__+'-----success!!!'+ '\033[0m')
        except Exception as e:
            print(func.__name__+'---error:', e)
        return res
    return inner_wrapper
"""

#装饰器处理异常
def catch_error(func):
    def wrapped():
        try:
            func()
            print('\033[1;32m' + func.__name__ + '-----success!!!' + '\033[0m')
        except Exception as ex:
            print(func.__name__ + '---error:',ex)
        #可要可不要
        return func
    return wrapped