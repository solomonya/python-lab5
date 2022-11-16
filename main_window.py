import PySimpleGUI as sg
import contact_information_window
import database_interface
import validation

layout = [[sg.Text("Enter full name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20, 1))],
          [sg.Text("Enter address:"), sg.Input(key='-ADDRESS-', do_not_clear=True, size=(10, 1))],
          [sg.Text("Enter phone number:"), sg.Input(key='-PHONE_NUMBER-', do_not_clear=True, size=(10, 1))],
          [sg.Button('Submit Contact Information'), sg.Button('Show Table'), sg.Exit()]]

window = sg.Window("Submit Contact Information", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Submit Contact Information':
        validation_result = validation.validate(values)
        if validation_result["is_valid"]:
            database_interface.insert_contact(values['-NAME-'], values['-ADDRESS-'], values['-PHONE_NUMBER-'])
            sg.popup("Contact Information submitted!")
        else:
            error_message = validation.generate_error_message(validation_result["values_invalid"])
            sg.popup(error_message)
    elif event == 'Show Table':
        contact_information_window.create()