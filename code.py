import csv
import datetime

# Converting the csv or txt file to a list of dictionaries
def csv_into_dict(filename: str):
    with open(filename, 'r') as file:
        csvreader = csv.DictReader(file)
        data = [row for row in csvreader]
    return data


# Convert Time('HH:MM:SS') to seconds
def get_seconds(time: str):
    hours, minutes, seconds = time.split(':')
    seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    return seconds


# Convert seconds to Time('HH:MM:SS')
def seconds_into_time(sec: int):
    return str(datetime.timedelta(seconds = sec))
        

# Call_logs is a list of dictionaries
call_logs = csv_into_dict('call_log.txt')
# call_logs = csv_into_dict('call_log.csv')


# Distinct From Numbers for a day
distinct_numbers = set([row['From Mobile'] for row in call_logs])
print('Distinct From Numbers for a day :', distinct_numbers)


# Distinct From Numbers who used the Free Plan. (Call Duration less than 1 min)
distinct_numbers_free = set([row['From Mobile'] for row in call_logs if get_seconds(row['Call Duration']) < 60])
print('Distinct From Numbers who used the Free Plan :', distinct_numbers_free)


# Total call duration with respect to From Number
total_call_duration = {}
for row in call_logs:
    if row['From Mobile'] not in total_call_duration:
        total_call_duration[row['From Mobile']] = get_seconds(row['Call Duration'])
    else:
        total_call_duration[row['From Mobile']] += get_seconds(row['Call Duration'])

for key, value in total_call_duration.items():
    total_call_duration[key] = seconds_into_time(value)
    # print('Total call duration with respect to From Number :')
    # print(key, ':', total_call_duration[key])
    print(f'The total call duration of the number {key} is {total_call_duration[key]}')


# Total income for a day. (Cost to be considered for Call Duration greater 1 min)
total_minutes = 0
for row in call_logs:
    if get_seconds(row['Call Duration']) >= 60:
        total_minutes += (get_seconds(row['Call Duration'])//60)


# If the Call Duration is above 1 min then it will be charged at 
# 30paise/min
total_income = (83 * 30) / 60
print('Total Income for the day :', total_income)