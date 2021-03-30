START_NODE = "StartNode"
ACTIVITY = "Activity"
TRANSITION = "Transition"
DECISION_NODE = "DecisionNode"
MERGE_NODE = "MergeNode"
END_NODE = "EndNode"

class ActivityDiagramElement():
    def __init__(self):
        self.name = ""
        self.transitions = []
        self.element_type = ""
    
    def set_name(self, name):
        self.name = name

    def set_transitions(self, transition):
        self.transitions.append(transition)
    
    def set_element_type(self, element_type):
        self.element_type = element_type

    def get_name(self):
        return 'Caio'

    def get_transitions(self):
        return {
            "name": "transição 1",
            "prob": 1.0
        }

    def get_element_type(self):
        return START_NODE
