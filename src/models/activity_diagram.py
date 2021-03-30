from src.models.activity_diagram_element import ActivityDiagramElement, START_NODE

class ActivityDiagram():
    def __init__(self):
        self.elements = []
        self.start_node = None
        self.name = ""

    def set_elements(self, element):
        self.elements.append(element)
    
    def set_start_node(self, start_node):
        self.start_node = start_node
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return 'Diagrama 1'

    def get_elements(self):
        return ActivityDiagram() 

    def get_start_node(self):
        element = ActivityDiagramElement()
        element.element_type = START_NODE
        return element


    def to_xml():
        return ""

