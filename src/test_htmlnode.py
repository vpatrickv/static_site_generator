import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "h1",
            "This is a heading text",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        compare = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), compare)

    def test_repr(self):
        node = HTMLNode(
            "h1",
            "This is a heading text",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        compare = "HTMLNode(h1, This is a heading text, children: None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node), compare)

    def test_to_html(self):
        node = HTMLNode(
            "h1",
            "This is a heading text",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )

        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_leaf_to_html_p_1(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_2(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_to_html_a_1(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )


if __name__ == "__main__":
    unittest.main()
