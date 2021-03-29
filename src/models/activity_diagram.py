class ActivityDiagram():
    def __init__(self):
        self.elements = []
        self.start_node = None
        self.name = ""

    def __init__(self, elements, start_node, name):
        self.elements = elements
        self.start_node = start_node
        self.name = name

    def add_element(self, diagram_element):
        self.elements.append(diagram_element)

    def to_xml():
        return ""

