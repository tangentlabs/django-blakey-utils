def parse_int(value, default = -1):
    """
    :param value: value which needs to be parsed to int
    :type value: unicode
    :param default: returned if param value is not valid int representation
    :type default: int
    :return: parsed int if value is valid int representation, otherwise default
    :rtype: int
    """
    try:
        result = int(value)
    except ValueError:
        result = default
    return result
