# GUI Automation for DeskTime Vacation Entry

This script automates the process of entering vacation data for employees into DeskTime using GUI automation with `pyautogui`. It reads employee data from CSV files, calculates the appropriate vacation times, and interacts with the DeskTime web interface to input this data.

## Prerequisites

1. **Python 3.x**: Ensure Python 3.x is installed on your system.
2. **Required Python Packages**: Install the necessary packages using pip:
   ```bash
   pip install requests pyautogui
   ```
3. **API Key**: Place your DeskTime API key in a file named `apikey.txt` in the same directory as this script.

## Files

- `apikey.txt`: Contains the DeskTime API key.
- `vacations.csv`: Contains vacation data for employees.
- `rate.csv`: Contains hourly rates for employees.
- `element.png`, `element2.png`, `element3.png`: Images used for locating GUI elements on the DeskTime webpage.

## CSV File Formats

### vacations.csv
```csv
id,date,type
1,2023-05-01,vacation
2,2023-05-01,sick_leave
...
```

### rate.csv
```csv
id,rate
1,9.5
2,8
...
```

## Script Overview

1. **Read API Key**: The script reads the DeskTime API key from `apikey.txt`.
2. **Define Functions**:
   - `get_productivity(emp)`: Fetches productivity data for an employee and calculates the remaining hours.
   - `read_emps(vac_file, rate_file)`: Reads employee data and rates from CSV files.
3. **GUI Automation**:
   - Opens Firefox.
   - Navigates to the DeskTime employee page.
   - Inputs vacation data.
4. **Locate GUI Elements**: Uses predefined images to locate elements on the webpage.

## Running the Script

1. Ensure all prerequisite files are in the same directory as the script.
2. Adjust sleep times in the script if necessary to match your system's speed.
3. Run the script:
   ```bash
   python script.py
   ```

## Detailed Code Explanation

### Import Statements
```python
import requests
from datetime import datetime, time
import pyautogui
import time as timer
```
These imports are required for making API requests, handling date and time, and automating the GUI.

### Reading API Key
```python
with open('apikey.txt', 'r') as f:
    apiKey = f.read().strip()
```
Reads the DeskTime API key from `apikey.txt`.

### Get Productivity Data
```python
def get_productivity(emp):
    ...
```
Fetches productivity data for an employee and calculates remaining hours.

### Read Employee Data
```python
def read_emps(vac_file, rate_file):
    ...
```
Reads vacation data and hourly rates from CSV files.

### Open and Interact with Firefox
```python
pyautogui.press('win')
pyautogui.typewrite('firefox')
timer.sleep(1)
pyautogui.press('enter')
timer.sleep(1)

# Maximize the window
pyautogui.hotkey('win', 'up')
```
Opens Firefox and maximizes the window.

### Navigate to DeskTime and Enter Data
```python
emps = read_emps('vacations.csv', 'rate.csv')
for emp in emps:
    ...
    pyautogui.typewrite(url)
    pyautogui.press('enter')
    ...
```
Iterates over employees and enters their vacation data into DeskTime.

### Locate GUI Elements
```python
element_image = r'element.png'
element2_image = r'element2.png'
element3_image = r'element3.png'
...
element_location = pyautogui.locateOnScreen(element_image, confidence=0.9)
```
Locates GUI elements using images.

### Complete Data Entry
```python
pyautogui.moveTo(x, y, duration=0.5)
pyautogui.click()
...
pyautogui.typewrite(emp['type'])
...
pyautogui.typewrite(f'{start}')
...
pyautogui.typewrite(f'{end}')
...
pyautogui.click()
```
Fills out and submits the vacation data form on DeskTime.

## Notes

- Adjust sleep times (`timer.sleep()`) based on your system's performance.
- Ensure the paths to the element images are correct.
- Handle any exceptions that may occur during GUI automation to make the script more robust.

This script is designed for a specific task and may require adjustments based on changes to the DeskTime interface or your specific requirements.