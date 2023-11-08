# Decorator Exercise
user1 = {
    'name': 'ABCD',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper_func(*args, **kargs):
        if args[0]['valid']:
            return fn(*args, **kargs)
    return wrapper_func


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
