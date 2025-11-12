thonimport sys
import json
from extractors.zillow_parser import parse_zillow_data
from outputs.exporters import export_to_json, export_to_csv

def main(input_file, output_format="json"):
    try:
        with open(input_file, 'r') as file:
            data = file.read().splitlines()

        properties = []
        for line in data:
            properties.append(parse_zillow_data(line))

        if output_format == "json":
            export_to_json(properties, "output.json")
        elif output_format == "csv":
            export_to_csv(properties, "output.csv")
        else:
            print("Unsupported output format")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python runner.py <input_file> [output_format]")
    else:
        input_file = sys.argv[1]
        output_format = sys.argv[2] if len(sys.argv) > 2 else "json"
        main(input_file, output_format)