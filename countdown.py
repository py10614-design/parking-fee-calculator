import time

countdown_value = 10


def start_countdown():
    global countdown_value
    countdown_value = 10

    while countdown_value > 0:
        time.sleep(1)
        countdown_value -= 1


def get_countdown():
    return countdown_value


def reset_countdown():
    global countdown_value
    countdown_value = 10


def tick_countdown():
    global countdown_value
    if countdown_value > 0:
        countdown_value -= 1


def decrease_turn():
    global countdown_value
    if countdown_value > 0:
        countdown_value -= 1
    else:
        countdown_value = 0


def set_turn_count(value):
    global countdown_value
    countdown_value = value