import unittest
import src.models.activity_diagram as activity_diagram_model
from src.models.activity_diagram_element import ActivityDiagramElement, START_NODE

class TestActivityDiagram(unittest.TestCase):

    def setUp(self):
        self.activity_diagram = activity_diagram_model.ActivityDiagram()
    
    def test_set_name(self):
        self.activity_diagram.set_name('Diagrama 1')
        self.assertEqual(self.activity_diagram.get_name(), 'Diagrama 1')
    
    def test_set_elements(self):
        element = ActivityDiagramElement()
        self.activity_diagram.set_elements(element)
        self.assertEqual(self.activity_diagram.get_elements().name, element.name)


    def test_set_start_node(self):
        element = ActivityDiagramElement()
        element.element_type = START_NODE
        self.activity_diagram.set_start_node(element)
        self.assertEqual(self.activity_diagram.get_start_node().element_type, element.element_type)
    