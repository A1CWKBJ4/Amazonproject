import pandas as pd
import xlrd

global data
data= pd.read_excel("C:/Users/LADDUGOPAL/PycharmProjects/AmazonA/Testdata/Registration.xlsx")

class Registration:
    def yourname(self,i):
        return data["Yourname"][i]


    def mobile(self,i):
        return data["Mobile"][i]

    def email(self,i):
        return data["Email"][i]

    def password(self,i):
        return data["Password"][i]


    def rowscount(self):
        return len(data)











