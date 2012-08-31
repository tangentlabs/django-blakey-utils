def get_matched_string(match):
    """
    :return: string portion which matched specified match (not the initial search string which is represented by match.string)
    """
    return match.string[match.start():match.end()]
def remove_group_from_match(match, group):
    """
    :return: string portion which matched specified match without text portion matched by the specified group
    """
    return "%s%s" % (match.string[match.start():match.start(group)], match.string[match.end(group):match.end()])

def replace_groups_in_match(match, group_values):
    """
    :param group_values: a list-like object of tuples (group_name, str_value_with_which_group_has_to_be_replaced)
    :return: string portion which matched specified match, but with text portions which matched group_names from parameter group_values replaced by values_with_which_groups_have_to_be_replaced from group_values.
    """
    result = get_matched_string(match)
    group_names_to_replace = [group_name for group_name, value in group_values]
    # spans identifying coordinates of groups from group_values in matched string (they need to be shifted to start of the match)
    spans_to_replace = [(match.start(group_name) - match.start(), match.end(group_name) - match.start()) for group_name in group_names_to_replace]
    spans_to_replace_w_values = [(spans_to_replace[i], group_values[i]) for i in range(len(group_values))]
    sorted_spans_with_group_values = sorted(spans_to_replace_w_values, key=lambda span_and_value: span_and_value[0], reverse=True)
    for span, (group, value) in sorted_spans_with_group_values:
        prefix = result[:span[0]]
        postfix = result[span[1]:]
        result = "%s%s%s" % (prefix, value, postfix)
    return result
