import unittest
from models.activity_diagram import ActivityDiagram

from models.activity_diagram_element import ActivityDiagramElement, START_NODE
from parameterized import parameterized


class TestActivityDiagram(unittest.TestCase):

    def setUp(self):
        self.activity_diagram = ActivityDiagram()
        self.activity_diagram2 = ActivityDiagram()
    
    @parameterized.expand([
        ['Diagrama 1'],
        ['Diagrama 2'],
        ['Diagrama 3'],
    ])
    def test_set_name(self, name):
        self.activity_diagram.set_name(name)
        self.assertEqual(self.activity_diagram.get_name(), name)
    
    @parameterized.expand([
        [ActivityDiagramElement('Elemento 1')],
        [ActivityDiagramElement('Elemento 2')],
        [ActivityDiagramElement('Elemento 3')],
    ])
    def test_set_elements(self, element):
        self.activity_diagram.set_elements(element)
        self.assertListEqual(self.activity_diagram.get_elements(), [element])

    @parameterized.expand([
        [ActivityDiagramElement('Elemento 1', [], START_NODE)],
        [ActivityDiagramElement('Elemento 2', [], START_NODE)],
        [ActivityDiagramElement('Elemento 3', [], START_NODE)],
    ])
    def test_set_start_node(self, element):
        self.activity_diagram.set_start_node(element)
        self.assertEqual(self.activity_diagram.get_start_node(), element)

    def tearDown(self):
        self.activity_diagram.dispose()
        self.activity_diagram2.dispose()