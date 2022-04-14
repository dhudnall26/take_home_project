# imports sqlalchemy for connection to sql database, json for data formatting, and fastapi for creation of api structure
import sqlalchemy as db
from sqlalchemy import create_engine
import json
from fastapi import FastAPI, HTTPException, status

# declares FastAPI app
app = FastAPI()

# prompts user to log into SQL server (rather than sharing login information in program)
host_value = input("Enter the host name:")
port_number = input("Enter the port number:")
database_value = input("Enter the database/schema:")
user_name = input("Enter your username:")
password = input("Enter your password:")

# connects to SQL server
engine = db.create_engine('mysql://' + user_name + ':' + password + '@' + host_value + ':' + port_number + '/' + database_value)
connection = engine.connect()       

# declares get method
@app.get("/menu/{date_id}/{type_id}", status_code=status.HTTP_200_OK)
async def read_item(date_id, type_id):
# parses GET request to obtain data needed for search in SQL. Gives 404 error if date has incorrect number of characters  
    get_request = "/menu/" + date_id + "/" + type_id
    try:
        year = int(get_request[6:10])
        month = int(get_request[11:13])
        day = int(get_request[14:16])
        type_meal = (get_request[17:])
    except :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Sorry, no meals are available on this date.')
    if (get_request[10:11] != "-") or (get_request[13:14] != "-"):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Sorry, no meals are available on this date.')
    week_id_no = 0
    meal_id_no = []
    meal_names = []

    # Finds the week id number based on the date input and the range in which it falls
    result = engine.execute("SELECT start_date, end_date, id FROM week")
    for a in result:
        x = str(a[0]) + str(a[1]) + str(a[2])
        x = x.replace("(","")
        x = x.replace(")","")
        x = x.replace(".","")
        x = x.replace(" ","")
        x = x.replace(",","")
        x = x.replace("-","")
        x = x.replace("datetimedate","")
        if ((year >= int(x[0:4])) and (year <= int(x[8:12]))):
            if ((month == int(x[4:6])) or (month == int(x[12:14])) and (1 <= month <= 12)):
                if (((month == 2) and (1 <= day <= 29) and ((year % 4) == 0)) or ((month == 2) and (1 <= day <= 28)) or (((month == 4) or (month == 6) or (month == 9) or (month == 11)) and (1 <= day <= 30)) or (((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)) and (1 <= day <= 31))):
                    if((month == int(x[4:6])) and (month == int(x[12:14])) and (day >= int(x[6:8])) and (day <= int(x[14:16]))):
                        week_id_no = x[16:20]
                    elif((int(x[4:6]) != int(x[12:14])) and (((month == int(x[4:6])) and (day >= int(x[6:8]))) or ((month == int(x[12:14])) and (day <= int(x[14:16]))))):
                        week_id_no = x[16:20]

    # Finds meal id numbers associated with the identified week id number
    result = engine.execute("SELECT week_id, meal_id FROM meal_week")
    for a in result:
        if str(a[0]) == str(week_id_no):
            meal_id_no.append(a[1])

    # Finds meals associated with the identified meal id numbers and input meal type
    result = engine.execute("SELECT id, name, type FROM meal")
    for a in result:
      if (a[0] in meal_id_no) and (str(a[2]) == str(type_meal)):
          meal_names.append(a[1])
          
    # Returns meal names if meals are found for the week and meal type
    if meal_names != []:
        meal_names = json.dumps(meal_names)
        return(json.loads(meal_names))
    else:    
    # Returns 404 error if no meals are found 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Sorry, no meals are available on this date.')
