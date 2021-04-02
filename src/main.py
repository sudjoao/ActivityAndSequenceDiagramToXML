from models.activity_diagram import ActivityDiagram
from models.activity_diagram_element import ActivityDiagramElement
from models.transition import Transition
from utils.utils import Util
from time import sleep

util = Util()

def main():
    print(util.START_NODE)
    main_menu()

def main_menu():
    while(True):
        print('----- Main Menu -----')
        print('Select the diagram you want to generate:\n'
            '1 - Activity Diagram\n'
            '2 - Sequence Diagram\n'
            '3 - Exit')
        user_in = input('Insert your option: ')
        
        if(user_in == '1'):
            name = input('Insert the Activity Diagram name: ')
            activity_diagram_menu(name)
            sleep(5)
            clear()
        elif(user_in == '2'):
            sequence_diagram_menu()
            clear()
        elif(user_in == '3'):
            print('Leaving the program!')
            return 0
        else:
            clear()
            print('Invalid input. Please select again\n')
    
def activity_diagram_menu(name):
    clear()

    activity_diagram = ActivityDiagram(name=name)
    while(True):
        print('----- Activity Diagram Menu -----')
        print('Select the element you want to generate:\n'
            f'1 - {util.START_NODE}\n'
            f'2 - {util.ACTIVITY_NODE}\n'
            f'3 - {util.DECISION_NODE}\n'
            f'4 - {util.MERGE_NODE}\n'
            f'5 - {util.END_NODE}\n'
            '6 - Return to Main Menu')
        user_in = input('Insert your option: ')
        
        if user_in == '1':
            if util.check_start_node_existence(activity_diagram.get_elements()):
                clear()
                print('Start node already exists!')
                # TODO Criar exceção
                sleep(2)
            else:
                start_node_name = input('Insert the Start Node name: ')
                start_node = ActivityDiagramElement(name=start_node_name, element_type=util.START_NODE)
                activity_diagram.set_elements(start_node)
                activity_diagram.set_start_node(start_node)
        elif user_in == '2':
            if util.check_start_node_existence(activity_diagram.get_elements()):
                activity_node_name = input('Insert the Activity Node name: ')
                activity_node = ActivityDiagramElement(name=activity_node_name, element_type=util.ACTIVITY_NODE)
                activity_diagram.set_elements(activity_node)
                add_transition(activity_diagram, activity_node)
            else:
                clear()
                print('You need to create a start node before add others nodes')
                # TODO Criar exceção
                sleep(2)

        elif user_in == '3':
            if util.check_start_node_existence(activity_diagram.get_elements()):
                decision_node_name = input('Insert the Decision Node name: ')
                decision_node = ActivityDiagramElement(name=decision_node_name, element_type=util.DECISION_NODE)
                activity_diagram.set_elements(decision_node)
                add_transition(activity_diagram, decision_node)
                # TODO Lógica de separação dos 2 caminhos de decisão
            else:
                clear()
                print('You need to create a start node before add others nodes')
                # TODO Criar exceção
        elif user_in == '4':
        
            if util.check_start_node_existence(activity_diagram.get_elements()) and \
               util.check_join_possibility(activity_diagram.get_elements()):
                merge_node_name = input('Insert the Merge Node name: ')
                merge_node = ActivityDiagramElement(name=merge_node_name, element_type=util.MERGE_NODE)
                activity_diagram.set_elements(merge_node)
                add_transition(activity_diagram, merge_node)
            else:
                clear()
                print('something wrong happens')
                sleep(2)
            
        elif user_in == '5':
            if util.check_start_node_existence(activity_diagram.get_elements()):
                end_node_name = input('Insert the End Node name: ')
                end_node = ActivityDiagramElement(name=end_node_name, element_type=util.END_NODE)
                add_transition(activity_diagram, end_node)
                activity_diagram.set_elements(end_node)
            else:
                clear()
                print('You need to create a start node before add others nodes')
                # TODO Criar exceção
                sleep(2)
            
        elif user_in == '6':
            print(activity_diagram.to_xml())
            return
        else:
            clear()
            print('Invalid input. Please select again\n')

def sequence_diagram_menu():
    clear()
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
            clear()
            print('Invalid input. Please select again\n')

def add_transition(activity_diagram, source_element):
    print(activity_diagram.elements)
    elements = list(activity_diagram.elements.values())
    print(elements)
    position = elements.index(source_element)
    print(position)
    before_element = elements[0 : position]
    print(before_element)
    source = None
    name = input('Type the transition name: ')
    print('Select the source node of the actual node:')
    for index, element in  enumerate(before_element):
        print(f'{index} - {element}')
    source = int(input('Type the number of your choice: '))
    prob = input('Type the probability of this transition: ')
    source_node = activity_diagram.elements[elements[source].name]

    activity_diagram.set_transitions(Transition(name=name,
                                                prob=prob,
                                                source=source_node, 
                                                target=None, 
                                                element_type=util.TRANSITION_NODE))
def clear():
    for i in range(1, 50):
        print()

if __name__ == "__main__":
    main()