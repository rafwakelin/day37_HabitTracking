import requests
import config
from _datetime import datetime

# Pixela Habit Graphs ID
PYTHON_CODING = "coding"
SOFTWARE_ENG_STUDY = "engsoft"
PRODUCTION_ENG_STUDY = "engprod"
JOB_APPLICATION = "lookingwork"

# User Authentication
headers = {
    "X-USER-TOKEN": config.PIXELA_TOKEN
}
# Setting up today's date and formatting in Pixela's requested format
today = datetime.now().strftime("%Y%m%d")

# Creating a Pixela Account
pixela_end_point = "https://pixe.la/v1/users"
pixela_params = {
    "token": config.PIXELA_TOKEN,
    "username": config.PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_end_point, json=pixela_params)
# print(response.text)

# Creating a graph in Pixela
graph_end_point = f"{pixela_end_point}/{config.PIXELA_USERNAME}/graphs"
graph_params = {
    "id": "lookingwork",
    "name": "Applications Sent",
    "unit": "commit",
    "type": "int",
    "color": "kuro",
}
# response = requests.post(url=graph_end_point, json=graph_params, headers=headers)
# print(response.text)

# Adding a pixel to the tracker

add_pixel_end_point = f"https://pixe.la/v1/users/{config.PIXELA_USERNAME}/graphs/{PYTHON_CODING}"
add_pix_params ={
    "date": today,
    "quantity": "4.0",
}
response = requests.post(url=add_pixel_end_point, headers=headers, json=add_pix_params)
print(response.text)

# Updating a pixel
update_pix_endpoint = f"{add_pixel_end_point}/{today}"
update_params = {
    "quantity": "3.0"
}
# response = requests.put(url=update_pix_endpoint, headers=headers, json=update_params)
# print(response.text)

# Deleting a pixel
# response = requests.delete(url=update_pix_endpoint, headers=headers)
# print(response.text)
