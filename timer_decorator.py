import datetime

def timing_decorator(func):
    """

    :param func:
    :return:
    """
    def get_execution_time():
        """

        :return:
        """
        start_time = datetime.datetime.now()
        print(start_time)
        func()
        end_time = datetime.datetime.now()
        print(end_time)
        return "Execution Time : "+ str(end_time - start_time)

    return get_execution_time

@timing_decorator
def testFunction():
    for item in range(0, 100):
        print(item)

res = testFunction()

print(res)