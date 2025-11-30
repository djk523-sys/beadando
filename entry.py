from datetime import datetime

class WeatherEntry:
    def __init__(self, date_str: str, min_temp: float, max_temp: float):

        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Hibás dátumformátum! (Helyes: YYYY-MM-DD)")

        if min_temp > max_temp:
            raise ValueError("A minimum hőmérséklet nem lehet nagyobb, mint a maximum!")

        self.date = date_str
        self.min_temp = min_temp
        self.max_temp = max_temp

    def __str__(self):
        return f"{self.date} | {self.min_temp}°C / {self.max_temp}°C "