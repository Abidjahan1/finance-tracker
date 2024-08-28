import pandas as pd
import csv
from datetime import datetime
from data_insert import *


class Csv:
    CSV_FILE = "finance.csv"
    COLUMNS = ['date','amount','category','description']
    
    
    @classmethod
    def initialze_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE,index=False)

    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry = {
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }
        with open(cls.CSV_FILE,"a",newline="")as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
            print("Data Insert Successfully")
    
def add():
    Csv.initialze_csv()
    date = get_date("Enter the date of the transaction(dd-mm-yyyy) or enter for today's date",default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    Csv.add_entry(date,amount,category,description)




add()