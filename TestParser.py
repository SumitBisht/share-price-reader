import unittest
import Parser

class TestParser(unittest.TestCase):
  def setUp(self):
    self.p = Parser.Parser('no file')

  def test_should_raise_error_if_file_not_specified(self):
    self.assertRaises(self.p.find_highest_values)

  def test_use_sample_file(self):
    self.p.parse_file_contents('data.csv')
    self.p.find_highest_values()
    results = self.p.get_parsed_data()
    self.assertNotEqual(None, results)
    self.assertEqual(3, len(results))
    self.assertEqual(['Apr', '2000', 23], results['Company 1'])
    self.assertEqual(['Mar', '2000', 24], results['Company 2'])
    self.assertEqual(['June', '2000', 23], results['Company 3'])

  def test_processed_list(self):
    self.p.parse_file_contents('data.csv')
    self.p.find_highest_values()
    result_list = self.p.get_processed_company_list()
    self.assertNotEqual(None, result_list)
    self.assertEqual(3, len(result_list))
    self.assertEqual(result_list[0][0], 'Company 1')
    self.assertEqual(result_list[0][1][0], 'Apr')
    self.assertEqual(result_list[0][1][1], '2000')
    self.assertNotEqual(result_list[0][1][1], 2000)
    self.assertNotEqual(result_list[0][1][2], '23')
    self.assertEqual(result_list[0][1][2], int('23'))

  def test_command_line_requires_csv_as_second_argument(self):
    self.assertRaises( Parser.main() )
    self.assertRaises( Parser.main(["data.csv"]) )
    self.assertRaises( Parser.main(["parser.py", "not a csv"]) )
    Parser.main(["parser.py", "data.csv"])

  def tearDown(self):
    self.p = None

if __name__ == '__main__':
  unittest.main()
