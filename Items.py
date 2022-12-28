import DB

class Items():
    @staticmethod
    def GetAllItems(id=None):
        Condition = ''
        if id != None:
            Condition = "and itmID = " + id
        query = f"select * from Items where  Itmstate ='1'{Condition} order by itmName"

        return list(DB.DBActions.GetRecords(query))

    def __init__(self, id:int = None) -> None:
        self.id = id
        self.itmName = ''
        self.itmPrice=0
        

        if id != None:
            s = Items.GetAllItems(id)
            if len(s) == 0:
                raise Exception("Item not found")
            s = s[0]
            self.itmName = s[1]
            self.itmPrice=s[2]
            

    def Saveitm(self):
        if self.id == None:
            DB.DBActions.GetRecords(f"insert into Items (itmName ,itmprice,Itmstate) Values('{self.itmName}','{self.itmPrice}','1')")
        else:
            DB.DBActions.GetRecords(f"update Items set itmName ='{self.itmName}' , itmprice='{self.itmPrice}' where itmID = ('{self.id}')")


    def Deleteitm (self):
        if self.id!= None:
              DB.DBActions.GetRecords(f"update Items set Itmstate ='0'  where itmID = ('{self.id}')")