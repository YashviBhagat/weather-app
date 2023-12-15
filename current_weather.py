from tkinter import *
import tkinter as tk
import geocoder
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("WEATHER APP")
root.geometry("900x500+300+200")
root.resizable(False,False)
def getWeather():
    try:
        city=textfield.get()
        geolocator = Nominatim(user_agent="geoapiExcercises")
        location = geolocator.geocode(city)

        # get user's current location
        user_location = geocoder.ip('me')
        user_lat = user_location.latlng[0]
        user_lon = user_location.latlng[1]



        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

    # Weather
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a23cadc7cbfa425aba43577f439623ac"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKES",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    # user current location weather
        user_api = "https://api.openweathermap.org/data/2.5/weather?lat="+str(user_lat)+"&lon="+str(user_lon)+"&appid=a23cadc7cbfa425aba43577f439623ac"
        user_json_data = requests.get(user_api).json()
        # user_condition = user_json_data['weather'][0]['main']
        user_temp = int(user_json_data['main']['temp']-273.15)


        cname.config(text=user_location.city)
        t_user.config(text=(user_temp,"°"))
        
        
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")

# Search Box
search_image = PhotoImage(file="search.png")
myimage = Label(image = search_image)
myimage.place(x=20,y=20)

textfield = tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

# logo
logo_img = PhotoImage(file="logo.png")
logo = Label(image=logo_img)
logo.place(x = 150,y = 100)

# Bottom box
Frame_image = PhotoImage(file=" box.png")
frame_myimage = Label(image = Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

# Time
name = Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)
# Label
label1 = Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2 = Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3 = Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4 = Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250) 


w = Label(text=". . .",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h = Label(text=". . .",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d = Label(text=". . .",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p = Label(text=". . .",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)

cname = Label(root,text="Current Location",font=("arial",20,"bold"),fg="black")
cname.place(x=700,y=30)
t_user=Label(root,font=("arial",20),fg="black")
t_user.place(x=720,y=100)
root.mainloop()