"""
Created By: Ubaidullah Effendi-Emjedi
Date: 27 October 2019
"""

import csv
import json

from .convert_to_type import adv_type_conversion


def convert_csv_to_json(csv_path="", json_path="", allow_empty_strings=True, allow_null_values=True):
    try:
        data = []
        with open(csv_path, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                for key in row.keys():
                    row[key] = adv_type_conversion(row[key], allow_empty_strings, allow_null_values)
                data.append(row)

        with open(json_path if json_path != "" else "parse.json", 'w') as jsonFile:
            jsonFile.write(json.dumps(data, indent=4))

        print("Conversion Successful!")

    except Exception as error:
        print(error)


def convert_csv_to_json_with_uid(csv_path="", json_path="", column_tag="", allow_empty_strings=True,
                                 allow_null_values=True):
    try:
        data = {}
        with open(csv_path, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                for key in row.keys():
                    row[key] = adv_type_conversion(row[key], allow_empty_strings, allow_null_values)
                key = row[column_tag]
                data[key] = row

        with open(json_path if json_path != "" else "parse.json", 'w') as jsonFile:
            jsonFile.write(json.dumps(data, indent=4))

        print("Conversion Successful!")

    except Exception as error:
        print(error)


def convert_csv_to_json_with_root(csv_path="", json_path="", root_key="", allow_empty_strings=True,
                                  allow_null_values=True):
    try:
        data = []
        rooted_data = {}
        with open(csv_path, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                for key in row.keys():
                    row[key] = adv_type_conversion(row[key], allow_empty_strings, allow_null_values)
                data.append(row)

        rooted_data[root_key] = data
        with open(json_path if json_path != "" else "parse.json", 'w') as jsonFile:
            jsonFile.write(json.dumps(data if root_key == "" else rooted_data, indent=4))

        print("Conversion Successful!")

    except Exception as error:
        print(error)


def convert_csv_to_json_with_root_and_uid(csv_path="", json_path="", root_key="", column_tag="",
                                          allow_empty_strings=True, allow_null_values=True):
    try:
        data = {}
        rooted_data = {}
        with open(csv_path, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                for key in row.keys():
                    row[key] = adv_type_conversion(row[key], allow_empty_strings, allow_null_values)
                key = row[column_tag]
                data[key] = row

        rooted_data[root_key] = data
        with open(json_path if json_path != "" else "parse.json", 'w') as jsonFile:
            jsonFile.write(json.dumps(data if root_key == "" else rooted_data, indent=4))

        print("Conversion Successful!")

    except Exception as error:
        print(error)
