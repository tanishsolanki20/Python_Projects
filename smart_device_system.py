from abc import ABC, abstractmethod

 

# Abstract base — all devices must implement these

class Device(ABC):

    def __init__(self, brand, model):

        self.brand  = brand

        self.model  = model

        self.on     = False

 

    @abstractmethod
    def power_on(self):

        pass

 

    @abstractmethod

    def power_off(self):

        pass

 

    def __str__(self):

        status = "ON" if self.on else "OFF"

        return f"{self.brand} {self.model} [{status}]"

 

 

# Mix-in 1 — adds WiFi capability

class WiFiCapable:

    def connect_wifi(self, network):

        print(f"{self.brand} {self.model} connected to {network}")

 

    def disconnect_wifi(self):

        print(f"{self.brand} {self.model} disconnected from WiFi")

 

 

# Mix-in 2 — adds calling capability

class CallCapable:

    def make_call(self, number):

        print(f"{self.brand} {self.model} calling {number}...")

 

    def end_call(self):

        print("Call ended.")

class gps_capable:
    def get_location(self):
        print("The location is pune.")

class Laptop(Device, WiFiCapable):      # Device + WiFi only

    def power_on(self):

        self.on = True

        print(f"{self.brand} {self.model} booting up...")

 

    def power_off(self):

        self.on = False

        print(f"{self.brand} {self.model} shutting down.")

 

 

class SmartPhone(Device, WiFiCapable, CallCapable):  # all three

    def power_on(self):

        self.on = True

        print(f"{self.brand} {self.model} starting up.")

 

    def power_off(self):

        self.on = False

        print(f"{self.brand} {self.model} powering off.")

 

 

class SmartTV(Device, WiFiCapable):     # Device + WiFi only

    def power_on(self):

        self.on = True

        print(f"{self.brand} {self.model} — Welcome!")

 

    def power_off(self):

        self.on = False

        print(f"{self.brand} {self.model} — Goodbye!")

class Smartwatch(Device, CallCapable, gps_capable):
    def power_on(self):
        self.on= True
        print(f"{self.brand} {self.model} powering on.")

    def power_off(self):
        self.off=  False
        print(f"{self.brand} {self.model} powering off.")

    def get_location(self):
        return super().get_location()


laptop = Laptop("Apple", "MacBook")

phone  = SmartPhone("Samsung", "Galaxy S24")

tv     = SmartTV("Sony", "Bravia")

smartwatch= Smartwatch("Noise", "G27")

smartwatch.power_on()


laptop.power_on()

laptop.connect_wifi("HomeNetwork")

print(laptop)

 

phone.power_on()

phone.connect_wifi("HomeNetwork")

phone.make_call("9876543210")

phone.end_call()

print(phone)

 

# All devices in one list — polymorphism via abstract base

devices = [laptop, phone, tv, smartwatch]

print("\n--- All devices ---")

for d in devices:
    d.power_on()
    if isinstance(d, gps_capable):
        d.get_location()
    print(d)


