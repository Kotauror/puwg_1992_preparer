#!/usr/bin/env python    
import csv
import pyperclip

def db_prepper(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        lines = []
        for row in csv_reader:
            lines.append([float(row[0]), float(row[1])])
        print(lines)

if __name__ == '__main__':
    db_prepper('sample_wsg84_data.csv')