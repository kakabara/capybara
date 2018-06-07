import datetime

def required(message="Field is not presented"):
    def check(field: str, dict_to_check: dict):
        if dict_to_check.get(field) is not None:
            return True, None
        else:
            return False, message
    return check


def is_type(type_object, message="Type doesn't is type field"):
    def check(field: str, dict_to_check: dict):
        value = dict_to_check.get(field)
        if not value:
            return True, None
        if value and isinstance(value, type_object):
            return True, None
        else:
            return False, message
    return check


def str_to_datetime(format_str: str, message="Can convert to date format"):
    def check(field: str, dict_to_check: dict):
        value = dict_to_check.get(field)
        if not value:
            return True, None
        try:
            dt = datetime.datetime.strptime(value, format_str)
            if isinstance(dt, datetime.datetime):
                return True, None
        except ValueError:
            return False, message
    return check
