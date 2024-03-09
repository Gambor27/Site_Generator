from textnode import TextNode

def main():
    node = TextNode('This is a text node', 'italics', 'localhost:8888')
    print(node.__repr__)


main()