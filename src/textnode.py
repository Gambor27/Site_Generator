from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return Exception("Not a Textnode object")
        return (self.text == other.text 
                and self.text_type == other.text_type
                and self.url == other.url)
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        new_leaf = LeafNode(None, text_node.text)
    elif text_node.text_type == text_type_bold:
        new_leaf = LeafNode("b", text_node.text)
    elif text_node.text_type == text_type_italic:
        new_leaf = LeafNode("i", text_node.text)
    elif text_node.text_type == text_type_code:
        new_leaf = LeafNode("code", text_node.text)
    elif text_node.text_type == text_type_link:
        new_leaf = LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == text_type_image:
        new_leaf = LeafNode("image", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("text type not known")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes.isinstance(TextNode):
        split_text = old_nodes.split(delimiter)
        return_text = []
        if len(split_text) < 3:
            raise Exception("That is not correct Markdown formatting")
        for i, node in enumerate(split_text):
            if 2 % i == 0:
                return_text.append([node, text_type])
            else:
                return_text.append([node, text_type_text])
        return return_text
    else:
        return [old_nodes, text_type]