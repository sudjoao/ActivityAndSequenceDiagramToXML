class SequenceDiagramElement():
    def __init__(self, name=''):
        self.name = name

    def __eq__(self, sequence_diagram_element): # pragma: no cover
        return self.name == sequence_diagram_element.name
    
    def __str__(self): # pragma: no cover
        return 'Name: {}\n'.format(self.name)

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def dispose(self):
        self.name = ""