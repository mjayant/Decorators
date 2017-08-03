from functools import wraps
import json

def json_validator(expected_args):
    """

    :param expected_args:
    :return:
    """
    def wrapped_func(func):
        """

        :param func:
        :return:
        """
        @wraps(func)
        def main_decorators(json_str, student_id):
            """

            :param json_str:
            :return:
            """
            json_data = json.loads(json_str)
            dict_keys = json_data.keys()
            for item in expected_args:
                if item not in dict_keys:
                    print("%s not found in database" %item)
                    return False
            else:
                return func(json_str, student_id)

        return main_decorators

    return wrapped_func

expected_args = ['marks', 'Age', 'Name']


@json_validator(expected_args)
def update_grade(json_str, student_id):
    """
    Upgrade json object for student id and sava into data base

    :param json_str:
    :return:
    """
    pass