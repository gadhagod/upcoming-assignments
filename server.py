from os import getenv
from json import dumps, loads
import schoolopy
import datetime
import flask

app = flask.Flask(__name__)
today = datetime.date.today()
days = [
    today,
    datetime.date.today() + datetime.timedelta(days=1),
    datetime.date.today() + datetime.timedelta(days=2),
    datetime.date.today() + datetime.timedelta(days=3),
    datetime.date.today() + datetime.timedelta(days=4),
    datetime.date.today() + datetime.timedelta(days=5),
    datetime.date.today() + datetime.timedelta(days=6)
]

def assignments():
    sc = schoolopy.Schoology(schoolopy.Auth(getenv('SCHOOLOGY_KEY'), getenv('SCHOOLOGY_SECRET')))
    classes = loads(getenv('CLASSES'))
    sc.limit = 100000*10000
    data = []
    for day in days:
        day_data = []
        for class_name in classes:
            for assignment in sc.get_assignments(classes[class_name]):    
                due_time = assignment['due']
                try:
                    due_day = due_time[:due_time.index(' ')]
                except:
                    continue
                if str(day) == due_day:
                    due_time = due_time[:-3][due_time.index(' '):].replace(' ', '')
                    due_hour = int(due_time[:2].replace('0', ''))
                    if due_hour > 12:
                        due = str(due_hour-12) + ' pm'
                    else:
                        due = str(due_hour) + ' am'
                    day_data.append({
                        'title': assignment['title'],
                        'link': getenv('SCHOOLOGY_URL') + '/assignment/' + str(assignment['id']),
                        'due': due
                    })
        data.append({
            'date': day,
            'assignments': day_data
        })
    return(data)

@app.route('/', methods=['GET'])
def server_assignments():
    body = (
        '<style>' + open('styles.css', 'r').read() + '</style>' + '<h1>Upcoming Assignments</h1>'
    )
    for day in assignments():
        body = body + (
            '<strong>' + str(day['date']) + '</strong>'
        )
        if day['assignments'] == []:
            body = body + '<p>No assignments</p><br><hr>'
            continue
        for assignment in day['assignments']:
            body = body + (
                '<a href="' + assignment['link'] + '"><p>' + assignment['title'] + '</a> ' + assignment['due'] + '</p>'
            )
        body = body + '<hr>'
    return(body)

app.run()