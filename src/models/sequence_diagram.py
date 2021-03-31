class SequenceDiagram():
    def __init__(self, name='', guard_condition=''):
        self.name = ''
        self.guard_condition = ''
        self.life_lines = []
        self.elements = []

    def __eq__(self, sequence_diagram): # pragma: no cover
        return self.name == sequence_diagram.name and \
        self.guard_condition == sequence_diagram.guard_condition and \
        self.life_lines == sequence_diagram.life_lines and \
        self.elements == sequence_diagram.elements
    
    def __str__(self): # pragma: no cover
        return 'Name: {}\nGuard Condition: {}\nLife Lines: {}\nElements: {}\n'.format(self.name, \
                                                                                self.start_node, \
                                                                                self.life_lines, \
                                                                                self.elements)

    def dispose(self):
        self.name = ''
        self.guard_condition = ''
        self.life_lines = []
        self.elements = []

    def set_name(self, name):
        self.name = name
    
    def set_guard_condition(self, guard_condition):
        self.guard_condition = guard_condition

    def set_life_lines(self, life_line):
        self.life_lines.append(life_line)
    
    def set_elements(self, element):
        self.elements.append(element)

    def get_name(self):
        return self.name
    
    def get_guard_condition(self):
        return self.guard_condition

    def get_life_lines(self):
        return self.life_lines
    
    def get_elements(self):
        return self.elements

    def create_fragment(self):
        return ''

    def to_xml(self):
        return ''
