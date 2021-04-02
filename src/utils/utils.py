class Util():
    def __init__(self):
        self.START_NODE='StartNode'
        self.ACTIVITY_NODE='Activity'
        self.TRANSITION_NODE='Transition'
        self.DECISION_NODE='DecisionNode'
        self.MERGE_NODE='MergeNode'
        self.END_NODE='EndNode'
        self.LIFELINE='LifeLine'
        self.MESSAGE='Message'
        self.FRAGMENT='Fragment'

    def check_start_node_existence(self, nodes):
        for element in nodes.values():
            if(element.element_type == self.START_NODE):
                return True
        return False

    def check_join_possibility(self, nodes):
        decision_count = 0
        merge_count = 0
        for element in nodes.values():
            if(element.element_type == self.DECISION_NODE):
                decision_count+=1
            elif(element.element_type == self.MERGE_NODE):
                merge_count+=1
        if(not decision_count or merge_count >= decision_count):
            return False
        
        return True
    
    def get_tab(self, size):
        return '\t'.expandtabs(size)