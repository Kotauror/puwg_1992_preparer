#!/usr/bin/env python    
import csv
import pyperclip

def unpollute_puwg_1992(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        numbers_without_empties = []
        for row in csv_reader:
            if len(row) != 0:
                numbers_without_empties.append(row[0])

        numbers_without_singles = []
        for number in numbers_without_empties:
            if len(number) > 2:
                numbers_without_singles.append(number)

        current_index = 0
        for idx, x in enumerate(numbers_without_singles):
            if current_index <= len(numbers_without_singles):
                print(f'{numbers_without_singles[current_index]} {numbers_without_singles[current_index + 1]}')
                current_index += 2

if __name__ == '__main__':
    unpollute_puwg_1992('sample_polluted_1992_data.csv')