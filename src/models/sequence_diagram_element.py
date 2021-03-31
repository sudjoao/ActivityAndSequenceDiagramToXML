LIFELINE = 'LifeLine'
MESSAGE = 'Message'
FRAGMENT = 'Fragment'

class SequenceDiagramElement():
    def __init__(self, name='', guard_condition=''):
        self.name = name
        self.guard_condition = guard_condition

    