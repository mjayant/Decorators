import collections

class MemorizedDecorator(object):
    """

    """
    def __init__(self, func):
        """

        """
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        """

        :param args:
        :param kwargs:
        :return:
        """
        if not isinstance(args, collections.Hashable):
            return self.func(*args) # because we can't save unhashabe or unmutable object as key to cache
        elif args in self.cache:
            return self.cache['args']
        else:
            self.cache['args'] = self.func(*args)
            return self.cache['args']


    def __str__(self):
        return self.func.__doc__

