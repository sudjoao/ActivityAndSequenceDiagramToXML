START_NODE = 'StartNode'
ACTIVITY = 'Activity'
TRANSITION = 'Transition'
DECISION_NODE = 'DecisionNode'
MERGE_NODE = 'MergeNode'
END_NODE = 'EndNode'

class ActivityDiagramElement():
    def __init__(self, name='', transitions=[], element_type=''):
        self.name = name
        self.transitions = transitions.copy()
        self.element_type = element_type

    def __eq__(self, activity_diagram_element):
        return self.name == activity_diagram_element.name and \
        self.element_type == activity_diagram_element.element_type and \
        self.transitions == activity_diagram_element.transitions

    def __str__(self):
        return 'Name: {}\nElement Type: {}\nTransitions: {}\n'.format(self.name, \
                                                                self.element_type, \
                                                                self.transitions)

    def dispose(self):
        self.name = ''
        self.transitions = []
        self.element_type = ''

    def set_name(self, name):
        self.name = name

    def set_transitions(self, transition):
        self.transitions.append(transition)
    
    def set_element_type(self, element_type):
        self.element_type = element_type

    def get_name(self):
        return self.name

    def get_transitions(self):
        return self.transitions

    def get_element_type(self):
        return self.element_type
