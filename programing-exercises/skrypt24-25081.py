# skrypt24-25081.py

import csv

def create_pc_csv(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['pc_name', 'ip'])
        for i in range(1, 101):
            pc_name = f"P{i}"
            ip = f"172.30.2.{i}"
            writer.writerow([pc_name, ip])

if __name__ == '__main__':
    create_pc_csv('pc.csv')
