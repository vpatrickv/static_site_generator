from textnode import TextType, TextNode


def main():
    Text_node = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(Text_node)

if __name__== "__main__":
    main()
