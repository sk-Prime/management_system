import pickle,os
db_name= "management.pdb"
def fresh():
    if not os.path.exists(db_name):
        with open(db_name,'wb') as pdb:
            pickle.dump([{},{}],pdb)

class db_handle(object):
    fresh()
    def __init__(self):
        self.student_data = {}
        self.employee_data = {}

        self.mode = ""
        self.info={}
        self.load_data()
    def load_data(self):
        with open(db_name,'rb') as pdb:
            data = pickle.load(pdb)
            self.student_data= data[0]
            self.employee_data= data[1]

    def write_data(self):
        with open(db_name,'wb') as pdb:
            pickle.dump([self.student_data,self.employee_data],pdb)

    def information(self, info=()):
        self.mode=info[0]
        self.info= info[1]

    def __empty_data(self):
        if "" in self.info or " " in self.info:
            return True
        return False

    def action(self):
        if self.mode=="register_page_employee":
            empty_key=self.__empty_data()
            if empty_key:
                return ("err","Error: Information can not be empty")
            else:
                self.employee_data[self.info[0]]=self.info
                return("ok","Registration Successful")

        elif self.mode=="login_page_employee":
            empty_key=self.__empty_data()
            if empty_key:
                return ("err","Error: Information can not be empty")
            else:
                if self.info[0] in self.employee_data:
                    data = self.employee_data[self.info[0]]
                    if data[2] == self.info[1]:
                        return ("ok","Employee login successful")
                    else:
                        return("err","Wrong Password")
                else:
                    return("err","Login ID does not exist")

        elif self.mode=="register_page_student":
            empty_key=self.__empty_data()

            if empty_key:
                return ("err","Error: Information can not be empty")
            else:
                self.student_data[self.info[0]]=self.info
                return("ok","Registration Successful")

        elif self.mode=="login_page_student":
            empty_key=self.__empty_data()
            if empty_key:
                return ("err","Error: Information can not be empty")
            else:
                if self.info[0] in self.employee_data:
                    data = self.student_data[self.info[0]]
                    if data[2] == self.info[1]:
                        return ("ok","Student login successful")
                    else:
                        return("err","Wrong Password")
                else:
                    return("err","Login ID does not exist")


    def query(self,data=()):
        pass


if __name__ == "__main__":
    dbhandle = db_handle()

