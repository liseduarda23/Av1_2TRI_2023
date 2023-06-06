import PySimpleGUI as sg

sg.theme("SystemDefaultForReal")

layout = [
  [sg.Push(), sg.Text("Indice de massa corpórea"), sg.Push()],
  [sg.Text("Massa: "),sg.Input(key="-MASS-",size=(30, 1))],
  [sg.Text("Altura: "),sg.Input(key="-HEIGHT-",size=(30, 1))],
  [sg.Push(), sg.Button("Calcular"), sg.Push()],
]
  
window = sg.Window("IMC", layout = layout, font="Monaco 18")
  
while True:
  event, value = window.read()
  print(event, value)
  massa = float(value["-MASS-"])
  altura = float(value["-HEIGHT-"])
  imc = massa / (altura ** 2)
  sg. Popup( f"Seu imc é{imc: .2f}", font="26")
  if event == "Quit" or event == sg.WIN_CLOSED:
    break
