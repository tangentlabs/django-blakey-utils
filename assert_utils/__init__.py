from django.utils.unittest.util import safe_repr

def assert_dictionary_contains_values(test_case, dictionary_name, dictionary, **kwargs):
    """
    Asserts that specified dictionary contains values specified in keyword arguments
    :param test_case: TestCase-like object which has assertTrue and assertEqual methods
    :param dictionary_name: name to output in case of error.
    :type dictionary_name: str
    :param dictionary: dictionary to validate
    :type dictionary: dict
    :param **kwargs: keyword arguments against which dictionary should be validated.
    """
    for k, v in kwargs.items():
        test_case.assertTrue(dictionary.has_key(k), "%s is not present in dictionary %s" % (k, dictionary_name))
        test_case.assertEqual(dictionary[k], v, "key %s; dictionary %s" % (k, dictionary_name))

def assert_dictionary_contains_values_from(test_case, dictionary_name, dictionary, from_dictionary):
    """
    Asserts that specified dictionary contains all (key, value) pairs from specified from_dictionary
    :param test_case: TestCase-like object which has assertTrue and assertEqual methods
    :param dictionary_name: name to output in case of error.
    :type dictionary_name: str
    :param dictionary: dictionary to validate
    :type dictionary: dict
    :param from_dictionary: dictionary with values which must be in specified param dictionary
    :type from_dictionary: dict
    """
    assert_dictionary_contains_values(test_case, dictionary_name, dictionary, **from_dictionary)

def assert_equal_line_by_line(test_case, expected_text, text, msg = None):
    """
    Asserts that text equals expected_text. Compares expected_text to text line-by-line for better output. Convenient for long texts.
    :param test_case: TestCase-like object which has assertTrue and assertEqual methods
    :param expected_text: expected value
    :type expected_text: str
    :param text: actual value
    :type text: str
    :param msg: optional message to append to the output of error
    :type msg: str
    """
    msg = msg and "\n%s" % msg or ""
    expected_lines = expected_text.splitlines(True)
    text_lines = text.splitlines(True)
    expected_lines_count = len(expected_lines)
    lines_error = ""
    if expected_lines_count != len(text_lines):
        lines_error = "Expected number of lines: %s, but was: %s" % (expected_lines_count, len(text_lines))
    for i in range(min(expected_lines_count, len(text_lines))):
        actual_line = text_lines[i]
        expected_line = expected_lines[i]
        test_case.assertEqual(expected_line, actual_line, "\nLine %s.\nExpected: %s\nActual:   %s\n%s%s" % (i, safe_repr(expected_line), safe_repr(actual_line), lines_error, msg))

