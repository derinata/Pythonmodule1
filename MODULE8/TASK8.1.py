import csv

def fetch_airport_info_from_csv(icao_code, filename="airports.csv"):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ident'].strip().upper() == icao_code.upper():
                    print(f"Airport name: {row['name']}")
                    print(f"Location: {row['municipality']}")
                    return
            print("No airport found with that ICAO code.")
    except FileNotFoundError:
        print("CSV file not found.")
    except KeyError as e:
        print(f"Missing expected column in CSV: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
icao_input = input("Enter ICAO code: ").strip()
fetch_airport_info_from_csv(icao_input)







