import os
import requests
import json
from time import sleep
from datetime import datetime
from zoneinfo import ZoneInfo

API_KEY = ("BSYZABBSQMDYY5P3ZRC5SGVR2")

# ============================================== API SECTION ==============================================
def get_from_api(city):
    # Unit group metric ensures °C and % for humidity (if supported)
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={API_KEY}"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.json()
# =========================================================================================================


# ============================================ DIAGNOSE-SECTION ===========================================
def print_info(city):
    data = get_weather_json(city)
    with open("data.json","w") as f:
        json.dump(data,f,indent=4)

def get_from_file():
    with open("data.json","r") as f:
        data = json.load(f)
    return data

def pretty_print(obj):
    print(json.dumps(obj, indent=2, sort_keys=True))
# =========================================================================================================

# ============================================= FORMAT-SECTION ============================================
def local_time(tz_name):
    local_time = datetime.now(ZoneInfo(tz_name))
    return local_time.strftime("%H:%M") # returns "14:32"

def hour_12(time):
    '''
    convert 24 hour to 12 hour format    
    :param time: time from local_time
    '''
    pass

def date_formate(date):
    '''
    convert yyyy-mm-dd to dd-month-yyyy
        
    :param date: date from data
    '''
    pass

def clear():
    '''
    to clear the terminal for a better console UI
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

def style(s,n=0.04):
    '''
    nothing, just attention to details
    :param s: string input
    :param n: speed of text (default 0.04)
    '''
    
    for i in range (0,len(s)):
        print(s[i],end='')
        sleep(n)

def press_key():
    input("\n\nPress ENTER to continue...")

# =========================================================================================================

# ========================= IMPORTANT SECTION (could not think of better name) ============================

def read_locations(filename="saved_locations.json"):
    """
    Returns a dict with structure:
    {
        "default": str,
        "saved": [str, str, ...]
    }
    """
    if not os.path.exists(filename):
        # Initialize an empty structure if file doesn't exist
        return {"default": None, "saved": []}

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def write_locations(data, filename="saved_locations.json"):
    """
    Writes the dict back to disk.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def manage_locations(mode=1, new_name=None, filename="saved_locations.json"):
    """
    mode 1: return default name
    mode 2: add `new_name` to saved list
    mode 3: replace default with `new_name` and push old default into saved
    """
    data = read_locations(filename)

    if "default" not in data:
        data["default"] = None
    if "saved" not in data:
        data["saved"] = []

    # --- MODE 1: return default ---
    if mode == 1:
        return data["default"]

    # --- MODE 2: add to saved list ---
    elif mode == 2:
        if new_name is None:
            raise ValueError("mode 2 requires new_name")
        if new_name not in data["saved"]:
            data["saved"].append(new_name)
        write_locations(data, filename)
        return True

    # --- MODE 3: replace default ---
    elif mode == 3:
        if new_name is None:
            raise ValueError("mode 3 requires new_name")

        old_default = data["default"]

        if old_default is not None and old_default not in data["saved"]:
            data["saved"].append(old_default)

        data["default"] = new_name

        if new_name in data["saved"]:
            data["saved"].remove(new_name)

        write_locations(data, filename)
        return True

    else:
        raise ValueError("Invalid mode. Use 1, 2, or 3.")

# ========================================== DATA-DELIVER SECTION =========================================
def currentTime_data(data):

    day_sameday_data = data["days"][0]
    date = day_sameday_data["datetime"]
    avg_temp = day_sameday_data["temp"]
    max_temp = day_sameday_data["tempmax"]
    min_temp = day_sameday_data["tempmin"]

    hour_sameday_data = data["days"][0]["hours"]
    current_time = local_time(data["timezone"])
    for i in hour_sameday_data:
        if i["datetime"][0:2] == current_time[0:2]:
                temp = i["temp"]
                feelslike = i["feelslike"]
                humidity = i["humidity"]
                conditions = i["conditions"]
                uvindex = i["uvindex"]
                visibility = i["visibility"]

    print(f'''
        Current Temperature
          
Time                        : {local_time(data["timezone"])}
Date                        : {date}
Location                    : {data["resolvedAddress"].capitalize()}

Current Temperature         : {temp}\u00B0C         
Feels like                  : {feelslike}\u00B0C

Max Temperature             : {max_temp}\u00B0C
Min Temperature             : {min_temp}\u00B0C
Average Temperature         : {avg_temp}\u00B0C
         
Humidity                    : {humidity}%
conditions                  : {conditions}
uvindex                     : {uvindex}
visibility                  : {visibility}
''')

def wholeDay_data(data):
    pass

def next7Days_data(data):
    pass

# =========================================================================================================


# ================================================== main ==================================================
if __name__ == "__main__":gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg

    clear()

    city = manage_locations() # default city

    try:
        data = get_from_api(city)
        # data = get_from_file()
    except requests.HTTPError as e:
        print("HTTP error:", e)
        try:
            print("Response text:", e.response.text)
        except Exception:
            pass
    except Exception as e:
        print("Error:", e)
    
    currentTime_data(data)
