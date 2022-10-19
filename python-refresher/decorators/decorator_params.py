import functools
user = {'username': 'yogi', 'access_level': 'user'}


# def secure_admin_password():
#     if user['access_level'] == 'admin':
#         return '1234'

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return 'No admin permission for {}.'.format(user['username'])

    return secure_function


@make_secure
def get_password(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return 'Super secured'


print(get_password('billing'))


# example 2
def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                return 'No {} permission for {}.'.format(access_level, user['username'])

        return secure_function
    return decorator


@make_secure('admin')
def get_admin_password():
    return '1234'


@make_secure('user')
def get_dashboard_password():
    return 'user:user_password'


print(get_admin_password())

print(get_dashboard_password())
