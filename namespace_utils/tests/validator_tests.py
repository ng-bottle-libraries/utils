from unittest import TestCase, main as unittest_main

from namespace_utils.validators import is_email


class TestValidators(TestCase):
    def test_is_email_failure(self):
        self.assertFalse(is_email('foo@bar'))
        self.assertFalse(is_email('f@b'))
        self.assertFalse(is_email(''))

    def test_is_email_success(self):
        self.assertTrue(is_email('foo@bar.com'))
        self.assertTrue(is_email('.foo.bar@bar.com'))
        self.assertTrue(is_email('foo-bar@bar.com'))


if __name__ == '__main__':
    unittest_main()
