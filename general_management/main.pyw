from PIL import Image, ImageTk
from pickle_data import db_handle
from tkinter import messagebox
import tkinter, random


class gui(tkinter.Frame):
    def __init__(self, root,**kwag):
        tkinter.Frame.__init__(self,root,**kwag)
        self.root = root
        self.root.title("Management System")
        self.root.minsize(450,550)
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit_event)
        self.current_frame = tkinter.Frame(self.root)
        self.front_page()
        self.mode = ""

        self.student_regText = ["Student ID","Name","Password","Department","Semester","Batch"]
        self.student_logText = ["Student ID","Password"]
        self.employee_regText = ["Emp ID","Name","Password","Department","Date of join","Salary"]

        self.employee_logText = ["Emp ID","Password"]
        self.entry_holder=[]

        self.database= db_handle()

        self.id_auto = 1
        self.id_length = 3
#-------------------gui------------------------------------------------------------
    def front_page(self):
        self.current_frame.destroy()
        bg = "white"
        btnbg="black"
        font = "Arial 15"

        self.frame_fp = tkinter.Frame(self.root)
        self.frame_fp.config(bg=bg)

        banner_text = tkinter.Button(self.frame_fp, width=40, text=" Welcome to Management system ",relief="flat",state="disabled",disabledforeground="black")
        banner_text.config(font=font)
        banner_text.pack(padx=10,pady=20)

        self.frame_btn = tkinter.Frame(self.frame_fp, bg=bg)
        self.employee_btn = tkinter.Button(self.frame_btn, text="Employee", font= font,command= self.employee_page)
        self.employee_btn.config(width= 10, bg=btnbg, fg="white", relief = "flat")
        self.employee_btn.pack(side="left",padx=10,fill='x')

        self.student_btn = tkinter.Button(self.frame_btn, text="Student", font= font,command=self.student_page)
        self.student_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
        self.student_btn.pack(side="left",padx=10,fill='x')

        self.image_file = ImageTk.PhotoImage(Image.open('image.jpg'))
        self.image = tkinter.Label(self.frame_fp, image=self.image_file)
        self.image.pack()

        self.exit_btn = tkinter.Button(self.frame_btn, text="exit", font= font,command = self.on_exit_event)
        self.exit_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
        self.exit_btn.pack(side="right",padx=10,fill='x')

        self.frame_btn.pack(side="bottom",pady=20)
        self.frame_fp.pack(fill="both", expand=True)
        self.current_frame= self.frame_fp
        self.mode = "front_page"

    def employee_page(self):
        self.current_frame.destroy()

        bg = "seagreen"
        btnbg="black"
        font = "Arial 15"

        self.frame_ep = tkinter.Frame(self.root)
        self.frame_ep.config(bg=bg)

        banner_text = tkinter.Button(self.frame_ep, width=40, text=" Employee ",relief="flat",state="disabled",disabledforeground="black")
        banner_text.config(font=font)
        banner_text.pack(padx=10,pady=20)

        self.frame_btn = tkinter.Frame(self.frame_ep, bg=bg)
        self.register_btn = tkinter.Button(self.frame_btn, text="Register", font= font,command= self.register_page)
        self.register_btn.config(width= 10, bg=btnbg, fg="white", relief = "flat")
        self.register_btn.pack(side="left",padx=10,fill='x')

        self.login_btn = tkinter.Button(self.frame_btn, text="Login", font= font,command=self.login_page)
        self.login_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
        self.login_btn.pack(side="left",padx=10,fill='x')

        self.back_btn = tkinter.Button(self.frame_btn, text="back", font= font,command = self.front_page)
        self.back_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
        self.back_btn.pack(side="right",fill='x',padx=10)

        self.image_file = ImageTk.PhotoImage(Image.open('image.jpg'))
        self.image = tkinter.Label(self.frame_ep, image=self.image_file)
        self.image.pack()

        self.frame_btn.pack(side="bottom",pady=20)
        self.frame_ep.pack(fill="both", expand=True)
        self.current_frame=self.frame_ep
        self.mode = "employee_page"

    def student_page(self):
        self.current_frame.destroy()

        bg = "light sea green"
        btnbg="black"
        font = "Arial 15"

        self.frame_sp = tkinter.Frame(self.root)
        self.frame_sp.config(bg=bg)

        banner_text = tkinter.Button(self.frame_sp, width=40, text=" Student ",relief="flat",state="disabled",disabledforeground="black")
        banner_text.config(font=font)
        banner_text.pack(padx=10,pady=20)

        self.frame_btn = tkinter.Frame(self.frame_sp, bg=bg)
        self.register_btn = tkinter.Button(self.frame_btn, text="Register", font= font,command= self.register_page)
        self.register_btn.config(width= 10, bg=btnbg, fg="white", relief = "flat")
        self.register_btn.pack(side="left",fill="x",padx=10)

        self.login_btn = tkinter.Button(self.frame_btn, text="Login", font= font,command=self.login_page)
        self.login_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
        self.login_btn.pack(side="left",fill="x",padx=10)

        self.back_btn = tkinter.Button(self.frame_btn, text="back", font= font,command = self.front_page)
        self.back_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
        self.back_btn.pack(side="right",fill='x',padx=10)

        self.image_file = ImageTk.PhotoImage(Image.open('image.jpg'))
        self.image = tkinter.Label(self.frame_sp, image=self.image_file)
        self.image.pack()

        self.frame_btn.pack(side="bottom",pady=20)
        self.frame_sp.pack(fill="both", expand=True)
        self.current_frame=self.frame_sp
        self.mode = "student_page"

    def register_page(self):
        self.entry_holder=[]
        self.current_frame.destroy()

        bg = "#044f67"
        btnbg="black"
        font = "Arial 15"
        fontInfo = "consolas 12"
        text=""
        labels=[]
        if self.mode == "student_page":
            text=" Student Register "
            labels = self.student_regText
            self.mode = "register_page_student"
        elif self.mode == "employee_page":
            text=" Employee Register "
            labels = self.employee_regText
            self.mode = "register_page_employee"

        self.frame_rp = tkinter.Frame(self.root)
        self.frame_rp.config(bg=bg)

        self.frame_entry = tkinter.LabelFrame(self.frame_rp, font=fontInfo, fg="gold", text= "Insert Information")
        self.frame_entry.config(bg=bg)

        banner_text = tkinter.Button(self.frame_rp, width=40, text=text,relief="flat",state="disabled",disabledforeground="black")
        banner_text.config(font=font)
        banner_text.pack(padx=10,pady=20)

        self.frame_btn = tkinter.Frame(self.frame_rp, bg=bg)
        self.submit_btn = tkinter.Button(self.frame_btn, text="Submit", font= font,command=self.submit_btn_cmnd)
        self.submit_btn.config(width= 10, bg=btnbg, fg="white", relief = "flat")
        self.submit_btn.pack(side="left",padx=10,fill='x')

