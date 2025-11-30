class WeatherStatisticsTP:
    @staticmethod
    def maximum_temperature(entries):
        if not entries:
            return None

        temps = (e.max_temp for e in entries)
        return max(temps)

    def minimum_temperature(entries):
        if not entries:
            return None

        temps = (e.min_temp for e in entries)
        return min(temps)