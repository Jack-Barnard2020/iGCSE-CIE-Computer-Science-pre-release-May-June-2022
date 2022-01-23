import datetime #gets the current year to calculate if membership is expired
import csv #enables us to read the csv data base



filename = open('member_records.csv', 'r') #this sets the file to read only so we cant edit the file inside this program
file = csv.DictReader(filename) #this sets the file to read as a dictionary

subject = "" #subject is the varible used to compare to the set values that would put a member on that list

full_date = "" 
current_date = ""

element = [] #element is a list, that stores the split up user join date
single_element = int() #stores the year of which the user joined
current_year = int() #stores the current date

members = []
members_volunteers = []
members_volunteers_entrancegate = []
members_volunteers_giftshop = []
members_volunteers_painting = []
members_expired = []
members_unpaid = []
#these are all the lists which we will append values for
#they are labled to clearly identfiy which list is for what
#searhces for what task2 asks for

list_of_lists = ["members", "members_volunteers", "members_volunteers_entrancegate", "members_volunteers_giftshop", "members_volunteers_painting", "members_expired", "members_unpaid"]
list_to_search = int()
to_return = str()
#these are for the last subroutine in this file called "member_search" it enables us to use a for loop to output what each interger will lookup


def members_list_create():
    members = []
    for col in file: 
        members.append(col['Name'])
    print(members)
#this adds evrything under the name collum and adds it to the list called members
#we must set the list to have nothing it before runnning to stop haveing any double entries    

def members_volunteers_list_create():
    members_volunteers = []
    for col in file:
        subject = col['Volunteer']
        if subject == "no":
            pass
        else:
            subject = col['Name']
            members_volunteers.append(subject)
    print(members_volunteers)
#this code checks if somone is not a volunter
#then addes everyone else to the list
#using the smae colum value becuase it is the same row
#we must set the list to have nothing it before runnning to stop haveing any double entries    

def members_volunteers_entrancegate_list_create():
    members_volunteers_entrancegate = []
    for col in file:
        subject = col['Volunteer']
        if subject == "entrance gate":
            subject = col['Name']
            members_volunteers_entrancegate.append(subject)
        else:
            pass
    print(members_volunteers_entrancegate)
#this cheks if someone volunters at the entrance gate
#it passes over everyone else
#using the smae colum value becuase it is the same row
#we must set the list to have nothing it before runnning to stop haveing any double entries  

def members_volunteers_giftshio_list_create():
    members_volunteers_giftshop = []
    for col in file:
        subject = col['Volunteer']
        if subject == "gift shop":
            subject = col['Name']
            members_volunteers_giftshop.append(subject)
        else:
            pass
    print(members_volunteers_giftshop)
#this checks if somone volunteers at the gift shop
#it passes over everyone else
#using the smae colum value becuase it is the same row
#we must set the list to have nothing it before runnning to stop haveing any double entries

def members_volunteers_painting_list_create():
    members_volunteers_painting = []
    for col in file:
        subject = col['Volunteer']
        if subject == "painting and decorating":
            subject = col['Name']
            members_volunteers_painting.append(subject)
        else:
            pass
    print(members_volunteers_painting)
#this checks if somone volunteers by painting and deocrating
#it passes over everyone else
#using the smae colum value becuase it is the same row
#we must set the list to have nothing it before runnning to stop haveing any double entries

def get_current_year():
    full_date = datetime.datetime.now()
    current_date = full_date.strftime("%x")
    current_date = current_date.split('/')
    current_date = int(current_date[2])
    return current_date
#this code uses the module datetime, imported at the begging of the file
#it then modfies the date to a six digit date in the format mm/dd/yy
#it tben splits the date and takes the last object in the list which is the year and makes it an interger so it can be used in a calulation 

def members_expired_list_create():
    members_expired = []
    current_year = get_current_year()
    for col in file:
        subject = col['Date']
        subject = subject.split('/')
        subject = int(subject[2])
        test = current_year - subject
        if test >= 1:
            subject = col['Name']
            members_expired.append(subject)
        else:
            pass
    print(members_expired)
#this code uses the subroutine get_currrent_year
#it takes the current year and subtracts the join date form it, if it is grater than or equeal to 1 it adds the user to the list
#it passes over everyone else
#using the smae colum value becuase it is the same row
#we must set the list to have nothing it before runnning to stop haveing any double entries


def members_unpaid_list_create():
    members_unpaid = []
    for col in file:
        subject = col['Payed']
        if subject == "yes":
            pass
        else:
            subject = col['Name']
            members_unpaid.append(subject)
    print(members_unpaid)
#this code looks to see if the memeber has payed, and then adds them to the list
#it passes over everyone else
#using the smae colum value becuase it is the same row
#we must set the list to have nothing it before runnning to stop haveing any double entries

def search_members():
    print("************************************")
    print("")
    print("           Member Search")
    print("")
    print("************************************")
    lists = -1
    for i in list_of_lists:
        lists = lists + 1
        print(lists, "=" ,list_of_lists[lists])
    while again == "y":
        list_to_search = int(input("Input number of list to look up? "))
        while list_to_search > 6:
            print("ERROR")
            print(f"{list_to_search} is not a valid input!")
            list_to_search = int(input("Input number of list to look up? "))
        if list_to_search == 0:
            members_list_create()
        elif list_to_search == 1:
            members_volunteers_list_create()
        elif list_to_search == 2:
            members_volunteers_entrancegate_list_create()
        elif list_to_search == 3:
            members_volunteers_giftshio_list_create()
        elif list_to_search == 4:
            members_volunteers_painting_list_create()
        elif list_to_search == 5:
            members_expired_list_create()
        elif list_to_search == 6:
            members_unpaid_list_create()
        else:
            print("Unkonw ERROR")
            search_members()
        again = str(input("Would you like to search for a new lit of mebers: y/n ? ")).lower()
        while again != "y" or "n":
            print("ERROR")
            print(f"{again}, is not a valid input!")
            again = str(input("Would you like to search for a new lit of mebers: y/n ? ")).lower()
    quit()
#this is the final bit of code, it prints all the values assinged to the lists
#once the value is slected it runs the selected subroutine
#the vlaue is outputted
#this repeates until the user desides for the prgoram to stop
#it also allows the user to put in incorrect values and will repetedly ask the user for correct inputs until given

search_members()