import os

from dotenv import load_dotenv
from models.activity_diagram import ActivityDiagram
from models.activity_diagram_element import ActivityDiagramElement

load_dotenv()

START_NODE=os.getenv('START_NODE')
ACTIVITY=os.getenv('ACTIVITY')
TRANSITION=os.getenv('TRANSITION')
DECISION_NODE=os.getenv('DECISION_NODE')
MERGE_NODE=os.getenv('MERGE_NODE')
END_NODE=os.getenv('END_NODE')
LIFELINE=os.getenv('LIFELINE')
MESSAGE=os.getenv('MESSAGE')
FRAGMENT=os.getenv('FRAGMENT')

def main():
    print(START_NODE)
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
            f'1 - {START_NODE}\n'
            f'2 - {ACTIVITY}\n'
            f'3 - {TRANSITION}\n'
            f'4 - {DECISION_NODE}\n'
            f'5 - {MERGE_NODE}\n'
            f'6 - {END_NODE}\n'
            '7 - Return to Main Menu')
        user_in = input('Insert your option: ')
        
        if(user_in == '1'):
            start_node_name = input('Insert the Start Node name: ')
            start_node = ActivityDiagramElement(name=start_node_name, element_type=START_NODE)
            activity_diagram.set_elements(start_node)
        elif(user_in == '2'):
            break
        elif(user_in == '3'):
            break
        elif(user_in == '4'):
            break
        elif(user_in == '5'):
            break
        elif(user_in == '6'):
            break
        elif(user_in == '7'):
            return
        else:
            clear()
            print('Invalid input. Please select again\n')

def sequence_diagram_menu():
    clear()
    while(True):
        print('----- Sequence Diagram Menu -----')
        print('Select the element you want to generate:\n'
            f'1 - {LIFELINE}\n'
            f'2 - {FRAGMENT}\n'
            f'3 - {MESSAGE}\n'
            '4 - Return to Main Menu')
        user_in = input('Insert your option: ')
        
        if(user_in == '1'):
            break
        elif(user_in == '2'):
            break
        elif(user_in == '3'):
            break
        elif(user_in == '4'):
            return
        else:
            clear()
            print('Invalid input. Please select again\n')

def clear():
    for i in range(1, 50):
        print()

if __name__ == "__main__":
    main()