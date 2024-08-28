from datetime import datetime 





date_format = "%d-%m-%Y"
categories = {"I":'income',"E":"expnese"}



def get_date(prompt,default = False):
    date = input(prompt)
    if default and not date:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date,date_format)
        return valid_date.strftime(date_format)
    except:
        print("Invalid date format, please enter the date in 'dd-mm-yyyy: '")
        return get_date(prompt,default)


def get_amount():
    try:
        amount = float(input("enter the amount: "))
        if amount <=0:
            raise ValueError("Amount must be a non-negative-zero value")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("enter the category I or E for income or expense: ").upper()
    if category in categories:
        return categories[category]
    
    print("""Invalid category, Please enter "I" for income or "E" for expense: """)
    return get_category()
def get_description():
    return input("Enter the description (optional): ")