import sys
def start(self):
    import win32com.client as win
    import datetime
    ##GROUPS
    STAFF = ['Name List']


    #Cnnectection
    outlook = win.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder("6")


    #### FOLDERS
    STAFF_FOLDER = inbox.Folders['Staff']
    UNKNOWN_FOLDER = inbox.Folders['Unknown']
    ZOOM_FOLDER = inbox.Folders['Zoom']

    messages = inbox.Items
    message = messages.GetFirst()
    for message in list(messages):
        if(message.SenderName in STAFF):
            print(f"Message received from Staff member: {message.SenderName}")
            message.Move(STAFF_FOLDER)
            print(f"Message has moves to {STAFF_FOLDER}")
        elif (message.SenderName == 'Zoom'):
            print("Message received from Zoom:")
            message.Move(ZOOM_FOLDER)
            print(f"Message has moves to {ZOOM_FOLDER}")
        else:
            print("Message received from UNKNOWN:")
            message.Move(UNKNOWN_FOLDER)
            print(f"Message has moves to {UNKNOWN_FOLDER}")


if __name__ == "__main__":
    start(sys.argv[0])