from models.activity_diagram_element import ActivityDiagramElement

class ActivityNode(ActivityDiagramElement):
    def __init__(self, name='', element_type=''):
        super().__init__(name, element_type)

    def __eq__(self, activity):
        return self.name == activity.name and \
                self.element_type == activity.element_type

    def __str__(self):
        return r'{' + f'Name: {self.name}, Element type: {self.element_type}' + r'}'