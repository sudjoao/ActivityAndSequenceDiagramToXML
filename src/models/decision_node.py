from models.activity_diagram_element import ActivityDiagramElement

class DecisionNode(ActivityDiagramElement):
    def __init__(self, name='', element_type=''):
        super().__init__(name, element_type)

    def __eq__(self, decision_node):
        return self.name == decision_node.name and \
                self.element_type == decision_node.element_type

    def __str__(self):
        return 'Name: {}\nElement type: {}\n', self.name, self.element_type                