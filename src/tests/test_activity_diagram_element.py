import unittest

from models.activity_diagram_element import ActivityDiagramElement, START_NODE, DECISION_NODE, MERGE_NODE
from parameterized import parameterized


class TestActivityDiagramElement(unittest.TestCase):

    def setUp(self):
        self.activity_diagram_element = ActivityDiagramElement()

    @parameterized.expand([
        ['Elemento 1'],
        ['Elemento 2'],
        ['Elemento 3'],
    ])
    def test_set_name(self, name):
        self.activity_diagram_element.set_name(name)
        self.assertEqual(self.activity_diagram_element.get_name(), name)
    
    @parameterized.expand([
        [{'name':'Transição 1', 'prob':1.0}],
        [{'name':'Transição 2', 'prob':0.5}],
        [{'name':'Transição 3', 'prob':0.0}],
    ])
    def test_set_transitions(self, transition_dict):
        self.activity_diagram_element.set_transitions(transition_dict)
        self.assertListEqual(self.activity_diagram_element.get_transitions(), [transition_dict])

    @parameterized.expand([
        [START_NODE],
        [DECISION_NODE],
        [MERGE_NODE],
    ])
    def test_set_element_type(self, element_type):
        self.activity_diagram_element.set_element_type(element_type)
        self.assertEqual(self.activity_diagram_element.get_element_type(), element_type)
    
    def tearDown(self):
        self.activity_diagram_element.dispose()
