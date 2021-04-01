class Util():
    def __init__(self):
        self.START_NODE='Start Node'
        self.ACTIVITY_NODE='Activity Node'
        self.TRANSITION_NODE='Transition Node'
        self.DECISION_NODE='Decision Node'
        self.MERGE_NODE='Merge Node'
        self.END_NODE='End Node'
        self.LIFELINE='Life Line'
        self.MESSAGE='Message'
        self.FRAGMENT='Fragment'

    def check_start_node_existence(self, nodes):
        for element in nodes:
            if(element.element_type == self.START_NODE):
                return True
        return False

    def check_join_possibility(self, nodes):
        decision_count = 0
        merge_count = 0
        for element in nodes:
            if(element.element_type == self.DECISION_NODE):
                decision_count+=1
            elif(element.element_type == self.DECISION_NODE):
                merge_count+=1
        if(not decision_count or merge_count >= decision_count):
            return False
        
        return True