##        self.update_btn = tkinter.Button(self.frame_btn, text="Update", font= font)
##        self.update_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
##        self.update_btn.pack(side="left",padx=10,fill='x')

        self.back_btn = tkinter.Button(self.frame_btn, text="back", font= font,command = self.front_page)
        self.back_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
        self.back_btn.pack(side="right",padx=10,fill='x')

        for i, label in enumerate(labels):
            label_tk =tkinter.Label(self.frame_entry,text="%-20s %s"%(label,":"),bg=bg,font=fontInfo,fg="white")
            entry_tk = tkinter.Entry(self.frame_entry,width = 20, font=fontInfo)
            label_tk.grid(row=i,sticky="nw",pady=0)
            entry_tk.grid(row=i,column=1,padx=2,pady=6)
            self.entry_holder.append(entry_tk)

        if self.id_auto:
            self.entry_holder[0].insert(0,self.auto_id())

        self.frame_entry.pack(expand=True)
        self.frame_btn.pack(pady=20)
        self.frame_rp.pack(fill="both", expand=True)
        self.current_frame=self.frame_rp

    def login_page(self):
        self.entry_holder=[]
        self.current_frame.destroy()

        bg = "#044f67"
        btnbg="black"
        font = "Arial 15"
        fontInfo = "consolas 12"
        text=""
        labels=[]
        if self.mode == "student_page":
            text=" Student Login "
            labels = self.student_logText
            self.mode = "login_page_student"
        elif self.mode == "employee_page":
            text=" Employee Login "
            labels = self.employee_logText
            self.mode = "login_page_employee"

        self.frame_lp = tkinter.Frame(self.root)
        self.frame_lp.config(bg=bg)

        self.frame_entry = tkinter.LabelFrame(self.frame_lp, font=fontInfo, fg="gold", text= "Insert Information")
        self.frame_entry.config(bg=bg)

        banner_text = tkinter.Button(self.frame_lp, width=40, text=text, relief="flat",state="disabled",disabledforeground="black")
        banner_text.config(font=font)
        banner_text.pack(padx=10,pady=20)

        self.frame_btn = tkinter.Frame(self.frame_lp, bg=bg)
        self.submit_btn = tkinter.Button(self.frame_btn, text="Submit", font= font,command=self.submit_btn_cmnd)
        self.submit_btn.config(width= 10, bg=btnbg, fg="white", relief = "flat")
        self.submit_btn.pack(side="left",padx=10,fill='x')

        self.back_btn = tkinter.Button(self.frame_btn, text="back", font= font,command = self.front_page)
        self.back_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
        self.back_btn.pack(side="right",padx=10,fill='x')


        for i, label in enumerate(labels):
            label_tk =tkinter.Label(self.frame_entry,text="%-20s %s"%(label,":"),bg=bg,font=fontInfo,fg="white")
            entry_tk = tkinter.Entry(self.frame_entry,width = 20, font=fontInfo)
            label_tk.grid(row=i,sticky="nw",pady=0)
            entry_tk.grid(row=i,column=1,padx=2,pady=6)
            self.entry_holder.append(entry_tk)
        self.frame_entry.pack(expand=True)
        self.frame_btn.pack(pady=20)
        self.frame_lp.pack(fill="both", expand=True)
        self.current_frame=self.frame_lp

    #-----------------------gui end-----------------------------------------------------------

    def auto_id(self):
        charset = "asdfghjklzxcvbnmqwertyuiop1234567890"
        l= len(charset)
        holder = ""
        for i in range(self.id_length):
            holder+= charset[random.randint(0,l-1)]
        return holder

    #------------------------gui button callbacks-----------------------------------------

    def submit_btn_cmnd(self):
        mode= self.mode
        if mode == "register_page_employee":
            key = self.employee_regText
        elif mode == "register_page_student":
            key = self.student_regText
        elif mode == "login_page_employee":
            key = self.employee_logText
        elif mode == "login_page_student":
            key = self.student_logText
        entry_data=[]
        for i,entry in enumerate(self.entry_holder):
            entry_data.append(entry.get())
        #print(mode,entry_data)
        self.database.information((mode,entry_data))
        check= self.database.action()
        if check[0]=="err":
            messagebox.showerror("Error", check[1])
        else:
            messagebox.showinfo("Success",check[1])

    def on_exit_event(self,event=0):
        self.database.write_data()
        self.root.destroy()


if __name__ == "__main__":
    root = tkinter.Tk()
    ui = gui(root)
    ui.mainloop()