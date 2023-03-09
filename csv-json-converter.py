import csv 
import json 
import pandas as pd

def csv_to_json(csv_file_path, json_file_path):
    json_array = []
      
    with open(csv_file_path, encoding='utf-8') as csvf: 
        csv_reader = csv.DictReader(csvf) 

        for row in csv_reader:
            json_array.append(row)
  
    with open(json_file_path, 'w', encoding='utf-8') as jsonf: 
        json_string = json.dumps(json_array, indent=4)
        jsonf.write(json_string)

def json_to_csv(json_file_path, csv_file_path):

    with open(json_file_path, encoding='utf-8') as f:
        jsonf = pd.read_json(f)
    
    jsonf.to_csv(csv_file_path, encoding='utf-8', index=False)

def main():          
    csv_file_path = r'sample.csv'
    json_file_path = r'sample.json'
    csv_to_json(csv_file_path, json_file_path)
    json_to_csv(json_file_path, csv_file_path)


if __name__ == "__main__":
    main()
