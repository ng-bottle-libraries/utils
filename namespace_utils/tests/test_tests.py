from unittest import TestCase, main as unittest_main

from namespace_utils.test_class import Test


class TestTests(TestCase):
    """ Ah, so meta! - This just tests that the same things which pass under unittest pass under Test """

    def test_raises(self):
        expression = lambda: 1 / 0
        self.assertRaises(ZeroDivisionError, expression)
        Test().assertRaises(ZeroDivisionError, expression)

    def test_true(self):
        value = True
        self.assertTrue(value)
        Test().assertTrue(value)

    def test_false(self):
        value = False
        self.assertFalse(value)
        Test().assertFalse(value)

    def test_in(self):
        item, enum = '5', ('5', '6')
        self.assertIn(item, enum)
        Test().assertIn(item, enum)

    def test_not_in(self):
        item, enum = '5', ('3', '6')
        self.assertNotIn(item, enum)
        Test().assertNotIn(item, enum)

    def test_equal(self):
        got, expect = 5, 5
        self.assertEqual(got, expect)
        Test().assertEqual(got, expect)

    def test_inequal(self):
        got, expect = 5, '5'
        self.assertNotEqual(got, expect)
        Test().assertInequal(got, expect)


if __name__ == '__main__':
    unittest_main()
