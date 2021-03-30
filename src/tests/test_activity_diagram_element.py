import unittest
import src.models.activity_diagram_element as activity_diagram_element_model
class TestActivityDiagram(unittest.TestCase):

    def setUp(self):
        self.activity_diagram_element = activity_diagram_element_model.ActivityDiagramElement()

    def test_set_name(self):
        self.activity_diagram_element.set_name('Caio')
        self.assertEqual(self.activity_diagram_element.get_name(), 'Caio')
    
    def test_set_transitions(self):
        transition_dict = {
            "name": "transição 1",
            "prob": 1.0
        }
        self.activity_diagram_element.set_transitions(transition_dict)
        self.assertEqual(self.activity_diagram_element.get_transitions(), transition_dict)


    def test_set_element_type(self):
        self.activity_diagram_element.set_element_type(activity_diagram_element_model.START_NODE)
        self.assertEqual(self.activity_diagram_element.get_element_type(), activity_diagram_element_model.START_NODE)
    