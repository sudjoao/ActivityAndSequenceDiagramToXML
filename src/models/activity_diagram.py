from models.activity_diagram_element import ActivityDiagramElement

class ActivityDiagram():
    def __init__(self, start_node= None, name=''):
        self.elements = []
        self.start_node = start_node
        self.name = name

    def __eq__(self, activity_diagram): # pragma: no cover
        return self.name == activity_diagram.name and \
        self.start_node == activity_diagram.start_node and \
        self.elements == activity_diagram.elements
    
    def __str__(self): # pragma: no cover
        return 'Name: {}\nStart Node: {}\nElements: {}\n'.format(self.name, \
                                                                self.start_node, \
                                                                self.elements)

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
        return self.name

    def get_elements(self):
        return self.elements

    def get_start_node(self):
        return self.start_node

    def to_xml():
        return ''

