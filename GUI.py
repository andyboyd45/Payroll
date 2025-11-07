import PySimpleGUI as sg
import Payroll as p


def add_employee():
    layout = [[sg.Text('Employee Name:')], [sg.Input('', enable_events=True, key='-NAME-', font=('Arial Bold', 20), expand_x=True)],
              [sg.Text('Employee Position:')], [sg.Input('', enable_events=True, key='-POSITION-', font=('Arial Bold', 20), expand_x=True)],
              [sg.Text('Employee Salary(Per Year):')], [sg.Input('', enable_events=True, key='-SALARY-', font=('Arial Bold', 20), expand_x=True)],
              [sg.Button('DONE')], [sg.Button('MAIN MENU')]]
    
    window = sg.Window('Add Employee', layout, size=(1920,1080))
    
    while True:
        event,value = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        elif event == 'MAIN MENU':
            window.close()
            main_win()
        elif event == 'DONE':
            if event == '-SALARY-':
                if value['-SALARY-'][-1] not in ('0123456789'):
                    sg.popup("Digit allowed only")
                    window['-SALARY-'].update(value['-SALARY-'][:-1])
                    
            elif value['-NAME-'] == "" or value['-POSITION-'] == "" or value['-SALARY-'] == "":
                sg.popup('NEED TO INPUT EMPOLYEE INFO')
                
            else:
                p.create_employee(value['-NAME-'], value['-POSITION-'], float(value['-SALARY-']))
                sg.popup('Employee added!')
                print('Employee added to Payroll.xlsx')
                break
    
    window.close()


def find_employee_win():
    layout = [[sg.Text("Input Employee's UUID:")], [sg.Input('', enable_events=True, key='-UUID-', font=('Arial Bold', 20), expand_x=True)],
              [sg.Button('DONE')], [sg.Button('Main Menu')]]
    window = sg.Window("Find Employee", layout, size=(1920,1080))
    
    while True:
        event, value = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Main Menu':
            window.close()
            main_win()
        elif event == 'DONE':
            if value['-UUID-'] == '':
                sg.popup('NEED TO INPUT UUID')
            else:
               employee =  p.find_employee(value['-UUID-'])
               
               if employee == None:
                   sg.popup('No Employee Found')
               else:
                   print('Info Found')
                   edit_win(employee)


def edit_win(employee = p.Employee):
    Heading = ['Employee', 'Position', 'Salary', 'Experience', 'ID']
    employee_info = [
                    [employee.getname(), employee.getposition(), employee.getsalary(), employee.getexp(), employee.getID()]
    ]
    layout = [[sg.Table(values = employee_info, headings= Heading, num_rows=1, auto_size_columns=True, key = '-TABLE-')], 
              [sg.Button('Main Menu')], [sg.Button('EDIT')]]     

    window = sg.Window('Employee Info',layout, size = (1920,1080))
    
    while True:
        event, value = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Main Menu':
            window.close()
            main_win()
        elif event == 'EDIT':
            #Enable editing of employee
            pass
        
        window.close()
        

def main_win():
    layout = [
        [sg.Button('Add Employee')],
        [sg.Button('Find Employee')],
        [sg.Button('Exit')]
    ]
    
    window = sg.Window("Demo", layout, size=(1920,1080))
    
    while True:
        event, values = window.read()
        
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        elif event == 'Add Employee':
            window.close()
            add_employee()
        elif event == 'Find Employee':
            window.close()
            find_employee_win()
            
    
    window.close()

