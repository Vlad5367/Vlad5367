import requests
from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry, CTkMessagebox
class WeatherApp(CTk):
    def __init__(self):
        super().__init__()
        self.title('Погода')
        self.geometry("400x250")
        self.city_label = CTkLabel(self, text="Город:")
        self.city_label.pack(pady=5)
        self.city_entry = CTkEntry(self)
        self.city_entry.pack(pady=5)
        self.get_weather_button = CTkButton(self, text="Погода в указанном городе", command=self.get_weather_by_city)
        self.get_weather_button.pack(pady=5)
        self.get_current_location_button = CTkButton(self, text="Погода в моем городе", command=self.get_weather_by_current_location)
        self.get_current_location_button.pack(pady=5)
        self.weather_display = CTkLabel(self, text="", font=("Arial", 12))
        self.weather_display.pack(pady=5)
    def get_weather_by_city(self):
        city = self.city_entry.get()
        if not city:
            CTkMessagebox.showerror("Ошибка", "Введите название города")
            return
        self.get_weather(city)
    def get_weather_by_current_location(self):
        try:
            response = requests.get("https://api64.ipify.org?format=json")
            ip_data = response.json()
            ip_address = ip_data["ip"]
            response = requests.get(f"https://ipinfo.io/{ip_address}/json")
            location_data = response.json()
            city = location_data.get("city")
            if not city:
                raise ValueError("Город не найден")
            self.get_weather(city)
        except Exception as e:
            self.weather_display.configure(text="Ошибка при получении погоды: " + str(e))
    def get_weather(self, city):
        try:
            api_key = "b11511ebe34b7d58c3ea8a0e91653b8c"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            weather_description = data['weather'][0]['description'].capitalize()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            weather_info = f"Погода в {city}: {weather_description}\nТемпература: {temperature}°C\nВлажность: {humidity}%\nСкорость ветра: {wind_speed} м/c"
            self.weather_display.configure(text=weather_info)
        except Exception as e:
            self.weather_display.configure(text="Ошибка при получении погоды: " + str(e))
if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
