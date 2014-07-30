class Test:
    """ Simple singleton test class for using when unittest library isn't applicable,
        e.g.: in unittest classmethods """

    def __init__(self):
        pass

    @staticmethod
    def assertFalse(value):
        assert not value, "'{0}' isn't falsey".format(value)

    @staticmethod
    def assertTrue(value):
        assert value, "'{0}' isn't truthy".format(value)

    @staticmethod
    def assertEqual(expect, got):
        assert expect == got, "Expected: '{0}', got '{1}'".format(expect, got)

    @staticmethod
    def assertInequal(expect, got):
        assert expect != got, "Expected: '{0}' isn't '{1}'".format(expect, got)

    @staticmethod
    def assertIn(item, enum):
        assert item in enum, "'{0}' not found in '{1}'".format(item, enum)

    @staticmethod
    def assertNotIn(item, enum):
        assert item not in enum, "'{0}' found in '{1}'".format(item, enum)

    @staticmethod
    def assertRaises(exception, expression):
        try:
            expression()
        except exception:
            return True
        raise AssertionError("'{0}' didn't raise: '{1}'".format(expression, exception))
