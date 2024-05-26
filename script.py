import requests
from datetime import datetime, time
import pyautogui
import time as timer

with open('apikey.txt', 'r') as f:
    apiKey = f.read().strip()
     
def get_productivity(emp):
    id = emp["id"]
    date = emp["date"]
    vac_hours = float(emp["vac_hours"])
    vac_mins = 0 if isinstance(vac_hours,int) else int((vac_hours-int(vac_hours)) * 60)
    vac_hours = int(vac_hours)
    hours = time(vac_hours, vac_mins)
    productivity_link = f'https://desktime.com/api/v2/json/employee?apiKey={apiKey}&id={id}&date={date}'
    res = requests.get(productivity_link)
    if res.status_code == 200:
        resp = res.json()
        start_time = datetime.fromisoformat(resp['arrived']).time()
        end_time = datetime.fromisoformat(resp['left']).time()
        rem = time(23-end_time.hour,59-end_time.minute,59-end_time.second) 
        if start_time > hours:
            return time(0), hours
        elif rem > hours:
            return time(23-hours.hour, 59-hours.minute,59-hours.second), time(23,59,59)
        else:
            return 'no','no' 
    else:
        print(f'error with id: {id}, {date}, code {res.status_code}')

# def feed_emp_vac_data(id, date,)


# vac_start, vac_end = get_productivity(id,date,9.6)

def read_emps(vac_file, rate_file):
    with open(rate_file, 'r') as f:
        lines = f.read().strip().split('\n')
    rates = {}
    for line in lines[1:]:
        id, rate = line.split(',')
        rates[id] = rate

    with open(vac_file, 'r') as f:
        lines = f.read().strip().split('\n')
    emps = []
    for line in lines[1:]:
        fields = line.split(',')
        emp = {}
        emp['id'] = fields[0]
        emp['date'] = fields[1]
        emp['type'] = fields[2]
        emp['vac_hours'] = 8 if emp['id'] not in rates else rates[emp['id']]
        emps.append(emp)
    return emps


# # Switch to Firefox
# pyautogui.hotkey('alt', 'tab')
# timer.sleep(1)  # Adjust sleep time according to your system speed

pyautogui.press('win')
pyautogui.typewrite('firefox')
timer.sleep(1)
pyautogui.press('enter')
timer.sleep(1)

# Maximize the window
pyautogui.hotkey('win', 'up')
emps = read_emps('vacations.csv', 'rate.csv')
for emp in emps:
    # Type the URL and press Enter
    pyautogui.hotkey('ctrl', 't')
    timer.sleep(1)  # Adjust sleep time according to your system speed
    url = f'https://desktime.com/app/employee/{emp["id"]}/{emp["date"]}'
    print(url)
    pyautogui.typewrite(url)
    pyautogui.press('enter')
    timer.sleep(3)  # Adjust sleep time according to your system speed

    print(emp)
    try:
        start,end = get_productivity(emp)
        element = 0
    except:
        start,end = 0, emp['vac_hours']
        element = 3
    if start==end=='no':
        print('failed:', 'no time slot available to add vacation for this emp.')
        continue

    # Scroll down
    x = 450
    y = 540
    pyautogui.moveTo(450, 740, duration=0.5)
    pyautogui.scroll(-500)
    timer.sleep(2)  # Adjust sleep time according to your system speed

    element_image = r'C:\Users\Mario\python projects\gui automation for vacations\element.png'
    element2_image = r'C:\Users\Mario\python projects\gui automation for vacations\element2.png'
    element3_image = r'C:\Users\Mario\python projects\gui automation for vacations\element3.png'
    try:
        if element == 3:
            raise Exception()
        element_location = pyautogui.locateOnScreen(element_image,confidence=0.9)
        y = element_location.top + element_location.height
        x = element_location.left + element_location.width
        print('element1')
    except:

        try:
            if element == 3:
                raise Exception()
            element_location = pyautogui.locateOnScreen(element2_image,confidence=0.9)
            x,y = pyautogui.center(element_location)
            print('element2')
        except:
            try:
                element_location = pyautogui.locateOnScreen(element3_image,confidence=0.9)
                y = element_location.top + element_location.height
                x = element_location.left + element_location.width / 2
                print('element3')
            except:
                print('failed:', "Element not found on the page.")
                continue

    
    pyautogui.moveTo(x, y, duration=0.5)
    timer.sleep(1)
    pyautogui.click()

    # description
    pyautogui.moveTo(670, 455, duration=0.5)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.typewrite(emp['type'])
    timer.sleep(1)

    # start time
    pyautogui.moveTo(880, 350, duration=0.5)
    pyautogui.click(clicks=3)
    timer.sleep(1)
    pyautogui.typewrite(f'{start}')

    # end time
    pyautogui.moveTo(1000, 350, duration=0.5)
    pyautogui.click(clicks=3)
    timer.sleep(1)
    pyautogui.typewrite(f'{end}')

    # click save
    pyautogui.moveTo(1250, 780, duration=0.5)
    pyautogui.click()
    timer.sleep(5)
    pyautogui.hotkey('ctrl', 'w')

    # x, y = 500, 500  # Example coordinates, change as needed
    # pyautogui.click()
