from button import *

def makeToolButtons(app):
    buttons = []
    textButtonActions = {'line': initiateLine, 
                         'pen': initiatePen,
                        'polygon': initiatePolygon, 
                        'oval': initiateOval,
                        'image': initiateImage,
                        'drag': initiateDrag,
                        'text': initiateText,
                        'undo': initiateUndo}
    y = 100
    x = 30
    for label in textButtonActions:
        buttons.append(Button((50,30), location=(x, y), label=label, fill='light grey', action=textButtonActions[label]))
        y += 40
    return buttons

def initiateLine(app):
    app.status = 'Line'

def initiatePen(app):
    app.status = 'Pen'

def initiatePolygon(app):
    app.status = 'Polygon'

def initiateOval(app):
    app.status = 'Oval'

def initiateImage(app):
    app.status = 'Image'

def initiateDrag(app):
    app.status = 'Drag'

def initiateText(app):
    app.status = 'Text'

def initiateUndo(app):
    undo(app)

def undo(app):
    if app.objects == []:
        return
    app.objects.pop()
    
################################################################################
#               test functions

# def appStarted(app):
#     makeToolButtons(app)
#     app.objects = [ ]

# def mousePressed(app, event):
#     for button in app.buttons:
#         if button.isPressed(event.x, event.y):
#             button.action(app)

# def redrawAll(app, canvas):
#     for button in app.buttons:
#         button.draw(canvas)
#     for object in app.objects:
#         object.draw(canvas)


# runApp(width=500, height=500)