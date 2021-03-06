from button import *

def makeOvalButtons(app):
    buttons = []
    ovalButtonActions={'thickness':getOvalThickness, 'color':getOvalFill, 'outline':getOvalOutline}

    y = 30
    x = 100
    for label in ovalButtonActions:
        buttons.append(Button((80,30), location=(x, y), 
        label=label, fill='powder blue', action=ovalButtonActions[label]))
        x += 90
    return buttons


def makeAutoOvalValues(app):
    app.ovalThickness = 3
    app.ovalFill = ''
    app.ovalOutline = 'black'

def getOvalThickness(app):
    thickness = (app.getUserInput('input your oval thickness here'))
    if thickness != None:
        app.ovalThickness = int(thickness)

def getOvalFill(app):
    app.ovalFill = app.getUserInput('input your oval color here')

def getOvalOutline(app):
    app.ovalOutline = app.getUserInput('input your oval outline color here')