from tkinter import *

class popupWindow(object):
    def __init__(self,master):
        self.master = master
        top = self.top = Toplevel(master)
        self.l1 = Label(top, text="Please enter your student email address:")
        self.l1.pack()
        self.e1 = Entry(top)
        self.e1.pack()
        self.l2 = Label(top, text="Which Session is this for?")
        self.l2.pack()
        self.e2 = Entry(top)
        self.e2.pack()
        self.b = Button(top, text='Submit',command=self.cleanup)
        self.b.pack()
        self.top.attributes("-topmost", True)

    def cleanup(self):
        self.value_email = self.e1.get()
        self.value_session = self.e2.get()
        self.top.destroy()

class mainWindow(object):
    def __init__(self,master):
        self.master = master
        self.master.geometry("400x400")
        self.master.title("Pre_class_work_selector")
        self.b = Button(master,text="Get Task",command=self.print_course)
        self.b.pack(pady=40)
        self.popup()

    def popup(self):
        if hasattr(self, 'label_warning'):
            self.label_warning.pack_forget()
            self.reopen_popup.pack_forget()
        self.w = popupWindow(self.master)
        self.master.wait_window(self.w.top)

    def print_course(self):
        problem = self.problem_choice(self.w.value_email, self.w.value_session)

        self.label_top = Label(self.master,text='For seminar {}'.format(self.w.value_session)).pack()
        self.label = Label(self.master,text=problem).pack()
        
        '''
        except AttributeError:
            self.label_warning = Label(self.master,text="You need to input your Minerva Email address first!")
            self.label_warning.pack()
            self.reopen_popup = Button(self.master,text="Enter Email",command=self.popup)
            self.reopen_popup.pack()
        '''


root=Tk()
m=mainWindow(root)
root.mainloop()
