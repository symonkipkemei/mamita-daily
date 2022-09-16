from ast import Str
import csv
from datetime import date


# the timestamp id
def time_id():
    """the following function records the year/month/day/hour/minute/seconds
    and uses it as a key in a database"""
    from datetime import datetime

    now = datetime.now()
    time_key = now.strftime("%Y%m%d%H%M%S")
    return time_key


# Date of Transaction

def date_of_transaction() -> date:
    """generate the date object at time of the recording

    Returns:
        date: date of transaction
    """


    global current_date
    from datetime import date
    print("Insert \n"
          "1) Today's date\n"
          "2) Custom date")

    user_option = int(input("insert: "))

    if user_option == 1:
        current_date = date.today()

    elif user_option == 2:
        custom_date = int(input("date:"))
        custom_month = int(input("month:"))
        custom_year = int(input("year:"))

        current_date = date(custom_year, custom_month, custom_date)
    return current_date

# Inserting options 


def project_configuration(filetype: str, filename:csv):
    """Modify the project parameters in the project set up, by allowing you to add or remove the individual items

    Args:
        filetype (str): name of the csv files
        filename (csv): The csv file
    """
    

    global user_index, user_item
    import csv

    # Look at what is available first
    with open(filetype, "r") as f:
        iterable = csv.reader(f)
        dd_iterable = list(iterable)
        index_list = []
        source_list = []
        # store the index and the category
        for item in dd_iterable:
            index_list.append(item[0])
            source_list.append(item[1])

    print(f"\n*****modify {filename}****\n"
          f"1). Add \n"
          f"2). Delete")

    user_selection = int(input("option : "))

    if user_selection == 1:
        print(f"\n*****adding {filename}****")
        # check if index is already used
        try_again_index = True
        while try_again_index:
            user_index = str(input(f"insert index:"))
            if user_index in index_list:
                print(f"{user_index} already used, try another.")
            # it should be a digit
            elif not user_index.isdigit():
                print(f"{user_index} is not a digit, try again.")
            # 0 is already used
            elif user_index == str(0):
                print("0 already used, try another.")

            # test passed , user_index released for use
            else:
                try_again_index = False

        # check if category already used
        try_again_category = True
        # subjecting the user category to test
        while try_again_category:
            user_item = str.upper(input(f"insert item:"))
            if user_item in source_list:
                print(f"{user_item} already used, try again.")
            else:
                print(f"{user_item} recorded")
                try_again_category = False

        # store data
        data = str(user_index) + "," + str(user_item) + "\n"
        with open(filetype, "a") as f:
            f.write(data)

    elif user_selection == 2:
        print(f"\n*****deleting {filename} ****")
        delete_index = int(input("insert index: "))
        tmp_list = []

        # isolating the identified item (death by isolation)
        for x in dd_iterable:
            if delete_index == int(x[0]):
                print(f"{x[1]} deleted")
            else:
                tmp_list.append(x)

        # empty the csv file , anticipating the new kids in town
        f = open(filetype, "w")
        f.close()

        # overriding the csv with the new generation
        for y in tmp_list:
            data = str(y[0]) + "," + str(y[1]) + "\n"
            with open(filetype, "a") as f:
                f.write(data)
    else:
        print("Wrong input, Try again")

def project_setup(filetype: csv, filename: str):
    """It allows the user to select one of the items listed among options set by the user,


    Args:
        filetype (csv): Th name of the csv files
        filename (name): The csv file

    Returns:
        str: Item selected by the user
    """

    
    restart = True
    while restart :
        try:
            global purpose
            import csv

            # announce what we are doing here

            file_type_upper = str.upper(filename)

            try_again = True
            while try_again:
                category_dict = {}
                with open(filetype, "r") as f:
                    print(f"\n****{file_type_upper}*****")
                    iterable = csv.reader(f)
                    list_iterable = list(iterable)
                    for x in list_iterable:
                        print(f"{x[0]}. {x[1]}")
                        category_dict[int(x[0])] = x[1]
                    print("0. (modify list)")
                user_selection = int(input("Insert option above: "))

                for x in category_dict:
                    if user_selection == x:
                        purpose = category_dict[x]
                        try_again = False
                        return purpose
                if user_selection == 0:
                    project_configuration(filetype, filename)

                restart = False

        except FileNotFoundError:
            f = open(filetype, "w")
            f.close()
            restart = True


def transaction_amount()-> float:
    """Input the amount transacted by the user

    Returns:
        float: Amount
    """

    while True:
        amount = input("Insert amount: ")
        if amount.isdigit():
            amount = float(amount)
            break
        else:
            print("Try again")
    return amount
   

def account_create(name_of_account, type_of_account):
    """Each and every account is unique

    Args:
        name_of_account (_type_): name of account
        type_of_account (_type_): The category it belongs
    """

    account_name = str.upper(name_of_account)
    account_type = str.upper(type_of_account)

    print("___________________________________")
    print(account_type)
    print(account_name)
    print("___________________________________")


    # key parameter
    recorded_time = time_id()

    # transaction of project
    transaction_date = date_of_transaction()

    # Money in or Money Out (money_option)
    money_option = project_setup("money_option.csv", "Money Option")
    money_option = str.lower(money_option)

    #particulars based on option
    if money_option == "money_in":
        #particulars based on money in
        money_in_particulars = project_setup("money_in_particulars.csv", "Money_in_particulars")

        # amount recorded in this category
        amount_transacted = transaction_amount()

    elif money_option == "money_out":
        #particulars based on money out
        money_out_particulars = project_setup("money_out_particulars.csv", "Money_in_particulars")

    #balance 
    # retrieved from the previous records in the database
    total_money_in = "total sum of money in "
    total_money_out = "total sum of money out"
    balance =  0


    output = [recorded_time, transaction_date, money_in_particulars, money_out_particulars, amount_transacted, balance]
    print(output)

    


account_create("mpesa account","expenditure")


        
