import datetime
filename = "TimeCheck.txt" #absolute path  of logging file .txt

def isWeekday():
    current_date = datetime.date.today()
    # Sunday (6) Saturday (5)
    return current_date.weekday() not in [5, 6] # remove unworked day

def editFile():
    with open(filename, 'r') as file:
        content = file.read()
    with open(filename, 'w') as file:
        file.write(f"{datetime.date.today().day}/{datetime.date.today().month}/{datetime.date.today().year} - {datetime.datetime.now().hour}h{datetime.datetime.now().minute} - {datetime.datetime.now().hour + 8}h{datetime.datetime.now().minute}\n" + content)


if isWeekday():
    try:
        file = open(filename, 'r')
        content = file.readlines()
        latest = content[0].split(' - ')[0]
        if latest != f"{datetime.date.today().day}/{datetime.date.today().month}/{datetime.date.today().year}":
            file.close()
            editFile()
        else:
            file.close()

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


