import os
import json
import csv
import pickle

def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)

            result = {
                "Path":f'{directory}/{os.path.relpath(file_path, directory)}',
                "Type": "File",
                "Size": file_size
            }

            results.append(result)

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_size = get_directory_size(dir_path)

            result = {
                "Path": f'{directory}/{os.path.relpath(dir_path, directory)}',
                "Type": "Directory",
                "Size": dir_size
            }

            results.append(result)

    return results


def get_directory_size(directory):
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            total_size += os.path.getsize(file_path)

    return total_size


def save_results_to_json(results, file_path):
    with open(file_path, "w") as file:
        json.dump(results, file)


def save_results_to_csv(results, file_path):
    with open(file_path, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["Path", "Type", "Size"])
        writer.writeheader()
        writer.writerows(results)


def save_results_to_pickle(results, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(results, file)