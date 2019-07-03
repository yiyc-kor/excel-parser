#! /usr/bin/env python

import argparse
import csv
import re


def parse_list(code_list, item_list):
    whole_zip = zip(code_list, item_list)
    for i, line in enumerate(whole_zip):
        item = line[1]
        item = re.sub(r'[^A-Za-z0-9\-]', ' ', item)
        item = ' '.join(x.strip('-') for x in item.split())
        item = ' '.join(x for x in item.split() if len(x) > 1)
        if item == '':
            whole_zip.pop(i)
    print(whole_zip)


def save_separated(code_list, item_list, code_path, item_path):
    with open(code_path, 'w', encoding="utf-8") as f:
        for line in code_list:
            f.write(line + '\n')
    with open(item_path, 'w', encoding="utf-8") as f:
        for line in item_list:
            f.write(line + '\n')
    return 0


def separate_data(input_path):
    code_list = []
    item_list = []
    with open(input_path, 'r', encoding="utf-8") as f:
        rdr = csv.reader(f)
        for i, line in enumerate(rdr):
            code = line[0]
            item = ' '.join(line[1:])
            code_list.append(str(code).strip())
            item_list.append(str(item).strip())
    return code_list, item_list


def main():
    parser = argparse.ArgumentParser(description="Parsing Csv File 2019-06-28")

    # options
    parser.add_argument('--separate_csv', dest="separate_csv", type=bool, default=False, nargs='?', const=True,
                        help="Separate csv")

    parser.add_argument('--save_separated', dest="save_separated", type=bool, default=False, nargs='?', const=True,
                        help="Save separated csv")

    # I&O file
    parser.add_argument('--input_csv_path', dest="input_csv_path", type=str, default="./data/data.csv",
                        help="Input csv data file path")

    parser.add_argument("--output_code_path", dest="output_code_path", type=str, default="./data/output_code.txt",
                        help="Output code file path")

    parser.add_argument("--output_item_path", dest="output_item_path", type=str, default="./data/output_item.txt",
                        help="Output item file path")

    parser.add_argument('--output_path', dest="output_path", type=str, default="./data/output.csv",
                        help="Output file path")

    flags, unused_flags = parser.parse_known_args()

    if flags.separate_csv:
        code_list, item_list = separate_data(flags.input_csv_path)

    if flags.save_separated and flags.separate_csv:
        save_separated(code_list, item_list, flags.output_code_path, flags.output_item_path)

    #parse_list(code_list, item_list)

    return 1


if __name__ == '__main__':
    main()
