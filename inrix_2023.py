from bs4 import BeautifulSoup
import csv
import os

# Output file
output_csv = "result.csv"

# Open the CSV for writing once
with open(output_csv, "w", newline="", encoding="utf-8") as f_out:
    writer = csv.writer(f_out)
    writer.writerow(["Urban Area", "Hours Lost", "Change from 2023"])

    # Loop through files p1.txt, p2.txt, ...
    index = 1
    while True:
        file_name = f"p{index}.txt"
        if not os.path.exists(file_name):
            break  # Stop when no more files

        print(f"Processing {file_name}...")

        with open(file_name, "r", encoding="utf-8") as f_in:
            soup = BeautifulSoup(f_in, "html.parser")

        rows = soup.find_all("div", {"role": "row"})

        for row in rows:
            urban_area_div = row.find("div", {"col-id": "urban_area"})
            hours_lost_div = row.find("div", {"col-id": "2024_delay"})
            change_div = row.find("div", {"col-id": "delay_change_percent"})

            if urban_area_div and hours_lost_div and change_div:
                urban_area = urban_area_div.get_text(strip=True)
                hours_lost = hours_lost_div.get_text(strip=True)
                change = change_div.get_text(strip=True)
                writer.writerow([urban_area, hours_lost, change])

        index += 1

print(f"Done. Combined result saved to {output_csv}")