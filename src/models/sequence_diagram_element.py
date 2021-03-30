LIFELINE='LifeLine'
MESSAGE='Message'
FRAGMENT='Fragment'
class SequenceDiagramElement():
    def __init__(self):
        self.name = ''
        self.element_type = ''

    def __init__(self, name, element_type):
        self.name = name
        self.element_type = element_type
    