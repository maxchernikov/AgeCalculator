
# Import necessary module(s)

import sys

# Enumerate the amount of age measurements the calculator outputs as a GLOBAL variable (e.g. Years, months, and days is 3 age measurements)
TIME_UNITS = 3        

#-------------------------------------------------------------------------------
def main():
        
    birthDateList = [-1,-1,-1]
    
    currentDateList = [-1,-1,-1]                         
    
    ageList = []

    accumulator = 0
    
    ##todo finish input validation
    # Populate list with user input birth date in MM/DD/YYYY format and validate input
    while valiDate(birthDateList[0],birthDateList[1],birthDateList[2]) == False:
        birthDateList = getBirthDate()
        
        
    while valiDate(currentDateList[0],currentDateList[1],currentDateList[2]) == False:
        currentDateList = getCurrentDate()
    
    # Doesn't run the entire program if the user was born on the current day
    if birthDateList == currentDateList:
        print()
        print("You are 0 days old. Happy birthday!")
        sys.exit()
        
    # Loop that calculates age in years, months, and days and appends date into a list
    while accumulator < TIME_UNITS:
        age = calcAge(birthDateList[accumulator],currentDateList[accumulator])
        ageList.append(age)                            
        accumulator +=1
    
    # Adjust years for cases where users birthday is coming up in the current year 
    ageList[2] = yearAdjust(ageList[2], ageList[0])
    
    # Adjust days for cases where users birthday is coming up in the current year
    ageList[1] = daysAdjust(ageList[1])

    # Adjust months to ensure no negative numbers
    ageList[0] = monthAdjust(ageList[0])
    
    # Print user age in years, months, and days
    printOutputs(ageList[0],ageList[1],ageList[2])            
    
#-------------------------------------------------------------------------------

def getBirthDate():
    birth_date = []
    print()
    birth_date = [int(x) for x in input("Enter birth date (e.g. mm/dd/yyyy): ").split("/")]
    return birth_date

#-------------------------------------------------------------------------------

def getCurrentDate():
    current_date = []
    print()
    current_date = [int(x) for x in input("Enter current date (e.g. mm/dd/yyyy): ").split("/")]
    return current_date

#-------------------------------------------------------------------------------

# Input validation for birth and current date
def valiDate(mnth, day, yr):
    while \
          mnth > 12 or mnth < 0 or \
          day > 31 or day < 0 or \
          yr > 9999 or yr < 1900:
        return False 
    
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
        age_month += 11
        return age_month
    else:
        return age_month
    
#-------------------------------------------------------------------------------

# Adjust for days to ensure no negative numbers
def daysAdjust(days_old):
    if days_old < 0:
        days_old+= 31
    return days_old

#-------------------------------------------------------------------------------

def printOutputs(mnth, day, yr):   
    print()
    age_output = "You are:"
    
    if yr > 0:
        age_output += f" {yr} year(s)"
    
    if mnth > 0:
        age_output += f" {mnth} month(s)"
        
    if day > 0:
        age_output += f" {day} day(s)"
        
    print (age_output)
    
#-------------------------------------------------------------------------------

main()



