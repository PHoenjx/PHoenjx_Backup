from PIL import ImageTk, Image
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import zipfile
import datetime
import os


today = datetime.datetime.today()
backup_filename = 'Backup_' + today.strftime('%d-%m-%Y_%H.%M')


def choose_copy_path():
    path = filedialog.askdirectory()
    copy_path.set(path)


def choose_save_path():
    path = filedialog.askdirectory()
    save_path.set(path)


main_window = tk.Tk()
main_window.title('Backup script by PHoenjx v2.0')
mainframe = ttk.Frame(main_window)

mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


copy_path = tk.StringVar()
save_path = tk.StringVar()
status = tk.StringVar(value='Введите нужные пути и нажмите "Начать"')


def backup(*args):
    with zipfile.ZipFile(rf'{os.path.abspath(save_path.get())}\{backup_filename}.zip', 'w') as backup_archive:
        for root, dirs, files in os.walk(os.path.abspath(copy_path.get())):
            for file in files:
                backup_archive.write(os.path.join(root, file))
    status.set('Завершено')


ML_icon_label = ttk.Label(mainframe)
image = Image.open('Mint Lizard team 2.png')
ML_icon = ImageTk.PhotoImage(image)
ML_icon_label['image'] = ML_icon
ML_label = ttk.Label(mainframe, text='Mint Lizard')


copy_path_entry_label = ttk.Label(mainframe, text='Введите путь к папке с файлами:')
copy_path_entry = ttk.Entry(mainframe, width=30, textvariable=copy_path)
copy_path_browse_button = ttk.Button(mainframe, text='Выбрать', command=choose_copy_path)

save_path_entry_label = ttk.Label(mainframe, text='Введите путь к конечной папке:')
save_path_entry = ttk.Entry(mainframe, width=30, textvariable=save_path)
save_path_browse_button = ttk.Button(mainframe, text='Выбрать', command=choose_save_path)

status_label = ttk.Label(mainframe, textvariable=status)
start_backup_button = ttk.Button(mainframe, text='Начать', command=backup)

ML_icon_label.grid(column=0, row=0, padx=20, sticky='WENS', rowspan=2)
ML_label.grid(column=0, row=2, padx=20, pady=3, sticky='W, N, E, S')

copy_path_entry_label.grid(column=1, row=0, padx=5, pady=5, sticky='WEN')
copy_path_entry.grid(column=2, row=0, padx=5, pady=5, sticky='EN')
copy_path_browse_button.grid(column=3, row=0, padx=5, pady=5, sticky='EN')

save_path_entry_label.grid(column=1, row=1, padx=5, sticky='WN')
save_path_entry.grid(column=2, row=1, padx=5, sticky='WN')
save_path_browse_button.grid(column=3, row=1, padx=5, sticky='EN')

status_label.grid(column=1, row=2, padx=5, pady=5, sticky='WNS')
start_backup_button.grid(column=2, row=2, padx=5, pady=5, sticky='WEN', columnspan=2)

main_window.bind('<Return>', backup)

main_window.mainloop()
