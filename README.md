# Title:
# Take Home Test

# Description:
# An HTTP REST API capable of returning menus for specific dates and type requests. This information is obtained from an SQL server and displayed on the web page.
# User enters GET request with date and time and API returns menu.

# Installation:
# To run this API, python and the following libraries are required: mysql.connector, json, fastapi (including FastAPI, HTTPException, and status).
# Additionally, uvicorn is required to connect to the server.

# Running the program:
# Once all items are installed, open the command prompt. Change directories (cd) to the file path where the python API program is stored. 
# Send the command "python -m uvicorn Take_Home:app --reload" to connect to the server.
# Enter the SQL server information when prompted.
# On a web browser, open the http:// address provided in the command response.
# Enter a GET request by entering a URL with a date and type using the format specified in the assignment.
