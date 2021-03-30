import unittest
import src.models.activity_diagram as activity_diagram_model
from src.models.activity_diagram_element import ActivityDiagramElement, START_NODE

class TestActivityDiagram(unittest.TestCase):

    def setUp(self):
        self.activity_diagram = activity_diagram_model.ActivityDiagram()
        self.activity_diagram2 = activity_diagram_model.ActivityDiagram()
    
    def test_set_name(self):
        self.activity_diagram.set_name('Diagrama 1')
        self.assertEqual(self.activity_diagram.get_name(), 'Diagrama 1')
    
    def test_set_elements(self):
        element = []
        element.append(ActivityDiagramElement())
        self.activity_diagram.set_elements(element[0])
        self.assertListEqual(self.activity_diagram.get_elements(), element)

    def test_set_start_node(self):
        element = ActivityDiagramElement()
        element.set_element_type(START_NODE)
        element.set_name('Elemento 1')
        self.activity_diagram.set_start_node(element)
        self.assertEqual(self.activity_diagram.get_start_node(), element)
    
    def test_set_name2(self):
        self.activity_diagram2.set_name('Diagrama 2')
        self.assertEqual(self.activity_diagram2.get_name(), 'Diagrama 2')
    
    def test_set_elements2(self):
        element = []
        element.append(ActivityDiagramElement("Diagrama 2"))
        self.activity_diagram2.set_elements(element[0])
        self.assertListEqual(self.activity_diagram2.get_elements(), element)


    def test_set_start_node2(self):
        element = ActivityDiagramElement('Elemento 2')
        element.set_element_type(START_NODE)
        self.activity_diagram2.set_start_node(element)
        self.assertEqual(self.activity_diagram2.get_start_node(), element)
