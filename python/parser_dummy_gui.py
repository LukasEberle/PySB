import PySimpleGUI as sg
import os.path

file_list_column = [
    [
        sg.Text("Input Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20),
            key="-FILE LIST-"
        )
    ]
]

image_viewer_column = [
    [sg.Text("Choose a file from the list on the left:")],
    [sg.Text(size=(65, 1), key="-TOUT-")],
    [sg.Text('Enter a name for the output file:'), sg.InputText('output.csv', key="-OFILE-")],
    [sg.Text("Choose a language:"), sg.Combo(['de', 'en'], key="-LANG-")],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column)
    ]
]

window = sg.Window("Parameter Picker", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".json"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
        except:
            pass
    elif event == "Ok":
        try:
            print(filename)
            print(values["-OFILE-"])
            print(values["-LANG-"])
        except:
            pass

window.close()
