from models.activity_diagram_element import ActivityDiagramElement

class EndNode(ActivityDiagramElement):
    def __init__(self, name='', element_type=''):
        super.__init__(name=name, element_type=element_type)

    def __eq__(self, end_node): # pragma: no cover
        return self.name == end_node.name and \
        self.element_type == end_node.element_type

    def __str__(self): # pragma: no cover
        return 'Name: {}\nElement Type: {}\n'.format(self.name, \
                                                        self.element_type