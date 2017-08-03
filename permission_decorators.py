from functools import wraps



def is_allowed(permission):
    """

    :param permission: Permisson which is required for execution wrapped function

    :return:
    """

    def wrapped_func(func):
        """

        :param func: wrapped function
        :return:
        """
        @wraps(func)
        def main_decorators(*args, **kwargs):
            """

            :param user_id: user id
            :return:
            """
            user_id = kwargs['current_user_id']
            user_permission = getUserPermission(user_id)
            if user_permission in permission:
                return func(*args, **kwargs)
            else:
                print("user is not allowed for this action")
                return False

        return main_decorators

    return wrapped_func

def getUserPermission(user_id):
    """

    :param user_id:
    :return:
    """

    return ['Admin']

@is_allowed(['Admin'])
def deleteUser(delete_user_id, current_user_id=1):
    """
    delete the user with the given Id. This function is only accessible to users with administrator permissions
    :param current_user_id:
    :return:
    """
    pass