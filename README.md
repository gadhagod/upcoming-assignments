# Schoology Upcoming Assignments
A quick Flask app that shows you your upcoming assignments from Schoology.

### Why?
Schoology calender is kinda cramped. Also, it doesn't show due times for assignments, and as a procrastinator, this is a big deal.

### Enviroment Variables
Four enviroment variables are used:
- `SCHOOLOGY_KEY` and `SCHOOLOGY_SECRET` are your API credentials. Obtain them from `{school's schoology URL}/api`
- `CLASSES` is a string, is in the format of a JSON object. Each key will be the class name, and each value will be the class ID
 - Example: `{"English": 1234567, "Math": 2345678}`
- `SCHOOLOGY_URL` is your school's schoology url. 
 - Example: `https://schoology.myschool.com` (or .org, .net; whatever your school's website uses)
To set an enviroment variable, run `'export VAR_NAME=VAR_VALUE'`

### Running locally
It's probably a better idea to run locally, because only you will be able to see your assignments. \
To start up the server, run:
    
    python3 server.py &

Usually, the port will default to 5000, so head to `127.0.0.1:5000`. Assignments for the next six days will show up, with their due times. You can click on each link to get to get assignment info and submission page.