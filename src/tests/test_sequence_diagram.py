import unittest
from models.activity_diagram import ActivityDiagram

from models.sequence_diagram import SequenceDiagram
from models.sequence_diagram_element import SequenceDiagramElement
from parameterized import parameterized


class TestSequenceDiagram(unittest.TestCase):

    def setUp(self):
        self.sequence_diagram = SequenceDiagram()
    
    @parameterized.expand([
        ['Diagrama 1'],
        ['Diagrama 2'],
        ['Diagrama 3'],
    ])
    def test_set_name(self, name):
        self.sequence_diagram.set_name(name)
        self.assertEqual(self.sequence_diagram.get_name(), name)
    
    @parameterized.expand([
        ['Condition 1'],
        ['Condition 2'],
        ['Condition 3'],
    ])
    def test_set_guard_condition(self, guard_condition):
        self.sequence_diagram.set_guard_condition(guard_condition)
        self.assertEqual(self.sequence_diagram.get_guard_condition(), guard_condition)

    @parameterized.expand([
        [SequenceDiagramElement('Elemento 1')],
        [SequenceDiagramElement('Elemento 2')],
        [SequenceDiagramElement('Elemento 3')],
    ])
    def test_set_life_lines(self, life_line):
        self.sequence_diagram.set_life_lines(life_line)
        self.assertListEqual(self.sequence_diagram.get_life_lines(), [life_line])

    @parameterized.expand([
        [SequenceDiagramElement('Elemento 1')],
        [SequenceDiagramElement('Elemento 2')],
        [SequenceDiagramElement('Elemento 3')],
    ])
    def test_set_elements(self, element):
        self.sequence_diagram.set_elements(element)
        self.assertListEqual(self.sequence_diagram.get_elements(), [element])

    def tearDown(self):
        self.sequence_diagram.dispose()