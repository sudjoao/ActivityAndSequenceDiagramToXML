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
        self.node_type = ""
    
    def __init__(self, name, transitions, node_type):
        self.name = name
        self.transitions = transitions
        self.node_type = node_type

