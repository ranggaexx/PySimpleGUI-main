import PySimpleGUI as sg
sg.theme("DarkGreen4")  
sg.theme_text_color ("#FFFF00")
window = sg.Window(title ="Profile", 
                layout =   [[sg.Text("SELAMAT DATANG DI KELAS",
                                        font=("Arial",25))],
                                [sg.Text("NPM       : 2210010638")],
                                [sg.Text("NAMA      : M.Rangga Maulana")],
                                [sg.Text("Kelas     : 5M Reguler Banjarmasin")]
                                ],
                size=(400,200),
                font=("Times", 18))
window()
window.close()