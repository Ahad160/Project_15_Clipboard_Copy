import datetime

def get_date_and_time():
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Format the date and time as a string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Print the result
    print("Current Date and Time: {}".format(formatted_datetime))

# Call the function to get and print the date and time
get_date_and_time()
