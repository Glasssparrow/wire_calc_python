

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

def calculate_max_cable_current(
        P, U, cos_fi, L,
        phases, load_type,
        cable_type,
):
    return "max_cable_current"

def calculate_cable_area(
        P, U, cos_fi, L,
        phases, load_type,
        cable_type,
):
    return "cable_area"

def calculate_breaker_current(
        P, U, cos_fi, L,
        phases, load_type,
        cable_type,
):
    return "breaker_current"

def calculate_load_u(
        P, U, cos_fi, L,
        phases, load_type,
        cable_type,
):
    return "load_u"