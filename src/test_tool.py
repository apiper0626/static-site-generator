import unittest

from textnode import TextNode, TextType
from tool import split_nodes_delimiter


class TestTool(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        print(new_nodes)





if __name__ == "__main__":
    unittest.main()
