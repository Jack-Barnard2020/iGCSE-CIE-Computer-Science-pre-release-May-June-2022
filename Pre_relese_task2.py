import datetime   #Import datetime to get current date without user input
import csv      #Import csv to save memeber infomation in spreadhseet 


date = str()
current_date = str()
full_date = str()

full_name = str()
full_name_correct = str()

volunteer = str()
volunteer_type = int()
volunteer_type_correct = str()
volunteer_type_array = ["entrance gate", "gift shop", "painting and decorating"]

pay_today = str()
payed = str()

sponsor = str()
sponsor_name = str()
sponsor_message = str()
sponsor_message_correct = str()



def get_current_date():
    full_date = datetime.datetime.now()
    current_date = full_date.strftime("%x")
    return current_date
    #gets full current date and then uses modifier to change it to short 6 digit date
    #then returns the value to be called at sing up

def fullname_sing_up():
    full_name_correct = "i"
    while full_name_correct != "y":
        full_name = str(input("Please input your full name? "))
        full_name_correct = str(input(f"Is {full_name} your correct full name: y/n ? ")).lower()
        while full_name_correct != "y" and full_name_correct != "n":
            print("ERROR")
            print(f"{full_name_correct} is not a valid input!")
            full_name_correct = str(input(f"Is {full_name} your correct full name: y/n ? ")).lower()
    return full_name
    #Asks for users full name
    #Validates if it is correct and allows user to edit
    #Allows invalid inputs
    #returns full name

def volunteer_sing_up():
    volunteer = str(input("Would you like to be a volunteer: y/n ? ")).lower()
    while volunteer != "y" and volunteer != "n":
        print("ERROR")
        print(f"{volunteer} is not a valid input!")
        volunteer = str(input("Would you like to be a volunteer: y/n ? ")).lower()
    if volunteer == "n":
        volunteer = "no"
    elif volunteer == "y":
        volunteer_type_correct = "i"
        while volunteer_type_correct != "y":
            volunteer_type = int(input(f"What type of volunteer would you like to be 1 = {volunteer_type_array[0]}, 2 = {volunteer_type_array[1]}, 3 = {volunteer_type_array[2]} : 1/2/3 ? "))
            volunteer_type = volunteer_type - 1
            while volunteer_type != 0 and volunteer_type != 1 and volunteer_type != 2:
                print("ERROR")
                print(f"{volunteer_type+1} is not a valid input!")
                volunteer_type = int(input(f"What type of volunteer would you like to be 1 = {volunteer_type_array[0]}, 2 = {volunteer_type_array[1]}, 3 = {volunteer_type_array[2]} : 1/2/3 ? "))
                volunteer_type = volunteer_type - 1
            volunteer_type_correct = str(input(f"Is {volunteer_type_array[volunteer_type]} your correct input: y/n ? ")).lower()
            while volunteer_type_correct != "y" and volunteer_type_correct != "n":
                print("ERROR")
                print(f"{volunteer_type_correct} is not a valid input!")
                volunteer_type_correct = str(input(f"Is {volunteer_type_array[volunteer_type]} your correct input: y/n ? ")).lower()
        volunteer = volunteer_type_array[volunteer_type]
    else:
        print("Unkown ERROR")
        volunteer_sing_up()
    return volunteer
    #asks user if they would like to be a volunteer
    #validates input , allows for invalid inputs
    #if user doesnt want to be volunteer varible is set
    #if user does, asks type
    #valdates type, allows for invlaid inputs
    #volunteer varible is set to type
    #returns volunteer

def pay_sing_up():
    pay_today = str(input("Would you like to pay today: y/n ? ")).lower()
    while pay_today != "y" and pay_today != "n":
        print("ERROR")
        print(f"{pay_today} is not a balid input!")
        pay_today = str(input("Would you like to pay today: y/n ? ")).lower()
    if pay_today == "y":
        print("You have been charged $75")
        payed = "yes"
    else:
        payed = "no"
    return payed
    #akss user to pay
    #charges fee if y
    #doesnt if n
    #returns payed

def member_sign_up():
    full_name = fullname_sing_up()
    date = get_current_date()
    volunteer = volunteer_sing_up()
    payed = pay_sing_up()
    rows = [[full_name, volunteer, date, payed, payed],]
    filename = "member_records.csv"
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerows(rows)
    #gets all user info
    #puts it into an array
    #appends it to csv file

def sponsor_sign_up():
    sponsor = str(input("Would you like to become a sponsor a brass plack: y/n ? ")).lower()
    while sponsor != "y" and sponsor != "n":
        print("ERROR")
        print(f"{sponsor} is not a valid input!")
        sponsor = str(input("Would you like to become a sponsor: y/n ? ")).lower()
    if sponsor == "y":
        full_name = fullname_sing_up()
        sponsor_message_correct = "i"
        while sponsor_message_correct != "y":
            sponsor_message = str(input("What message would you like to be on sponsored plack? "))
            sponsor_message_correct = str(input(f"Is '{sponsor_message}' correct: y/n ? ")).lower()
            while sponsor_message_correct != "y" and sponsor_message_correct != "n":
                print("ERROR")
                print(f"{sponsor_message_correct} is not a valid input!")
                sponsor_message_correct = str(input(f"Is '{sponsor_message}' correct: y/n ? ")).lower()
        rows = [[full_name, sponsor_message],]
        filename = "sponsor_records.csv"
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerows(rows)
        print("You have been charged $200")
    elif sponsor == "n":
        pass
    else:
        print("Unkown ERROR")
        sponsor_sign_up()
    #asks sponsor to reinput thier name in case they want to sposnor it diffrenlty
    #asks for message
    #validates messaage
    #saves to file



member_sign_up()
sponsor_sign_up()
