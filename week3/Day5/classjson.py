import requests
import json
def get_data(day):
    with open("iss.json","r") as file:
        data = json.load(file)
    
    current_iss = []
    lst_iss = []
    try:
        for _ in range(5):
            iss = requests.get("http://api.open-notify.org/iss-now.json")
            if iss.status_code != 200 :
                raise Exception ("no data found")
            else:
                python_dict = iss.json()
                lst_iss.append(python_dict)
                # print(f"latitude {python_dict['iss_position']['latitude']} {python_dict['iss_position']['longtitude']}")
        
        with open("iss.json", "w") as file:
            json.dump(lst_iss, file, indent=4)
            
    
    except Exception as err:
        print(err)

get_data()

