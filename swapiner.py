#!/usr/bin/env python    
import csv

def swapiner(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        line_count = 0
        for row in csv_reader:
            if row[1] == "0.0":
                if line_count != 0:
                    break
                line_count += 1
            else:
                print(f'{row[1]} {row[0]}')
                line_count += 1

if __name__ == '__main__':
    swapiner('sample_data.csv')