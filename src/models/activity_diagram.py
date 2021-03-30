from src.models.activity_diagram_element import ActivityDiagramElement, START_NODE

class ActivityDiagram():
    def __init__(self, elements=[], start_node= None, name=''):
        self.elements = elements
        self.start_node = start_node
        self.name = name

    def __eq__(self, activity_diagram):
        return self.name == activity_diagram.name and \
        self.start_node == activity_diagram.start_node and \
        self.elements == activity_diagram.elements

    def dispose(self):
        self.elements = []
        self.start_node = None
        self.name = ''

    def set_elements(self, element):
        self.elements.append(element)
    
    def set_start_node(self, start_node):
        self.start_node = start_node
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return 'Diagrama 1'

    def get_elements(self):
        element = []
        element.append(ActivityDiagramElement())
        return element

    def get_start_node(self):
        element = ActivityDiagramElement()
        element.set_name('Elemento 1')
        element.element_type = START_NODE
        return element


    def to_xml():
        return ''

