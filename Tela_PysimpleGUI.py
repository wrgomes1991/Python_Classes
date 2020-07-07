
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('Calendário')],
    [sg.Text('Qual data deseja agendar?')],
    [sg.In(key='-CAL-', enable_events=True, visible=False), sg.CalendarButton('Calendar', target='-CAL-', pad=None, font=('MS Sans Serif', 10, 'bold'), key='_CALENDAR_', format=('%d %B, %Y'))],
    [sg.Button('OK'), sg.Button('Cancel')]
]

window = sg.Window('AC Nails', layout)

while True:
    event, values = window.read()
    print('Agendamento concluído para,', '-CAL')
    if event in 'Cancel':
        break

window.close()
