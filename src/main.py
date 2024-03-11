from textnode import TextNode
from htmlnode import LeafNode, ParentNode, HTMLNode

def main():
    node = TextNode('This is a text node', 'italics', 'localhost:8888')
    print(node.__repr__)

main()