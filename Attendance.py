from datetime import datetime

attendance = {}

# employee function
def record_attendance(employee_name):
    current_time = datetime.now().strftime('%Y-%m-%d : %H-%M-%S')

    # Record the attendance
    attendance[employee_name] = current_time

def view_attendance():
    # Print the attendance
    for employee, time in\
            attendance.items():
        print(f'{employee}: {time}')

record_attendance('Nelly')
record_attendance('Smart')
view_attendance()