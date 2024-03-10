import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This is a text node", "bold", 'localhost:8888')
        node2 = TextNode("This is a text node", "bold", 'localhost:8888')
        self.assertEqual(node, node2)
    
    def test_different(self):
        node = TextNode("This is a text node", "italics")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()