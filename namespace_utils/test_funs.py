""" Useful function for when the unittest library isn't applicable,
    e.g.: in unittest classmethods """

# PS: This doesn't follow PEP8 function-name standards so that it's analogous to the unittest library.


def assertFalse(value):
    assert not value, "'{0}' isn't falsey".format(value)


def assertTrue(value):
    assert value, "'{0}' isn't truthy".format(value)


def assertEqual(expect, got):
    assert expect == got, "Expected: '{0}', got '{1}'".format(expect, got)


def assertInequal(expect, got):
    assert expect != got, "Expected: '{0}' isn't '{1}'".format(expect, got)


def assertIn(item, enum):
    assert item in enum, "'{0}' not found in '{1}'".format(item, enum)


def assertNotIn(item, enum):
    assert item not in enum, "'{0}' found in '{1}'".format(item, enum)


def assertRaises(exception, expression):
    try:
        expression()
    except exception:
        return True
    raise AssertionError("'{0}' didn't raise: '{1}'".format(expression, exception))
