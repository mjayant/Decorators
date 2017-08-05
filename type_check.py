"""
Following are logging stage , please give one of them:
0 -- NONE:   No type-checking. Decorators disabled.
1 -- MEDIUM: Print warning message to stderr. (Default)
2 -- STRONG: Raise TypeError with message.

If 'debug' is not passed to the decorator, the default level is used.

Example usage:

>>> NONE, MEDIUM, STRONG = 0, 1, 2
>>> @accepts(int, int, int)
... @returns(float)
... def average(x, y, z):
...     return (x + y + z) / 2
...
>>> average(5.5, 10, 15.0)
TypeWarning:  'average' method accepts (int, int, int), but was given
(float, int, float)
>>> average(5, 10, 15)
TypeWarning:  'average' method returns (float), but result is (int)
>>> TYPE_CHECK = STRONG
>>> @accepts(int, debug=TYPE_CHECK)
... @returns(int, debug=TYPE_CHECK)
... def test(n):
...     print n
...
>>> test(5.3)
Traceback (most recent call last):
...
TypeError: 'fib' method accepts (int), but was given (float)


"""

from functools import wraps

def info(fun_name, func_arg_type, expected_types, check_retrun_type=0):
    """

    :param fun_name:
    :param func_arg_type:
    :param expected_types:
    :return:
    """
    msg = ''
    #fun_args_type = [item[1] for item in func_arg_type]
    #import pdb ;pdb.set_trace()
    #expected_types = list(expected_types)
    flag = False
    # import pdb;
    # pdb.set_trace()
    # formatted_expec_type_list = [str(item).split(' ')[1].replace('>', '') for item in expected_types]
    # formatted_fun_arg_type_list = [str(item).split(' ')[1].replace('>', '') for item in func_arg_type]
    if func_arg_type != expected_types:
        flag = True
        if check_retrun_type:
            msg = fun_name + ' return ' + str(expected_types) + 'but in this case its returning ' + str(
                func_arg_type)
        else:
            msg = fun_name + ' was expecting'+ str(expected_types) + 'but it got ' + str(func_arg_type)

        return (flag, msg)

    return (flag, msg)


def accepts(*args, **kw):
    """
    It check all param of function are expected type or not
    :param args: type which is expected in function
    :param kw: debug level
    :return:
    """
    try:
        if not kw['debug']:
            debug = 1
        else:
            debug = kw['debug']

        def wrap_fucntion(func):
            """

            :param func:
            :return:
            """
            @wraps(func)
            def main_decorator(*arg, **kwargs):
                args_types = tuple(map(type, arg))
                flag, msg = info(func.__name__, args_types, args)
                if debug == 0:
                    func(*arg, **kwargs)
                elif debug == 1 and flag:
                    print('TypeWarning:'+msg)
                elif debug == 2 and flag:
                    raise TypeError(msg)

                return(func(*arg, **kwargs))

            return main_decorator
    except KeyError as key:
        raise KeyError (str(key) + "is not a valid keyword argument")

    return wrap_fucntion



def check_retrun_type(retrun_type, **kw):
    """
    It check all param of function are expected type or not
    :param args: type which is expected in function
    :param kw: debug level
    :return:
    """
    try:
        if not kw['debug']:
            debug = 1
        else:
            debug = kw['debug']

        def wrap_fucntion(func):
            """

            :param func:
            :return:
            """
            @wraps(func)
            def main_decorator(*arg, **kwargs):
                #args_types = list(map(type, arg))
                retrun_val = func(*arg, **kwargs)
                retrun_val_type = type(retrun_val)
                flag, msg = info(func.__name__, retrun_val_type, retrun_type, check_retrun_type=1)
                if debug == 0:
                    retrun_val
                elif debug == 1 and flag:
                    print('TypeWarning:'+msg)
                elif debug == 2 and flag:
                    raise TypeError(msg)

                return retrun_val

            return main_decorator
    except KeyError as key:
        raise KeyError (str(key) + "is not a valid keyword argument")

    return wrap_fucntion



@accepts(int, int, int, debug=2)
@check_retrun_type(int, debug=2)
def average(x, y, z):
    return (x + y + z) / 2

print(average(1, 2, 3))