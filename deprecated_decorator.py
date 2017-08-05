from functools import wraps

import warnings
import inspect


def deprecated(func):
    """

    :param func: Wrapped function
    :return: Decorate function
    """

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        """

        :param args: non key args
        :param kwargs: key words args
        :return:
        """
        #import pdb ;pdb.set_trace()
        callerframerecord = inspect.stack()[1]  # 0 represents this line
        # 1 represents line at caller
        frame = callerframerecord[0]
        info = inspect.getframeinfo(frame)
        print("************************Inside Decorator************************************")
        warnings.warn_explicit(message='Function {} is deprecated . '.format(func.__name__),
                               category=DeprecationWarning, filename=info.filename,
                               lineno=info.lineno)
        return func(*args, **kwargs)

    return wrapped_func

@deprecated
def test_function():
    print("We are inside testing function")

test_function()