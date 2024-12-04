from data import *


def get_beaker_current(load_current):
    breaker_current = 0
    for breaker in current_breakers_low_voltage:
        if breaker > load_current:
            breaker_current = breaker
            break
    if breaker_current != 0:
        return breaker_current
    else:
        raise Exception(
            f"Не найден подходящий автомат."
        )
