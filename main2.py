import requests
import config
from _datetime import datetime
from tkinter import *
import webbrowser

# Pixela Habit Graph IDs
PYTHON_CODING = "coding"
SOFTWARE_ENG_STUDY = "engsoft"
PRODUCTION_ENG_STUDY = "engprod"
JOB_APPLICATION = "lookingwork"

# User Authentication
headers = {
    "X-USER-TOKEN": config.PIXELA_TOKEN
}


# Updating a pixel
def update_pixel(habit, quantity):
    today = datetime.now().strftime("%Y%m%d")
    update_pix_endpoint = f"https://pixe.la/v1/users/{config.PIXELA_USERNAME}/graphs/{habit}/{today}"
    update_params = {
        "quantity": quantity,
    }
    response = requests.put(url=update_pix_endpoint, headers=headers, json=update_params)
    print(response.text)

# User Interface
screen = Tk()
screen.title("Habit Tracker")
screen.config(pady=30, padx=30)

canvas = Canvas(width=300, height=300)
image = PhotoImage(file="Vida_fitness_healthy-habits.png")
canvas.create_image(150, 150, image=image)
canvas.grid(column=1, row=0, columnspan=2)

# Radio buttons for selecting habit
habit_label = Label(text="Habit:")
habit_label.grid(column=0, row=1)

habit = StringVar()

python_coding_radio = Radiobutton(text="Python Coding", value=PYTHON_CODING, variable=habit)
python_coding_radio.grid(column=1, row=1)

software_eng_study_radio = Radiobutton(text="Software Eng.", value=SOFTWARE_ENG_STUDY, variable=habit)
software_eng_study_radio.grid(column=2, row=1)

production_eng_study_radio = Radiobutton(text="Production Eng.", value=PRODUCTION_ENG_STUDY, variable=habit)
production_eng_study_radio.grid(column=3, row=1)
job_application_radio = Radiobutton(text="Job Applications", value=JOB_APPLICATION, variable=habit)
job_application_radio.grid(column=4, row=1)


# Display URL of habit graph
def update_graph_label(*args):
    url = f"https://pixe.la/v1/users/wrafasantos/graphs/{habit.get()}.html"
    graph_label.config(text=f"Clik here to check the habit graph.", cursor="hand", font=("", 15, "underline"))
    graph_label.bind("<Button-1>", lambda event: webbrowser.open(url))


habit.trace("w", update_graph_label)

graph_label = Label(text="Select the habit")
graph_label.grid(column=3, row=0, columnspan=2)

qtd_label = Label(text="Quantity:")
qtd_label.grid(column=0, row=2)
qtd_entry = Entry(width=10)
qtd_entry.focus()
qtd_entry.grid(column=1, row=2)
habit_button = Button(text="Add to Tracker", command=lambda: update_pixel(habit.get(), qtd_entry.get()))
habit_button.grid(column=2, row=2)

screen.mainloop()
