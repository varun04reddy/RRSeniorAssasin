import csv

def isDead(player_name, csv_file):
    updated = False

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

        for row in rows:
            if row['Player'] == player_name:
                row['isDead'] = 'Yes'
                updated = True
                break

    if updated:
        with open(csv_file, 'w', newline='') as file:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"{player_name} marked as dead ")
    else:
        print(f"Player {player_name} not found ")

def kills(player_name, kills_count, csv_file):
    updated = False

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

        for row in rows:
            if row['Player'] == player_name:
                current_kills = int(row['Kills'])
                row['Kills'] = str(current_kills + kills_count)
                updated = True
                break

    if updated:
        with open(csv_file, 'w', newline='') as file:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"{kills_count} kills added to {player_name}'s kills count ")
    else:
        print(f"Player {player_name} not found .")


