import time
contacts = ['Yan', 'Aung', 'Hein']


def sms_decorator(func):
    def inner(contacts):
        for contact in contacts:
            print(f'Send SMS to {contact}')
        func(contacts)
    return inner


def facebook_decorator(func):
    def inner(contacts):
        for contact in contacts:
            print(f'Send Facebook to {contact}')
        func(contacts)
    return inner


@sms_decorator
@facebook_decorator
def send_noti(contacts):
    for contact in contacts:
        print(f'Send Notification to {contact}')


# send_noti(contacts)


def timethis(func):
    def inner(*args, **kwargs):
        print(func.__name__, end=" ... ")

        start_time = time.time()
        result = func(*args, **kwargs)
        elapse_time = time.time() - start_time

        print(elapse_time)
        return result
    return inner


@timethis
def factorial(number):
    result = 1
    for index in range(number):
        result *= index + 1
    print(result)


factorial(3)
