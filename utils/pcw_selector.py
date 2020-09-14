import hashlib
from tkinter import *
import argparse

class BaseMethod:
    def __init__(self):
        self.sessions = {'3.2': ['2 - Logging',
                                 '3 - Graphics'],
                         '6.2': ['2 - Pokemon',
                                 '3 - Crypto Exchange', 
                                 '4 - What3words',
                                 '5 - Flying Aircraft']}
        self.user_email = ''
        self.sessions_key = ''

    def user_input_output(self):
        '''
        Method for gathering both user email and session user is querying.
        '''
        pass

    def problem_choice(self, sessions_key, email):
        '''
        Method for determining the session given the student's email. This is standard throughout
        all implementations so useful to implement in abstract class.
        '''
        email = self.user_email.strip().lower() #xtra careful
        sessions_key = self.sessions_key.strip().lower() #xtra careful
        enc = (email + sessions_key).encode()
        md5 = hashlib.md5(enc).hexdigest()
        ind = int(md5, 16) % len(self.sessions[sessions_key])
        return self.sessions[sessions_key][ind]

    def run_main_program(self):
        '''
        Function for inherited class specific implementation to work.
        '''
        self.user_input_output()

class Terminal(BaseMethod):
    def __init__(self):
        super().__init__()

    def user_input_output(self):
        self.user_email = input("Please enter your student email address: ")
        while "@minerva.kgi.edu" not in self.user_email:
            print("Oops, I don't think that's a Minervan email address, would you mind checking you typed it write? You wrote {}.".format(self.user_email))
            self.user_email = input("Please enter your student email address: ")

        self.sessions_key = input("What session is this for (sessions supported: {}): ".format(", ".join([*self.sessions])))
        while self.sessions_key not in self.sessions.keys():
            print("Oops, I don't think we support that session number, would you mind checking you typed it write? You wrote {}.".format(self.sessions_key))
            self.sessions_key = input("What session is this for (sessions supported: {}): ".format(", ".join([*self.sessions])))

        print("You'll be doing: {}.".format(self.problem_choice(self.sessions_key, self.user_email)))

class TKinter(BaseMethod):
    def __init__(self):
        super().__init__()

    def user_input_output(self):
        top = Toplevel(self.root)
        label_user_email = Label(top, text="Please enter your student email address:")
        label_user_email.pack()
        entry_user_email = Entry(top)
        entry_user_email.pack()
        label_sessions_key = Label(top, text="Which Session is this for?")
        label_sessions_key.pack()
        entry_sessions_key = Entry(top)
        entry_sessions_key.pack()

        def checker():
            self.user_email = entry_user_email.get()
            self.sessions_key = entry_sessions_key.get()
            if "@minerva.kgi.edu" in self.user_email and self.sessions_key in [*self.sessions]:
                top.destroy()
                display_selection()
            else:
                if "@minerva.kgi.edu" in self.user_email:
                    label_warning = Label(top, text="It looks like you may not have entered a session we currently support!\n Would you mind retyping? As a reminder, you wrote {}.\n We currently only support ({})".format(self.sessions_key, ", ".join([*self.sessions])))
                else:
                    label_warning = Label(top, text="Would you mind checking you entered a minerva address?\n As a reminder, you wrote {}.".format(self.user_email))

                label_warning.pack()

                if hasattr(self.root, 'label_warning'):
                    self.user_input()

        b = Button(top, text='Submit', command=checker)
        b.pack()
        top.attributes("-topmost", True)

        def display_selection():
            self.root.title("Pre-Class Work Select")
            self.root.geometry("300x100")
            Label(self.root, text='For seminar {}'.format(self.sessions_key)).pack()
            Label(self.root, text=self.problem_choice(self.sessions_key, self.user_email)).pack()

    def run_main_program(self):
        self.root = Tk()
        self.user_input_output()
        self.root.mainloop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='UI Controller')

    parser.add_argument('UI', action='store', default=Terminal)

    args = parser.parse_args()

    methods = {
        'TKinter' : TKinter(),
        'Terminal' : Terminal()
    }

    try:
        methods[vars(args)['UI']].run_main_program()
    except KeyError:
        print("Oops, I don't recognize that UI. Want to implement it?")
