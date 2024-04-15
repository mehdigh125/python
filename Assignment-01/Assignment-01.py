from tkinter import *
from requests import get as getWeather
import json
from datetime import datetime
from PIL import ImageTk, Image
import os

# Initialize Window
root = Tk()
root.geometry("500x500")  # size of the window by default
root.resizable(0, 0)  # to make the window size fixed
# title of our window
root.title("Weather App - AskPython.com")
# ----------------------Functions to fetch and display weather info
city_value = StringVar()


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def showWeather():
    city_name = city_value.get()
    response = getWeather("https://goweather.herokuapp.com/weather/" + city_name)
    tfield.delete("1.0", "end")
    print(response.status_code)
    if response.status_code != 200:
        tfield.insert(INSERT, "connection failed")
    if response.status_code == 200:

        weather_info = json.loads(response.text)
        print(weather_info)
        temperature = weather_info.get("temperature")
        wind = weather_info.get("wind")
        description = weather_info.get("description")
        forecast = weather_info.get("forecast")
        day1 = forecast[0]
        day2 = forecast[1]
        day3 = forecast[2]
        temperature1 = day1.get("temperature")
        wind1 = day1.get("wind")
        temperature2 = day2.get("temperature")
        wind2 = day2.get("wind")
        temperature3 = day3.get("temperature")
        wind3 = day3.get("wind")

        weather = f"Weather of: {city_name}\n\n Temperature :{temperature}, wind:{wind}, description:{description}\n\n day1:Temperature:{temperature1}, wind:{wind1}\n\n day2:Temperature:{temperature2}, wind:{wind2}\n\n day3:Temperature:{temperature3}, wind:{wind3}"
        tfield.insert(INSERT, weather)
              
        if description == "Partly cloudy":
            imagePath = PhotoImage(file="images/partlycloudy.png")
        elif description == "sunny":
            imagePath = PhotoImage(file="images/sunny.png")
        elif description == "Rainny":
            imagePath = PhotoImage(file="images/rainy.png")
        elif description == "Cloudy":
            imagePath = "images/Cloudy.png"
        canvas = Canvas(root, width=500, height=500)
        canvas.create_image(250, 53, image=imagePath)
        canvas.pack()
        root.mainloop()


    # ------------------------------Frontend part of code - Interface


city_head = Label(root, text='Enter City Name', font='Arial 12 bold').pack(pady=10)  # to generate label heading

inp_city = Entry(root, textvariable=city_value, width=24, font='Arial 14 bold').pack()

Button(root, command=showWeather, text="Check Weather", font="Arial 10", bg='lightblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

# to show output

weather_now = Label(root, text="The Weather is:", font='arial 12 bold').pack(pady=10)

tfield = Text(root, width=65, height=10, font='arial 12 bold')
tfield.pack()

root.mainloop()

