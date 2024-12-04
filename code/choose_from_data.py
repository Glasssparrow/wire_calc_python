from .data import *


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


def get_cable_current(breaker_current, material):
    cable_current = 0
    if material == COPPER:
        for cable in copper_low_voltage:
            if cable[ТОК_ОТКРЫТО] >= breaker_current:
                cable_current = cable[ТОК_ОТКРЫТО]
                break
    elif material == ALUMINIUM:
        for cable in aluminium_low_voltage:
            if cable[ТОК_ОТКРЫТО] >= breaker_current:
                cable_current = cable[ТОК_ОТКРЫТО]
                break
    else:
        raise Exception("unexpected incident")
    if cable_current != 0:
        return cable_current
    else:
        raise Exception(
            f"Не найден подходящий автомат."
        )
