import unittest
import app

class TestApp(unittest.TestCase):
    def test_handleField(self):
        sent = ['name', 'code']
        expected = "name, code"
        result = app.handleFields(sent)
        self.assertEqual(result, expected)

    def test_handleFilters_equal(self):
        sent = {'field': 'name', 'value': 1}
        expected = 'name = 1'
        result = app.handleFilters(sent)
        self.assertEqual(result, expected)

    def test_handleFilters_contains(self):
        sent = {'field': 'name', 'value': 1, 'predicate': 'contains'}
        expected = 'name LIKE "%1%"'
        result = app.handleFilters(sent)
        self.assertEqual(result, expected)

    def test_handleFilters_error(self):
        sent = {'fields': ['toto']}
        result, v = app.validateInput(sent)
        self.assertIsNotNone(v.errors)


if __name__ == 'main':
    unittest.main()
