from entry import WeatherEntry

class WeatherLog:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry: WeatherEntry):
        self.entries.append(entry)

    def list_entries(self):
        return self.entries

    def find_by_date(self, date_str: str):
        results = [e for e in self.entries if e.date == date_str]
        return results