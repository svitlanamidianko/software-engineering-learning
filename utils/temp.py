import hashlib
from tkinter import *

class SessionAssignment:
    def __init__(self):
        self.sessions = {'3.2': ['2 - Logging', 
                                 '3 - Graphics'], 
                        '6.1': ['2 - The Current Weather', 
                                '3 - Crypto Exchange', 
                                '4 - Google directions', 
                                '5 - Flying Aircraft']}
        self.interfaces = {'Terminal' : self.Terminal, 
                           'TKinter' : self.TKinter}
    
    def problem_choice(self, sessions_key, email):
        email = email.strip().lower()
        sessions_key = sessions_key.strip().lower()
        enc = (email + sessions_key).encode()
        md5 = hashlib.md5(enc).hexdigest()
        ind = int(md5, 16) % len(self.sessions[sessions_key])
        return self.sessions[sessions_key][ind]
    
    def Main(self):
        ui_type = input("What interface would you like? I can currently do: {}: ".format(', '.join([*self.interfaces])))
        return self.interfaces[ui_type]()

    def Terminal(self):
        sessions_key = input("What session is this for (sessions supported: {}): ".format(", ".join([*self.sessions])))
        while sessions_key not in self.sessions.keys():
            print("Oops, I don't think we support that session number, would you mind checking you typed it write? You wrote {}.".format(sessions_key))
            sessions_key = input("What session is this for (sessions supported: {}): ".format(", ".join([*self.sessions])))
        
        email = input("Please enter your student email address: ")
        while "@minerva.kgi.edu" not in email:
            print("Oops, I don't think that's a Minervan email address, would you mind checking you typed it write? You wrote {}.".format(email))
            email = input("Please enter your student email address: ")
        
        print("You'll be doing {}.".format(self.problem_choice(sessions_key, email)))

    def TKinter(self):
        pass

if __name__ == '__main__':
    SessionAssignment = SessionAssignment()
    SessionAssignment.Main()


