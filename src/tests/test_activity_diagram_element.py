import unittest
from utils.utils import Util
from models.activity_diagram_element import ActivityDiagramElement
from parameterized import parameterized

util = Util()


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
        [util.START_NODE],
        [util.DECISION_NODE],
        [util.MERGE_NODE],
    ])
    def test_set_element_type(self, element_type):
        self.activity_diagram_element.set_element_type(element_type)
        self.assertEqual(self.activity_diagram_element.get_element_type(), element_type)
    
    def tearDown(self):
        self.activity_diagram_element.dispose()
