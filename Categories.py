import DB

class Categories():
    @staticmethod
    def GetAllCategories(id=None):
        Condition = ''
        if id != None:
            Condition = " and ctgID = " + id
        query = f"select * from Categories where  Ctgstate ='1'{Condition}  order by ctgName "

        return list(DB.DBActions.GetRecords(query))

    def __init__(self, id:int = None) -> None:
        self.id = id
        self.Name = ''
        

        if id != None:
            s = Categories.GetAllCategories(id)
            if len(s) == 0:
                raise Exception("Category not found")
            s = s[0]
            self.Name = s[1]
            

    def Save(self):
        if self.id == None:
            DB.DBActions.GetRecords(f"insert into Categories (ctgName,Ctgstate) Values('{self.Name}','1')")
        else:
            DB.DBActions.GetRecords(f"update Categories set ctgName ='{self.Name}'  where ctgID = ('{self.id}')")


    def Deletectg (self):
        if self.id!= None:
              DB.DBActions.GetRecords(f"update Categories set Ctgstate ='0'  where ctgID = ('{self.id}')")