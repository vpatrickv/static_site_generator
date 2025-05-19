import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
