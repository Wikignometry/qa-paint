from button import *

def makeImageButtons(app):
    buttons = []
    imageButtonActions={'import':getImage,'crop':initiateCrop, 
                        'rotate':rotateImage, 'export':exportImage,
                        'brightness': initiateBrightness}

    y = 30
    x = 100
    for label in imageButtonActions:
        buttons.append(Button((80,30), location=(x, y), 
        label=label, fill='powder blue', action=imageButtonActions[label]))
        x += 90
    # buttons.append(Button((50,30), location=(30, 420), 
    #     label='redo', fill='light grey', action=redoImage))
    return buttons

# def redoImage(app):
#     app.image.redo()

def getImage(app):
    filePath = filedialog.askopenfilename(initialfile="import-image", defaultextension=".jpg", )
    if filePath: app.image.importImage(app, path=filePath)

def initiateCrop(app):
    app.status = 'Crop'

def rotateImage(app):
    app.image.action["rotate"]["ing"] = True

def initiateBrightness(app):
    app.image.action["brightness"]["ing"] = True

def exportImage(app):
    filePath = filedialog.asksaveasfilename(initialfile="export-image", defaultextension=".jpg",
                                                filetypes=[("ImageFile", ".jpg")])
    if filePath: app.image.exportImage(app, path=filePath)

