#-------------------------------------------------------------------------------
#Name:  Maksim Chernikov
#Start Date: 7/23/23
#Title: Age Calculator
#Inputs: Birth date and current date
#Process: Calculate age
#Outputs: Age in years, months, weeks, and days
#-------------------------------------------------------------------------------

import calendar
                                           #Import necessary modules
from pprint import pprint

#-------------------------------------------------------------------------------
def main():
    
    birthMonth = 0
    birthDay = 0
    birthYear = 0
    
    currentMonth = 0                                                                   
    currentDay = 0
    currentYear = 0                        #Initialize variables
    ageYear = 0
    
    ageMonth = 0
    ageDay = 0
    
    
    birthMonth = getBirthDate("month")           #Prompt input of birth month
    
    birthDay = getBirthDate("day")           #Prompt input of birth day
    
    birthYear = getBirthDate("year")           #Prompt input of birth year
    
    
    currentMonth = getCurrentDate("month")           #Prompt input of current month
    
    currentDay = getCurrentDate("day")           #Prompt input of current month
    
    currentYear = getCurrentDate("year")           #Prompt input of current month
    
    
    ageYear = calcAge(birthYear, currentYear)           #Calculate age in years   
    
    ageMonth = calcAge(birthMonth, currentMonth)           #Calculate age in months left over after ageYear calculation
    
    ageDay = calcAgeDay(birthDay, currentDay)           #Calculate age in days left over after ageMonth calculation
    
    
    ageYear = yearAdjust(ageYear, ageMonth)             #Adjust for bad math

    ageMonth = monthAdjust(ageMonth)                    #Adjust for bad math
    
    ageDay = daysAdjust(birthYear, currentYear, ageDay, birthMonth, currentMonth, currentDay)  #Adjust for leap days
    
    printOutputs(ageYear, ageMonth, ageDay)             #Print outputs
    
#-------------------------------------------------------------------------------

def getBirthDate(time_unit):
    birth_date = int
    
    birth_date = int(input("Input birth " + time_unit +": "))
    return birth_date

#-------------------------------------------------------------------------------

def getCurrentDate(time_unit):
    current_date = int
    
    current_date = int(input("Input current " + time_unit +": "))
    return current_date

#-------------------------------------------------------------------------------

def calcAge(birth_int, current_int):
    age = 0
    age = current_int - birth_int
    return age

#-------------------------------------------------------------------------------

def calcAgeDay(birth_day, current_day):
    days_old = 0
    days_old = current_day - birth_day
    return days_old
    
#-------------------------------------------------------------------------------

def yearAdjust(age_year, age_month):
    if age_month < 0:
        age_year -=1
        return age_year
    else:
        return age_year

#-------------------------------------------------------------------------------

def monthAdjust(age_month):
    if age_month < 0:
        age_month = age_month + 12
        return age_month
    else:
        return age_month
    
#-------------------------------------------------------------------------------
    
def daysAdjust(birth_year, current_year, days_old, b_month, c_month, c_day):
    leap_days = 0
    leap_days = calendar.leapdays(birth_year,current_year)
    days_old = leap_days + days_old
    if b_month > 2 or (c_month > 3 and c_day != 29):
        days_old -= 1
    return days_old

#-------------------------------------------------------------------------------

def printOutputs(yr, mnth, day):
    output = f" You are {yr} year(s), {mnth} month(s), and {day} day(s) old"
    print(output)
#-------------------------------------------------------------------------------

main()


