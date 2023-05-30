import unittest
import parse

line = "| 717 | 1-bit and 2-bit Characters | Easy | Google |"

class TestParse(unittest.TestCase):


    def test_add(self):
        result = parse.add(1,2)
        self.assertEqual(3, result)
    
    def test_get_title(self):
        result = '1-bit and 2-bit Characters'
        self.assertEqual(parse.get_title(line), result)
    
    def test_get_list_with_updated_link(self):
        result = ["717","https://leetcode.com/problems/1-bit-and-2-bit-characters/","Easy", "Google"]
        lineObj = parse.Line(line=line).get_list()
        self.assertEqual(result, lineObj)

    def test_get_formatted_line(self):
        result = "| 717 | [1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters/) | Easy | Google |\n"
        formatted_line = parse.Line(line).get_formatted_line()
        self.assertEqual(result, formatted_line)




if __name__ == "__main__":
    unittest.main()