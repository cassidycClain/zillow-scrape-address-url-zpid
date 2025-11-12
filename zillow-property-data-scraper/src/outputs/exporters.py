thonimport json
import csv

def export_to_json(data, filename):
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data exported to {filename}")
    except Exception as e:
        print(f"Error exporting to JSON: {e}")

def export_to_csv(data, filename):
    try:
        keys = data[0].keys() if data else []
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data exported to {filename}")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")