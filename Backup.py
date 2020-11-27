from PIL import ImageTk, Image
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import zipfile
import datetime
import os


today = datetime.datetime.today()
backup_filename = 'Backup_' + today.strftime('%d-%m-%Y_%H.%M')

language_dict = {
    'RU': {
        'copy': 'Введите путь к папке с файлами:',
        'save': 'Введите путь к конечной папке:',
        'status': 'Введите нужные пути и нажмите "Начать"',
        'end_status': 'Завершено',
        'choose': 'Выбрать',
        'start': 'Начать'
    },

    'EN': {
        'copy': 'Enter path to folder you want save:',
        'save': 'Enter path to folder where you want save:',
        'status': 'Enter the following paths and then press "Start"',
        'end_status': 'Complete',
        'choose': 'Choose',
        'start': 'Start'
    }
}


main_window = tk.Tk()
main_window.title('Backup script by PHoenjx v2.4')
main_window.resizable(False, False)
mainframe = ttk.Frame(main_window)

mainframe.grid(column=0, row=0, sticky='WNES')
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


language = tk.StringVar(value='RU')
copy_path_entry_label_language = tk.StringVar(value=language_dict['EN']['copy'])
save_path_entry_label_language = tk.StringVar(value=language_dict['EN']['save'])
status_label_language = tk.StringVar(value=language_dict['EN']['status'])
end_status_label_language = tk.StringVar(value=language_dict['EN']['end_status'])
choose_buttons_language = tk.StringVar(value=language_dict['EN']['choose'])
start_backup_button_language = tk.StringVar(value=language_dict['EN']['start'])

copy_path = tk.StringVar()
save_path = tk.StringVar()
status = tk.StringVar(value=status_label_language.get())


def language_switch():
    if language.get() == 'RU':
        language.set('EN')
    elif language.get() == 'EN':
        language.set('RU')

    if language.get() == 'RU':
        copy_path_entry_label_language.set(language_dict['EN']['copy'])
        save_path_entry_label_language.set(language_dict['EN']['save'])
        status_label_language.set(language_dict['EN']['status'])
        end_status_label_language.set(language_dict['EN']['end_status'])
        choose_buttons_language.set(language_dict['EN']['choose'])
        start_backup_button_language.set(language_dict['EN']['start'])
    elif language.get() == 'EN':
        copy_path_entry_label_language.set(language_dict['RU']['copy'])
        save_path_entry_label_language.set(language_dict['RU']['save'])
        status_label_language.set(language_dict['RU']['status'])
        end_status_label_language.set(language_dict['RU']['end_status'])
        choose_buttons_language.set(language_dict['RU']['choose'])
        start_backup_button_language.set(language_dict['RU']['start'])

    status.set(status_label_language.get())


def choose_copy_path():
    path = filedialog.askdirectory()
    copy_path.set(path)


def choose_save_path():
    path = filedialog.askdirectory()
    save_path.set(path)


def backup(*args):
    with zipfile.ZipFile(rf'{os.path.join(os.path.abspath(save_path.get()), backup_filename)}.zip', 'w') as \
            backup_archive:
        for root, dirs, files in os.walk(os.path.abspath(copy_path.get())):
            for file in files:
                backup_archive.write(os.path.join(root, file))
    status.set(end_status_label_language.get())


language_switch_button = ttk.Button(mainframe, textvariable=language, width=3, command=language_switch)

ML_icon_label = ttk.Label(mainframe, padding=(0, 0, 15, 0))
ML_icon = ImageTk.PhotoImage(Image.open('Mint Lizard team 2.png'))
ML_icon_label['image'] = ML_icon
ML_label = ttk.Label(mainframe, text='Mint Lizard')


copy_path_entry_label = ttk.Label(mainframe, textvariable=copy_path_entry_label_language)
copy_path_entry = ttk.Entry(mainframe, width=30, textvariable=copy_path)
copy_path_browse_button = ttk.Button(mainframe, textvariable=choose_buttons_language, command=choose_copy_path)

save_path_entry_label = ttk.Label(mainframe, textvariable=save_path_entry_label_language)
save_path_entry = ttk.Entry(mainframe, width=30, textvariable=save_path)
save_path_browse_button = ttk.Button(mainframe, textvariable=choose_buttons_language, command=choose_save_path)

status_label = ttk.Label(mainframe, textvariable=status)
start_backup_button = ttk.Button(mainframe, textvariable=start_backup_button_language, command=backup)


language_switch_button.grid(column=0, row=0, padx=(20, 0), sticky='E')

ML_icon_label.grid(column=1, row=0, sticky='E', rowspan=2)
ML_label.grid(column=1, row=2, padx=20, pady=3, sticky='W, N, E, S')

copy_path_entry_label.grid(column=2, row=0, padx=5, pady=5, sticky='WEN')
copy_path_entry.grid(column=3, row=0, padx=5, pady=5, sticky='EN')
copy_path_browse_button.grid(column=4, row=0, padx=5, pady=5, sticky='EN')

save_path_entry_label.grid(column=2, row=1, padx=5, sticky='WN')
save_path_entry.grid(column=3, row=1, padx=5, sticky='WN')
save_path_browse_button.grid(column=4, row=1, padx=5, sticky='EN')

status_label.grid(column=2, row=2, padx=5, pady=5, sticky='WNS')
start_backup_button.grid(column=3, row=2, padx=5, pady=5, sticky='WEN', columnspan=2)


main_window.bind('<Return>', backup)

main_window.mainloop()
