import requests
from tkinter import *

ip = ""


def load_info():
    global ip
    ip = entry.get()
    api = "https://vpnapi.io/api/"+ip+"?key=bb9a8748de52434dba5d5238c73fc4f3"
    response = requests.get(api).json()
    label.config(text="IP: " + response["ip"] + "\n"+"\n" +
                 "vpn: " + str(response["security"]["vpn"])+"\n" +
                 "Proxy: " + str(response["security"]["proxy"]) + "\n" +
                 "Longitude: " + response["location"]['longitude'] + "\n" +
                 "Latittude: " + response["location"]['latitude'] + "\n" +
                 "Time_Zone: " + response["location"]['time_zone'] + "\n")


api = "https://vpnapi.io/api/"+ip+"?key=bb9a8748de52434dba5d5238c73fc4f3"


response = requests.get(api).json()
print(response)

window = Tk()
window.title("VPN proxy detetction app")
window.geometry("500x500")


entry = Entry(window, width=40, font=("Arial", 30))
entry.pack(pady=25)

button = Button(window, text="LOAD", font=(
    "BELl MT", 25), command=load_info, width=7)
button.pack()

label = Label(window, font=("Arial", 25))
label.pack()

window.mainloop()
