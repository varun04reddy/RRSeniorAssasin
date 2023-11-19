import csv
import random

def assign_targets(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    random.shuffle(rows)

    for i in range(len(rows)):
        current_row = rows[i]
        current_team = current_row['Team']
        target_row = rows[(i + 1) % len(rows)]

        while target_row['Team'] == current_team or target_row['isDead'] == 'Yes':
            target_row = rows[(i + 1) % len(rows)]
        
        current_row['Target'] = target_row['Player']
        current_row['Target Email'] = target_row['Email']

    with open(csv_file, 'w', newline='') as file:
        fieldnames = reader.fieldnames + ['Target', 'Target Email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Targets assigned successfully!")

csv_file_path = 'C:\\Users\\varun\\OneDrive\\Documents\\responses.csv'
assign_targets(csv_file_path)
