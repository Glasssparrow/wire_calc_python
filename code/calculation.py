from .choose_from_data import *


def calculate_load_current(
        P, U, cos_fi, L,
        phases, load_type,
        cable_type,
):
    if phases == 3:
        load_current = (P*1000)/((3**0.5)*cos_fi*U)
    elif phases == 1:
        load_current = (P*1000)/(cos_fi*U)
    else:
        raise Exception(f"Unexpected incident")
    return load_current

def calculate_breaker_current(
        P, U, cos_fi, L,
        phases, load_type,
        cable_type,
):
    load_current = calculate_load_current(
        P, U, cos_fi, L,
        phases, load_type,
        cable_type,
    )
    breaker_current = get_beaker_current(load_current)
    return breaker_current

def calculate_max_cable_current(
        P, U, cos_fi, L,
        phases, load_type,
        cable_type,
):
    breaker_current = calculate_breaker_current(
        P, U, cos_fi, L,
        phases, load_type,
        cable_type,
    )
    cable_current = get_cable_current(breaker_current, cable_type)
    return cable_current

def calculate_cable_area(
        P, U, cos_fi, L,
        phases, load_type,
        cable_type,
):
    cable_current = calculate_max_cable_current(
        P, U, cos_fi, L,
        phases, load_type,
        cable_type,
    )
    cable_area = get_cable_area(cable_current, cable_type)
    return cable_area

def calculate_load_u(
        P, U, cos_fi, L,
        phases, load_type,
        cable_type,
):
    return "load_u"
