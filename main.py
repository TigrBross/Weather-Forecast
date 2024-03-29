import PIL.Image
from customtkinter import *
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz


city = None


def getweather(cty=None):
    global city, this_day_lbl, one_day_lbl, two_day_lbl, three_day_lbl, four_day_lbl, five_day_lbl, six_day_lbl
    try:
        if not cty:
            city = search_entry.get()
        if cty:
            city = cty
        geolocator = Nominatim(user_agent="main")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        timezone_lbl.configure(text=result)
        long_lat_lbl.configure(text=f"{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        main_time = local_time.strftime("%I:%M:%p")
        time_lbl.configure(text=main_time)

        latitude = location.latitude
        longitude = location.longitude

        # api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=8a8233bc1cd8a787b2535ea0ce0a2330&units=metric"
        # api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8a8233bc1cd8a787b2535ea0ce0a2330&units=metric"
        api = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid=7b8e0713fae80f87ecee8ad094dac405&units=metric&cnt=7"
        json_data = requests.get(api).json()

        temp = json_data['list'][0]['main']['temp']
        t.configure(text=f"{temp}C°")
        humidity = json_data['list'][0]['main']['humidity']
        h.configure(text=f"humidity: {humidity}%")
        pressure = json_data['list'][0]['main']['pressure']
        p.configure(text=f"pressure: {pressure}hPa")
        wind_speed = json_data['list'][0]['wind']['speed']
        w.configure(text=f"wind_speed: {wind_speed}m/s")
        description = json_data['list'][0]['weather'][0]['description']
        d.configure(text=f"description: {description}")

        this = datetime.now()
        this_weekday_lbl.configure(text=this.strftime("%A"))

        one_day = this + timedelta(days=1)
        one_weekday_lbl.configure(text=one_day.strftime("%A"))

        two_day = this + timedelta(days=2)
        two_weekday_lbl.configure(text=two_day.strftime("%A"))

        three_day = this + timedelta(days=3)
        three_weekday_lbl.configure(text=three_day.strftime("%A"))

        four_day = this + timedelta(days=4)
        four_weekday_lbl.configure(text=four_day.strftime("%A"))

        five_day = this + timedelta(days=5)
        five_weekday_lbl.configure(text=five_day.strftime("%A"))

        six_day = this + timedelta(days=6)
        six_weekday_lbl.configure(text=six_day.strftime("%A"))

        this_max = json_data['list'][0]['main']['temp_max']
        this_min = json_data['list'][0]['main']['temp_min']
        this_icon = json_data['list'][0]['weather'][0]['icon']
        this_day_icon_lbl.configure(text=f"max: {this_max}C°\nmin: {this_min}C°",
                                    image=CTkImage(light_image=PIL.Image.open(f"Images/{this_icon}.png"), size=(100, 100)),
                                    compound=LEFT)

        one_max = json_data['list'][1]['main']['temp_max']
        one_min = json_data['list'][1]['main']['temp_min']
        one_icon = json_data['list'][1]['weather'][0]['icon']
        one_day_icon_lbl.configure(text=f"max: {one_max}C°\nmin: {one_min}C°",
                                   image=CTkImage(light_image=PIL.Image.open(f"Images/{one_icon}.png"), size=(70, 70)),
                                   compound=BOTTOM)

        two_max = json_data['list'][2]['main']['temp_max']
        two_min = json_data['list'][2]['main']['temp_min']
        two_icon = json_data['list'][2]['weather'][0]['icon']
        two_day_icon_lbl.configure(text=f"max: {two_max}C°\nmin: {two_min}C°",
                                   image=CTkImage(light_image=PIL.Image.open(f"Images/{two_icon}.png"), size=(70, 70)),
                                   compound=BOTTOM)

        three_max = json_data['list'][3]['main']['temp_max']
        three_min = json_data['list'][3]['main']['temp_min']
        three_icon = json_data['list'][3]['weather'][0]['icon']
        three_day_icon_lbl.configure(text=f"max: {three_max}C°\nmin: {three_min}C°",
                                     image=CTkImage(light_image=PIL.Image.open(f"Images/{three_icon}.png"), size=(70, 70)),
                                     compound=BOTTOM)

        four_max = json_data['list'][4]['main']['temp_max']
        four_min = json_data['list'][4]['main']['temp_min']
        four_icon = json_data['list'][4]['weather'][0]['icon']
        four_day_icon_lbl.configure(text=f"max: {four_max}C°\nmin: {four_min}C°",
                                    image=CTkImage(light_image=PIL.Image.open(f"Images/{four_icon}.png"), size=(70, 70)),
                                    compound=BOTTOM)

        five_max = json_data['list'][5]['main']['temp_max']
        five_min = json_data['list'][5]['main']['temp_min']
        five_icon = json_data['list'][5]['weather'][0]['icon']
        five_day_icon_lbl.configure(text=f"max: {five_max}C°\nmin: {five_min}C°",
                                    image=CTkImage(light_image=PIL.Image.open(f"Images/{five_icon}.png"), size=(70, 70)),
                                    compound=BOTTOM)

        six_max = json_data['list'][6]['main']['temp_max']
        six_min = json_data['list'][6]['main']['temp_min']
        six_icon = json_data['list'][6]['weather'][0]['icon']
        six_day_icon_lbl.configure(text=f"max: {six_max}C°\nmin: {six_min}C°",
                                   image=CTkImage(light_image=PIL.Image.open(f"Images/{six_icon}.png"), size=(70, 70)),
                                   compound=BOTTOM)
    except AttributeError:
        messagebox.showerror("Error", "Input correct city name!")


def focus_in(event):
    if event:
        pass
    search_entry.delete(0, END)


def focus_out(event):
    if event:
        pass
    search_entry.delete(0, END)
    search_entry.insert(0, "Enter your city name")


root = CTk()
root.geometry("1020x500+250+150")
root.resizable(False, False)
root.title("Weather Forecast")
root.config(bg="#8fe0ff")


frame_label = CTkLabel(root, fg_color="#282829", width=1020, height=200, text="")
frame_label.place(x=0, y=300)

this_day_lbl = CTkLabel(frame_label, text="",
                        image=CTkImage(light_image=PIL.Image.open("Images/Rounded Rectangle 2.png"), size=(230, 150)))
this_day_lbl.place(x=30, y=25)

one_day_lbl = CTkLabel(frame_label, text="",
                       image=CTkImage(light_image=PIL.Image.open("Images/Rounded Rectangle 2 copy.png"),
                                      size=(100, 150)))
one_day_lbl.place(x=300, y=25)

two_day_lbl = CTkLabel(frame_label, text="",
                       image=CTkImage(light_image=PIL.Image.open("Images/Rounded Rectangle 2 copy.png"),
                                      size=(100, 150)))
two_day_lbl.place(x=420, y=25)

three_day_lbl = CTkLabel(frame_label, text="",
                         image=CTkImage(light_image=PIL.Image.open("Images/Rounded Rectangle 2 copy.png"),
                                        size=(100, 150)))
three_day_lbl.place(x=540, y=25)

four_day_lbl = CTkLabel(frame_label, text="",
                        image=CTkImage(light_image=PIL.Image.open("Images/Rounded Rectangle 2 copy.png"),
                                       size=(100, 150)))
four_day_lbl.place(x=660, y=25)

five_day_lbl = CTkLabel(frame_label, text="",
                        image=CTkImage(light_image=PIL.Image.open("Images/Rounded Rectangle 2 copy.png"),
                                       size=(100, 150)))
five_day_lbl.place(x=780, y=25)

six_day_lbl = CTkLabel(frame_label, text="",
                       image=CTkImage(light_image=PIL.Image.open("Images/Rounded Rectangle 2 copy.png"),
                                      size=(100, 150)))
six_day_lbl.place(x=900, y=25)

search_bar = CTkLabel(root, text="",
                      image=CTkImage(light_image=PIL.Image.open("Images/search bar.png"), size=(450, 60)),
                      bg_color="#8fe0ff")
search_bar.place(x=550, y=187)
search_btn = CTkButton(search_bar, width=45, height=45, text="",
                       image=CTkImage(light_image=PIL.Image.open("Images/search.png"), size=(45, 45)),
                       fg_color="#203243", bg_color="#203243", hover_color="#182630", command=getweather)
search_btn.place(x=370, y=4)
search_entry = CTkEntry(search_bar, font=("Sitka Heading", 27, "bold"), width=350, height=35, text_color="#75b4e3",
                        fg_color="#203243", bg_color="#203243", border_width=0)
search_entry.place(x=10, y=7)

search_entry.insert(0, "Enter your city name")
search_entry.bind('<FocusIn>', focus_in)
search_entry.bind('<FocusOut>', focus_out)
search_entry.bind("<Return>", getweather)

other_parameters = CTkLabel(root, bg_color="#8fe0ff", fg_color="#282829", width=450, height=200, text="",
                            corner_radius=15)
other_parameters.place(x=20, y=50)

t = CTkLabel(root, bg_color="#8fe0ff", text_color="#2b235a", font=("Candara", 60, "bold"), text="")
t.place(x=820, y=100)
h = CTkLabel(other_parameters, bg_color="#282829", fg_color="#282829", font=("Candara", 30, "bold"), text="",
             corner_radius=15, text_color="#b8b8b8")
h.place(x=20, y=10)
p = CTkLabel(other_parameters, bg_color="#282829", fg_color="#282829", font=("Candara", 30, "bold"), text="",
             corner_radius=15, text_color="#b8b8b8")
p.place(x=20, y=60)
w = CTkLabel(other_parameters, bg_color="#282829", fg_color="#282829", font=("Candara", 30, "bold"), text="",
             corner_radius=15, text_color="#b8b8b8")
w.place(x=20, y=110)
d = CTkLabel(other_parameters, bg_color="#282829", fg_color="#282829", font=("Candara", 30, "bold"), text="",
             corner_radius=15, text_color="#b8b8b8")
d.place(x=20, y=155)

time_lbl = CTkLabel(root, bg_color="#8fe0ff", text_color="#2b235a", font=("Candara", 60, "bold"), text="")
time_lbl.place(x=550, y=100)

timezone_lbl = CTkLabel(root, bg_color="#8fe0ff", text_color="#2b235a", font=("Candara", 30, "bold"), text="")
timezone_lbl.place(x=630, y=10)

long_lat_lbl = CTkLabel(root, bg_color="#8fe0ff", text_color="#2b235a", font=("Candara", 20, "bold"), text="")
long_lat_lbl.place(x=630, y=42)


this_weekday_lbl = CTkLabel(this_day_lbl, text="", font=("Candara", 25, "bold"))
this_weekday_lbl.place(x=45, y=10)

one_weekday_lbl = CTkLabel(one_day_lbl, text="", font=("Candara", 20, "bold"))
one_weekday_lbl.place(x=10, y=2)

two_weekday_lbl = CTkLabel(two_day_lbl, text="", font=("Candara", 20, "bold"))
two_weekday_lbl.place(x=10, y=2)

three_weekday_lbl = CTkLabel(three_day_lbl, text="", font=("Candara", 20, "bold"))
three_weekday_lbl.place(x=10, y=2)

four_weekday_lbl = CTkLabel(four_day_lbl, text="", font=("Candara", 20, "bold"))
four_weekday_lbl.place(x=10, y=2)

five_weekday_lbl = CTkLabel(five_day_lbl, text="", font=("Candara", 20, "bold"))
five_weekday_lbl.place(x=10, y=2)

six_weekday_lbl = CTkLabel(six_day_lbl, text="", font=("Candara", 20, "bold"))
six_weekday_lbl.place(x=10, y=2)


this_day_icon_lbl = CTkLabel(this_day_lbl, text="", font=("Candara", 22, "bold"))
this_day_icon_lbl.place(x=5, y=40)


one_day_icon_lbl = CTkLabel(one_day_lbl, text="",
                            font=("Candara", 18, "bold"))
one_day_icon_lbl.place(x=3, y=35)


two_day_icon_lbl = CTkLabel(two_day_lbl, text="",
                            font=("Candara", 18, "bold"))
two_day_icon_lbl.place(x=3, y=35)


three_day_icon_lbl = CTkLabel(three_day_lbl, text=f"",
                              font=("Candara", 18, "bold"))
three_day_icon_lbl.place(x=3, y=35)


four_day_icon_lbl = CTkLabel(four_day_lbl, text="",
                             font=("Candara", 18, "bold"))
four_day_icon_lbl.place(x=3, y=35)


five_day_icon_lbl = CTkLabel(five_day_lbl, text="",
                             font=("Candara", 18, "bold"))
five_day_icon_lbl.place(x=3, y=35)


six_day_icon_lbl = CTkLabel(six_day_lbl, text="",
                            font=("Candara", 18, "bold"))
six_day_icon_lbl.place(x=3, y=35)


getweather("yerevan")
root.mainloop()
