from entry import WeatherEntry
from log import WeatherLog
from statistics import WeatherStatisticsTP
from helpers import print_header

def main():
    log = WeatherLog()

    while True:
        print_header("Időjárás Napló")
        print("1 – Új bejegyzés rögzítése")
        print("2 – Bejegyzések listázása")
        print("3 – Keresés dátum alapján")
        print("4 – Legmagasabb hőmérséklet")
        print("5 - Legalacsonyabb hőmérséklet")

        print("0 – Kilépés")

        choice = input("Választás: ")

        if choice == "1":
            date = input("Dátum (YYYY-MM-DD): ")
            min_temp = float(input("Minimum hőmérséklet: "))
            max_temp = float(input("Maximum hőmérséklet: "))

            try:
                entry = WeatherEntry(date, min_temp, max_temp)
                log.add_entry(entry)
                print("Bejegyzés rögzítve!")
            except ValueError as e:
                print("Hiba:", e)

        elif choice == "2":
            print_header("Bejegyzések")
            entries = log.list_entries()
            if not entries:
                print("Nincs rögzített adat.")
            else:
                for e in entries:
                    print(e)

        elif choice == "3":
            date = input("Keresett dátum: ")
            results = log.find_by_date(date)

            if results:
                print_header("Találatok")
                for r in results:
                    print(r)
            else:
                print("Nem található ilyen dátum.")

        elif choice == "4":
            max = WeatherStatisticsTP.maximum_temperature(log.entries)
            if max is None:
                print("Nincs elég adat.")
            else:
                print(f"Legmagasabb: {max:}°C")

        elif choice == "5":
            min = WeatherStatisticsTP.minimum_temperature(log.entries)
            if min is None:
                print("Nincs elég adat.")
            else:
                print(f"Legalacsonyabb: {min:}°C")

        elif choice == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás!")


if __name__ == "__main__":
    main()