stu1 = {'name': 'Madhur', 'marks': 90.56, 'rno': 1}
stu2 = {'name': 'Rupali', 'marks': 100.0, 'rno': 2}
stu3 = {'name': 'Heena', 'marks': 91.0, 'rno': 3}
stu4 = {'name': 'Varun', 'marks': 95.0, 'rno': 4}

students = [stu1, stu2, stu3, stu4]

def display_all():
    for stu in students:
        print('{} {} {}'.format(stu['rno'], stu['name'], stu['marks']))

def display(stu):
    print('{} {} {}'.format(stu['rno'], stu['name'], stu['marks']))

def display_topper():
    topper = students[0]
    for s in students:
        if topper['marks'] < s['marks']:
            topper = s
    '''
    With while loop
    i = 1
    while i < len(students):
        if topper['marks'] < students[i]['marks']:
            topper = students[i]
        i += 1
    '''
    display(topper)

def get_average_marks():
    sum = 0
    for stu in students:
        sum += stu['marks']
    avg = sum / len(students)
    return avg

def is_below_avg(stu):
    avg = get_average_marks()

    if stu['marks'] < avg:
        print('{} is below average'.format(stu['name']))
    elif stu['marks'] == avg:
        print('{} is equal to average'.format(stu['name']))
    else:
        print('{} is above average'.format(stu['name']))


display_all()

display(stu1)

display_topper()

is_below_avg(students[0])
is_below_avg(students[1])
is_below_avg(students[2])
is_below_avg(students[3])


