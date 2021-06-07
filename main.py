import requests
from tkinter import *
from tkinter import messagebox

class WeatherAppGUI:
    def __init__(self, master):
        # Window setup
        self.master = master
        self.master.geometry('350x440')
        self.master.title("Weather")
        self.master.config(bg='#222')

        # Country code label and entry
        self.lbl_country = Label(self.master, text='Enter country code', font='Garuda 10', bg='#222', fg='#fff')
        self.lbl_country.place(x=10, y=10)
        self.entry_country = Entry(self.master, borderwidth='0')
        self.entry_country.place(x=173, y=16)

        # City label and entry
        self.lbl_city = Label(self.master, text='Enter city', font='Garuda 10', bg='#222', fg='#fff')
        self.lbl_city.place(x=10, y=50)
        self.entry_city = Entry(self.master, borderwidth='0')
        self.entry_city.place(x=173, y=56)

        # get weather button
        self.btn_weather = Button(self.master, activebackground='#3784de', activeforeground='#222', text='Get weather',
                                  bg='#0e0e0e', fg='#3784de', borderwidth=0, relief='solid',
                                  highlightbackground='#3784de', width=43, font='Garuda 10', command=self.get_weather)
        self.btn_weather.place(x=11, y=100)

        # Frame and labels for temperature
        self.frame_temp = Frame(self.master, width=329, bg='#111', height=40)
        self.lbl_temp_head = Label(self.frame_temp, text='Temperature (min/max)', font='Garuda 10', bg='#111',
                                   fg='#fff')
        self.lbl_temp = Label(self.frame_temp, text='', font='Garuda 10', bg='#111', fg='#3784de')
        self.frame_temp.place(x=10, y=170)
        self.lbl_temp_head.place(x=10, y=5)
        self.lbl_temp.place(x=225, y=5)

        # Frame and labels for humidity
        self.frame_hum = Frame(self.master, width=329, bg='#111', height=40)
        self.lbl_hum_head = Label(self.frame_hum, text='Humidity', font='Garuda 10', bg='#111',
                                  fg='#fff')
        self.lbl_hum = Label(self.frame_hum, text='', font='Garuda 10', bg='#111', fg='#3784de')
        self.frame_hum.place(x=10, y=320)
        self.lbl_hum_head.place(x=10, y=5)
        self.lbl_hum.place(x=225, y=5)

        # Frame and labels for wind
        self.frame_wind = Frame(self.master, width=329, bg='#111', height=40)
        self.lbl_wind_head = Label(self.frame_wind, text='Wind', font='Garuda 10', bg='#111',
                                   fg='#fff')
        self.lbl_wind = Label(self.frame_wind, text='', font='Garuda 10', bg='#111', fg='#3784de')
        self.frame_wind.place(x=10, y=270)
        self.lbl_wind_head.place(x=10, y=5)
        self.lbl_wind.place(x=225, y=5)

        # Frame and labels for cloud cover
        self.frame_cloud = Frame(self.master, width=329, bg='#111', height=40)
        self.lbl_cloud_head = Label(self.frame_cloud, text='Cloud cover', font='Garuda 10', bg='#111',
                                    fg='#fff')
        self.lbl_cloud = Label(self.frame_cloud, text='', font='Garuda 10', bg='#111', fg='#3784de')
        self.frame_cloud.place(x=10, y=220)
        self.lbl_cloud_head.place(x=10, y=5)
        self.lbl_cloud.place(x=225, y=5)

        # Clear button
        self.btn_clear = Button(self.master, activebackground='#2CDA9D', activeforeground='#222', text='Clear',
                                bg='#0e0e0e', fg='#2CDA9D', borderwidth=0, relief='solid',
                                highlightbackground='#2CDA9D', width=10, font='Garuda 10', command=self.clear)
        self.btn_clear.place(x=10, y=390)

        # Exit button
        self.btn_exit = Button(self.master, activebackground='#DC143C', activeforeground='#222', text='Exit',
                               bg='#0e0e0e', fg='#DC143C', borderwidth=0, relief='solid',
                               highlightbackground='#DC143C', width=10, font='Garuda 10', command=exit)
        self.btn_exit.place(x=244, y=390)

        self.master.mainloop()

    def get_weather(self):
        try:
            # Get country and city from entry fields
            country = self.entry_country.get()
            city = self.entry_city.get()

            # fetch data from weather api
            api_weather = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country + "&units=metric&appid=953a4a4cddff1086a1171621db392044"
            details = requests.get(api_weather).json()

            # populate temperature label
            temp = "{}/{} °C".format(details["main"]["temp_min"], details["main"]["temp_max"])
            self.lbl_temp.config(text=temp)

            # populate cloud cover label
            self.lbl_cloud.config(text=details["weather"][0]["description"])

            # populate wind speed label
            wind = "{} km/h".format(details["wind"]["speed"])
            self.lbl_wind.config(text=wind)

            # populate humidity label
            humidity = "{}%".format(details["main"]["humidity"])
            self.lbl_hum.config(text=humidity)

        except KeyError:
            messagebox.showwarning("Error", "Incorrect country code or city")

        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "No internet connection")

    def clear(self):
        self.entry_city.delete(0, END)
        self.entry_country.delete(0, END)
        self.entry_country.focus()
        self.lbl_hum.config(text='')
        self.lbl_cloud.config(text='')
        self.lbl_wind.config(text='')
        self.lbl_temp.config(text='')



root = Tk()
WeatherAppGUI(root)
# country = str()
# api_weather = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country + "&units=metric&appid=953a4a4cddff1086a1171621db392044"
# details = requests.get(api_weather).json()
# print(details["main"]["temp"])
