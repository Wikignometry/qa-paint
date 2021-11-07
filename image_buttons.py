from  button import *

def makeImageButtons(app):
    buttons = []
    imageButtonActions={'import':getImage,'crop':initiateCrop, 'rotate':rotateImage, 'export':exportImage}

    y = 50
    x = 100
    for label in imageButtonActions:
        buttons.append(Button((50,30), location=(x, y), 
        label=label, fill='light grey', action=imageButtonActions[label]))
        x += 60
    return buttons

def getImage(app):
    filePath = filedialog.askopenfilename(initialfile="import-image", defaultextension=".jpg", )
    if filePath: app.image.importImage(path=filePath)

def initiateCrop(app):
    app.status = 'Crop'

def rotateImage(app):
    app.image.action["rotate"]["ing"] = True


def exportImage(app):
    filePath = filedialog.asksaveasfilename(initialfile="export-image", defaultextension=".jpg",
                                                filetypes=[("ImageFile", ".jpg")])
    if filePath: app.image.exportImage(path=filePath)
