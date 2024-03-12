class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        return_props = ""
        for key in self.props:
            return_props += f' {key}=\"{self.props[key]}\"'
        return return_props
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        html = ''
        #if not self.value:
        #   raise ValueError
        if self.tag:
            html += f'<{self.tag}>'
        if self.props:
            html += self.props_to_html()
        html += self.value
        if self.tag:
            html += f'</{self.tag}>'
        return html
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("tag required")
        if not self.children:
            raise ValueError("chid nodes required")
        return_html = f"<{self.tag}"
        if self.props:
            return_html += f"{self.props_to_html()}"
        return_html += ">"
        for leaf in self.children:
            return_html += leaf.to_html()
        return_html += f"</{self.tag}>"
        return return_html

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"