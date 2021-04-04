from models.activity_diagram import ActivityDiagram
from models.activity_diagram_element import ActivityDiagramElement
from models.transition import Transition
from errors.errors import OrderError, MissMergeError
from utils.utils import Util
from time import sleep

util = Util()


def main():
    while(True):
        print('----- Main Menu -----')
        print('Select the diagram you want to generate:\n'
            '1 - Activity Diagram\n'
            '2 - Sequence Diagram\n'
            '3 - Exit')
        user_in = input('Insert your option: ')
        
        if(user_in == '1'):
            print('----- Activity Diagram -----')
            name = input('Insert the Activity Diagram name: ')
            activity_diagram_menu(name)
            sleep(5)
            util.clear()
        elif(user_in == '2'):
            print('----- Sequence Diagram -----')
            name = input('Insert the Sequence Diagram name: ')
            sequence_diagram_menu()
            util.clear()
        elif(user_in == '3'):
            print('Leaving the program!')
            return 0
        else:
            util.clear()
            print('Invalid input. Please select again\n')
    
def activity_diagram_menu(name):
    util.clear()

    activity_diagram = ActivityDiagram(name=name)
    while(True):
        print('----- Activity Diagram Menu -----')
        print('Select the element you want to generate:\n'
            f'1 - {util.START_NODE}\n'
            f'2 - {util.ACTIVITY_NODE}\n'
            f'3 - {util.DECISION_NODE}\n'
            f'4 - {util.MERGE_NODE}\n'
            f'5 - {util.END_NODE}\n'
            '6 - Generate Diagram\n'
            '7 - Return to Main Menu')
        user_in = input('Insert your option: ')
        
        if user_in == '1':
            try:
                util.check_start_node_existence(activity_diagram.get_elements(), util.START_NODE)
                start_node_name = input('Insert the Start Node name: ')
                start_node = ActivityDiagramElement(name=start_node_name, element_type=util.START_NODE)
                activity_diagram.set_elements(start_node)
                activity_diagram.set_start_node(start_node)
            except OrderError as e:
                util.print_and_clear(e)
            
        elif user_in == '2':
            try:
                util.check_start_node_existence(activity_diagram.get_elements(), util.ACTIVITY_NODE)
                activity_node_name = input('Insert the Activity Node name: ')
                activity_node = ActivityDiagramElement(name=activity_node_name, element_type=util.ACTIVITY_NODE)
                activity_diagram.set_elements(activity_node)
                add_transition(activity_diagram, activity_node)
            except OrderError as e:
                util.print_and_clear(e)

        elif user_in == '3':
            try:
                util.check_start_node_existence(activity_diagram.get_elements(), util.DECISION_NODE)
                decision_node_name = input('Insert the Decision Node name: ')
                decision_node = ActivityDiagramElement(name=decision_node_name, element_type=util.DECISION_NODE)
                activity_diagram.set_elements(decision_node)
                add_transition(activity_diagram, decision_node)
            except OrderError as e:
                util.print_and_clear(e)

        elif user_in == '4':
            try:
                util.check_start_node_existence(activity_diagram.get_elements(), util.MERGE_NODE)
                util.check_join_possibility(activity_diagram.get_elements())
                merge_node_name = input('Insert the Merge Node name: ')
                merge_node = ActivityDiagramElement(name=merge_node_name, element_type=util.MERGE_NODE)
                activity_diagram.set_elements(merge_node)
                add_transition(activity_diagram, merge_node)
            except OrderError as e:
                util.print_and_clear(e)
            
        elif user_in == '5':
            try:
                util.check_start_node_existence(activity_diagram.get_elements(), util.END_NODE)
                util.check_close_possibility(activity_diagram.get_elements())
                end_node_name = input('Insert the End Node name: ')
                end_node = ActivityDiagramElement(name=end_node_name, element_type=util.END_NODE)
                activity_diagram.set_elements(end_node)
                add_transition(activity_diagram, end_node)
            except OrderError as e:
                util.print_and_clear(e)
            except MissMergeError as e:
                util.print_and_clear(e)

        elif user_in == '6':
            try:
                util.generate_diagram(activity_diagram)
                return 0
            except Exception as e:
                util.print_and_clear(e)
        
        elif user_in == '7':
            return 0
        
        else:
            util.clear()
            print('Invalid input. Please select again\n')

def sequence_diagram_menu():
    util.clear()
    while True:
        print('----- Sequence Diagram Menu -----')
        print('Select the element you want to generate:\n'
            f'1 - {util.LIFELINE}\n'
            f'2 - {util.FRAGMENT}\n'
            f'3 - {util.MESSAGE}\n'
            '4 - Return to Main Menu')
        user_in = input('Insert your option: ')
        
        if user_in == '1':
            break
        elif user_in == '2':
            break
        elif user_in == '3':
            break
        elif user_in == '4':
            return
        else:
            util.clear()
            print('Invalid input. Please select again\n')

def add_transition(activity_diagram, source_element):
    elements = list(activity_diagram.elements.values())
    position = elements.index(source_element)
    before_element = elements[0 : position]
    source = None
    name = input('Type the transition name: ')
    print('Select the source node of the actual node:')
    index = 0
    while(True):
        for index, element in  enumerate(before_element):
            print(f'{index} - {element}')
        try:
            source = int(input('Type the number of your choice: '))
            if(source<0 or source>index):
                raise ValueError()
            break
        except ValueError:
            util.print_and_clear(f'You need input a number between 0 and {index}', False)

    while(True):
        try:
            prob = float(input('Type the probability of this transition(0.0 - 1.0): '))
            if(prob<0 or prob>1):
                raise ValueError()
            break
        except ValueError:
            util.print_and_clear('You need input a number between 0.0 and 1.0', False)

    source_node = activity_diagram.elements[elements[source].name]

    activity_diagram.set_transitions(Transition(name=name,
                                                prob=prob,
                                                source=source_node, 
                                                target=None, 
                                                element_type=util.TRANSITION_NODE))

if __name__ == "__main__":
    main()