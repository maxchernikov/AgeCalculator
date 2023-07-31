#-------------------------------------------------------------------------------
#Name:  Maksim Chernikov
#Start Date: 7/23/23
#Title: Age Calculator
#Inputs: Birth date and current date
#Process: Calculate age
#Outputs: Age in years, months, and days
#-------------------------------------------------------------------------------

# Import necessary module(s)
import calendar                 

# Enumerate the amount of age measurements the calculator outputs (e.g. Years, months, and days is 3 age measurements)
TIME_UNITS = 3        

#-------------------------------------------------------------------------------
def main():
    
    birthDateList = []
    
    currentDateList = []                         
    
    ageList = []

    accumulator = 0
    
    # Populate list with user input birth date in MM/DD/YYYY format
    birthDateList = getBirthDate()

    # Populate list with user input current date in MM/DD/YYYY format
    currentDateList = getCurrentDate()
    
    # Loop that calculates age in years, months, and days and appends date into a list
    while accumulator < TIME_UNITS:
        age = calcAge(birthDateList[accumulator],currentDateList[accumulator])
        ageList.append(age)                            
        accumulator +=1
    
    # Adjust years for cases where users birthday is coming up in the current year 
    ageList[2] = yearAdjust(ageList[2], ageList[0])    

    # Adjust months to ensure no negative numbers
    ageList[0] = monthAdjust(ageList[0])
    
    # Adjust for leap days and add them to days old
    ageList[1] = daysAdjust(birthDateList[1], birthDateList[2], currentDateList[1], currentDateList[2], ageList[1])  
    
    # Print user age in years, months, and days #UPDATE WHEN ADDING MORE TIME UNITS IN FUTURE#
    printOutputs(ageList[0],ageList[1],ageList[2])            
    
#-------------------------------------------------------------------------------

def getBirthDate():
    birth_date = []
    birth_date = [int(x) for x in input("Enter birth date (e.g. mm/dd/yyyy): ").split("/")]
    return birth_date

#-------------------------------------------------------------------------------

#todo improve user prompts? 
def getCurrentDate():
    current_date = []
    print()
    current_date = [int(x) for x in input("Enter current date (e.g. mm/dd/yyyy): ").split("/")]
    return current_date

#-------------------------------------------------------------------------------

def calcAge(birth_int, current_int):
    age = 0
    age = current_int - birth_int
    return age   
    
#-------------------------------------------------------------------------------

# Adjust years for cases where users birthday is coming up in the current year 
def yearAdjust(age_year, age_month):
    if age_month < 0:
        age_year -=1
        return age_year
    else:
        return age_year

#-------------------------------------------------------------------------------

# Adjust months to ensure no negative numbers
def monthAdjust(age_month):
    if age_month < 0:
        age_month += 12
        return age_month
    else:
        return age_month
    
#-------------------------------------------------------------------------------

# Adjust for leap days and add them to days old
def daysAdjust(birth_month, birth_year, current_month, current_year, days_old):
    leap_days = 0
    leap_days = calendar.leapdays(birth_year,current_year)
    days_old += leap_days
    if leap_days > 0:
        if birth_month > 2 or (current_month > 3):
            days_old -= 1
    return days_old

#-------------------------------------------------------------------------------

#todo add more time units (eg weeks)
def printOutputs(mnth, day, yr):
    print()
    age_output = ""
    
    if yr > 0:
        age_output += f"{yr} year(s)"
    
    if mnth > 0:
        age_output += f" {mnth} month(s)"
        
    if day > 0:
        age_output += f" {day} day(s)"
        
    print (age_output)
    
#-------------------------------------------------------------------------------

main()



