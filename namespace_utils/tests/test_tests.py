from unittest import TestCase, main as unittest_main

from namespace_utils.test_funs import *


class TestTests(TestCase):
    """ Ah, so meta! - unittests checking that what passes/fails under unittest passes/fails with my lib """

    def test_raises(self):
        expression = lambda: 1 / 0
        self.assertRaises(ZeroDivisionError, expression)
        assertRaises(ZeroDivisionError, expression)

    def test_true(self):
        value = True
        self.assertTrue(value)
        assertTrue(value)

    def test_false(self):
        value = False
        self.assertFalse(value)
        assertFalse(value)

    def test_in(self):
        item, enum = '5', ('5', '6')
        self.assertIn(item, enum)
        assertIn(item, enum)

    def test_not_in(self):
        item, enum = '5', ('3', '6')
        self.assertNotIn(item, enum)
        assertNotIn(item, enum)

    def test_equal(self):
        got, expect = 5, 5
        self.assertEqual(got, expect)
        assertEqual(got, expect)

    def test_inequal(self):
        got, expect = 5, '5'
        self.assertNotEqual(got, expect)
        assertInequal(got, expect)


if __name__ == '__main__':
    unittest_main()
