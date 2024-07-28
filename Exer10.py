def is_leap_year(year):
    """Return True if the year is a leap year, False otherwise."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(month, year=None):
    """Return the number of days in the specified month, considering leap years for February."""
    # Dictionary of months with their number of days
    month_days = {
        "January": 31,
        "February": 28,  # Default for non-leap years
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    
    # Check if the month is valid
    if month not in month_days:
        return None
    
    # Special case for February
    if month == "February" and year is not None:
        if is_leap_year(year):
            return 29
        else:
            return month_days[month]
    
    # Return the number of days for the month
    return month_days[month]

def main():
    # Input month from the user
    month = input("Enter the month name: ").strip()
    
    # Get the number of days in the month
    days = get_days_in_month(month)
    
    if days is None:
        print("Invalid month name.")
        return
    
    # Special case for February to ask for the year
    if month == "February":
        year = int(input("Enter the year: "))
        days = get_days_in_month(month, year)
    
    # Print the result
    print(f"The number of days in {month} is: {days}")

if __name__ == "__main__":
    main()
