from PIL import Image, ImageTk
from pickle_data import db_handle
from tkinter import messagebox
from tkinter import ttk

import random
import tkinter

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
        self.id_length = 5
        self.selected_id=""
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

    def admin_page(self):
        self.entry_holder=[]
        self.current_frame.destroy()

        bg = "khaki"
        btnbg="black"
        font = "Arial 15"

        self.frame_ap = tkinter.Frame(self.root)
        self.frame_ap.config(bg=bg)

        banner_text = tkinter.Button(self.frame_ap, width=40, text=" Administration ",relief="flat",state="disabled",disabledforeground="black")
        banner_text.config(font=font)
        banner_text.pack(padx=10,pady=20)

        self.frame_btn = tkinter.Frame(self.frame_ap, bg=bg)

        self.delete_btn = tkinter.Button(self.frame_btn, text="edit", font= font,command=self.__edit)
        self.delete_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
        self.delete_btn.pack(side="left",padx=10,fill='x')

        self.delete_btn = tkinter.Button(self.frame_btn, text="Delete", font= font,command=self.__tree_del)
        self.delete_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
        self.delete_btn.pack(side="left",padx=10,fill='x')

        self.back_btn = tkinter.Button(self.frame_btn, text="log out", font= font,command = self.front_page)
        self.back_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
        self.back_btn.pack(side="right",fill='x',padx=10)

        self.frame_btn.pack(side="bottom",pady=20)
        self.frame_ap.pack(fill="both", expand=True)
        self.current_frame=self.frame_ap
        self.mode = "admin_page"

        self.treeview= ttk.Treeview(self.frame_ap,height=18,columns=("Name","Value"))
        self.treeview.pack(fill="both")

        self.treeview.tag_configure("blue",background="blue")
        self.treeview.tag_configure("green",background="green")
        self.treeview.bind("<<TreeviewSelect>>",self.__tree_del)

        self.treeview.column('#0',width=40,stretch=0)
        self.treeview.heading('#1',text="Heading")
        self.treeview.heading('#2',text="Value")
        self.treeview.insert('','end','emp',values=('Employee',),tag="blue")
        self.treeview.insert('','end','std',values=('Student',),tag="green")
        self.__tree_update()

    def editor_top(self,t,values):
        entry_holder = []
        self.top = tkinter.Toplevel(self.root)
        def cancel_cmd():
            self.top.destroy()
            return False
        def update_command():
            values=[]
            for e in entry_holder:
                values.append(e.get())
            if values:
                self.database.delete(self.selected_id)
                self.database.add(self.selected_id,values,t)
                messagebox.showinfo("Success","%s updated successfuly"%self.selected_id)
                self.current_frame.destroy()
                self.admin_page()
            else:
                messagebox.showerror("Error","Something went wrong to update %s"%self.selected_id)
            self.top.destroy()

        self.top.title("Editor")
        self.frametop=tkinter.Frame(self.top)
        self.frametop.pack()

        if t==1:
            labels= self.employee_regText
        else:
            labels = self.student_regText

        for i, label in enumerate(labels):
            label_tk =tkinter.Label(self.frametop,text="%-20s %s"%(label,":"),font="consolas 12")
            entry_tk = tkinter.Entry(self.frametop,width = 20,font="consolas 12")
            label_tk.grid(row=i,sticky="nw",pady=0)
            entry_tk.grid(row=i,column=1,padx=2,pady=6)
            entry_tk.insert(0,values[i])
            entry_holder.append(entry_tk)

        update= tkinter.Button(self.top, text="update",command=update_command)
        update.config(width = 25)
        update.pack(side="left",padx=10,pady=2,fill='x')

        cancel = tkinter.Button(self.top, text="Cancel",command=cancel_cmd)
        cancel.config(width = 25)
        cancel.pack(side="left",padx=10,pady=2,fill='x')

    def student_view(self):
        self.current_frame.destroy()

        bg = "light sea green"
        btnbg="black"
        font = "Arial 15"
        empc,stdc= self.database.count()
        self.frame_sp = tkinter.Frame(self.root)
        self.frame_sp.config(bg=bg)

        banner_text = tkinter.Button(self.frame_sp, width=40, text=" Information ",relief="flat",state="disabled",disabledforeground="black")
        banner_text.config(font=font)
        banner_text.pack(padx=10,pady=20)

        banner_text2 = tkinter.Button(self.frame_sp, width=40, text="Number of Employee: %d "%empc,relief="flat",state="disabled",disabledforeground="black")
        banner_text2.config(font=font)
        banner_text2.pack(padx=10,pady=20)

        banner_text3 = tkinter.Button(self.frame_sp, width=40, text="Number of student: %d "%stdc,relief="flat",state="disabled",disabledforeground="black")
        banner_text3.config(font=font)
        banner_text3.pack(padx=10,pady=20)

        self.back_btn = tkinter.Button(self.frame_sp, text="log out", font= font,command = self.front_page)
        self.back_btn.config(width = 10, bg=btnbg, fg="white", relief = "flat")
        self.back_btn.pack(side="right",fill='x',padx=10)


        self.frame_sp.pack(fill="both", expand=True)
        self.current_frame=self.frame_sp
        self.mode = "student_view"

    def __tree_update(self,mode=0):
        employee, student = self.database.query()
        if mode==0:
            for emp in employee:
                data=employee[emp]
                self.treeview.insert('emp','end',emp,values=("  "+emp,''))
                for i,d in enumerate(data):
                    self.treeview.insert(emp,'end',values=("    "+self.employee_regText[i],d))

            for emp in student:
                data=student[emp]
                self.treeview.insert('std','end',emp,values=("  "+emp,''))
                for i,d in enumerate(data):
                    self.treeview.insert(emp,'end',values=("    "+self.student_regText[i],d))

        elif mode==1:
            pass
        #need to implement

    def __tree_del(self,e=0):
        if e==0:
            if self.selected_id:
                result = messagebox.askyesno("Delete","Would you like to delete id : %s ?"%self.selected_id)
                if result:
                    value=self.database.delete(self.selected_id)
                    if value:
                        messagebox.showinfo("Success","%s has deleted"%self.selected_id)
                        for i in self.treeview.get_children(self.selected_id):
                            self.treeview.delete(i)
                        self.treeview.delete(self.selected_id)
                        self.selected_id=''
                    else:
                        messagebox.showerror("Error","Something went wrong")
                else:
                    pass
            else:
                messagebox.showwarning("Error","No id Selected")
        else:
            data=self.treeview.item(self.treeview.focus())['values'][0]
            print(data)
            if data[:2]=="  " and data[2]!=" ":
                self.selected_id=data[2:]

    def __edit(self):
        data=False
        if self.selected_id:
            data = self.database.query(self.selected_id)
        if data:
            t,data=data
            self.editor_top(t,data)
        else:
            messagebox.showerror("Error","No id Selected")


    #-----------------------gui end-----------------------------------------------------------

    def auto_id(self):
        charset = "asdfghjklzxcvbnmqwertyuiop123456789"
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
            if check[1] == "admin":
                self.admin_page()
            elif mode=="login_page_student":
                self.student_view()
            else:
                messagebox.showinfo("Success",check[1])

    def on_exit_event(self,event=0):
        self.database.write_data()
        self.root.destroy()


if __name__ == "__main__":
    root = tkinter.Tk()
    ui = gui(root)
    ui.mainloop()
