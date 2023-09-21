
import PySimpleGUI as sg
import zip_creator

lable1 = sg.Text('Select files to compress')
input1 = sg.Input()
choose_button1 = sg.FilesBrowse('Choose',key = 'filepath1')

lable2 = sg.Text('Select destination folder')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose',key='dest')

compress_button = sg.Button('Compress')
compress_output = sg.Text(key='output')

window = sg.Window('File Compresser', layout=[[lable1, input1, choose_button1],
                                                [lable2, input2, choose_button2],
                                                [compress_button, compress_output]])
while True:
    a, b = window.read()
    print(a)
    print(b)
    filepaths = b['filepath1'].split(';')
    folder = b['dest']
    print(f'file : {filepaths}')
    print(f'destination :  {folder}')
    zip_creator.make_zip(filepaths, folder)
    window['output'].update(value='Compresstion Completed')


window.close()