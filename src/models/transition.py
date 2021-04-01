from models.activity_diagram_element import ActivityDiagramElement

class Transition(ActivityDiagramElement):
    def __init__(self, name='', source='', target='', element_type=''):
      super().__init__(name, elementy_type)
      self.source = source
      self.target = target

    def __eq__(self, transition):
        return self.name == transition.name and \
                self.source == transition.source and \
                self.target == transition.target

    def __str__(self):
        return 'Name: {}\Source: {}\nTarget: {}'.format(self.name, self.source, self.target)

    def get_source(self):
        return self.source
    
    def set_source(self, source):
        self.source = source

    def get_target(self):
        return self.target

    def set_target(self, target):
        self.target = target

      




  

  
