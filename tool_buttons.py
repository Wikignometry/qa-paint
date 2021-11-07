from button import *

def makeToolButtons(app):
    app.toolButtons = []
    textButtonActions = {'line': initiateLine, 
                        'polygon': initiatePolygon, 
                        'oval': initiateOval,
                        'crop': initiateCrop,
                        'drag': initiateDrag,
                        'text': initiateText}
    y = 100
    x = 30
    for label in [ 'line', 'polygon', 'oval', 'crop', 'drag', 'text']:
        app.toolButtons.append(Button((50,30), location=(x, y), label=label, fill='light grey', action=textButtonActions[label]))
        y += 40

def initiateLine(app):
    app.status = 'Line'

def initiatePolygon(app):
    app.status = 'Polygon'

def initiateOval(app):
    app.status = 'Oval'

def initiateCrop(app):
    app.status = 'Crop'

def initiateDrag(app):
    app.status = 'Drag'

def initiateText(app):
    app.status = 'Text'

################################################################################
#               test functions

def appStarted(app):
    makeToolButtons(app)
    app.objects = [ ]

def mousePressed(app, event):
    for button in app.toolButtons:
        if button.isPressed(event.x, event.y):
            button.action(app)

def redrawAll(app, canvas):
    for button in app.toolButtons:
        button.draw(canvas)
    for object in app.objects:
        object.draw(canvas)


runApp(width=500, height=500)