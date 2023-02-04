import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 174
AGE = 26


APP_ID = "6554b672"
API_KEY = "648ff6c773ea235a2f9f0b4b5616bdd3"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/c0a02ecbce47fae002420d60592e2147/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            "canko12",
            "1*23Afs09*",
        )
    )

    print(sheet_response.text)
