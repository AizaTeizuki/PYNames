'''
Created by @Aiza Teizuki
April, 2, 2019
https://github.com/AizaTeizuki
'''

import random

BoyNames = open("D:\\Coding\\Python\\NameLibrary\\NameLists\\BoyNames.txt").readlines()
GirlNames = open("D:\\Coding\\Python\\NameLibrary\\NameLists\\GirlNames.txt").readlines()
FamilyNames = open("D:\\Coding\\Python\\NameLibrary\\NameLists\\FamilyNames.txt").readlines()


def Random_Gender():
    if random.randint(1, 2) == 1:
        return("Male")
    else:
        return("Female")


def First_Name(Gender):
    Gender = str.lower(Gender)
    if Gender == "m" or Gender == "male":
        return(str.lower(BoyNames[random.randint(1, len(BoyNames))]).strip())
    elif Gender == "f" or Gender == "female":
        return(str.lower(GirlNames[random.randint(1, len(GirlNames))]).strip())
    else:
        print("Sorry, the only availabe genders are male and female.")


def FamilyName():
    return(str.lower(FamilyNames[random.randint(1, len(FamilyNames))]).strip())


def FullName(Gender):
    FirstName = First_Name(Gender).strip()
    LastName = FamilyName().strip()
    FullName = FirstName + " " + LastName
    return(str.lower(FullName))
