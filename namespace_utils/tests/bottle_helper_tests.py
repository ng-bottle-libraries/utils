from unittest import TestCase, main as unittest_main

from bottle import Bottle, request
from webtest import TestApp

from namespace_utils.bottle_helpers import from_params_or_json

sample_app = Bottle(catchall=False, autojson=True)


@sample_app.route('/api', method=['GET', 'POST'])
def api():
    return (lambda k: {k: from_params_or_json(request, k)})('foo')


class TestBottleHelpers(TestCase):
    app = TestApp(sample_app)

    def test_from_params(self):
        self.assertEqual(self.app.get('/api', {'foo': 'bar'}).json, {'foo': 'bar'})

    def test_from_json(self):
        self.assertEqual(self.app.post_json('/api', {'foo': 'bar'}).json, {'foo': 'bar'})


if __name__ == '__main__':
    unittest_main()
