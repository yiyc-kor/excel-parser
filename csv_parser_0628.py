#! /usr/bin/env python

import argparse
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


def check_csv(input_path):
    code_list = []
    item_list = []
    p = re.compile('[^A-Za-z0-9\-\/\(\)\&\"\.\<\>\:\;\'\=\*\%×\@\?\#＃ ？]')
    with open(input_path, 'r', encoding="utf-8") as f:
        for i, line in enumerate(f):
            sp = line.split(',')
            code = sp[0]
            item = ' '.join(sp[1:])
            item = item.strip().strip('\"')
            # if p.search(item) is not None:
            #     print("##### " + str(i) + "\t" + "wired character detected:\t" + item)
            code_list.append(code)
            item_list.append(item)
    return code_list, item_list


def main():
    parser = argparse.ArgumentParser(description="Parsing Csv File 2019-06-28")

    # I&O file
    parser.add_argument('--input_path', dest="input_path", type=str, default="./data/data.csv",
                        help="Input file path")

    parser.add_argument('--output_path', dest="output_path", type=str, default="./data/output.csv",
                        help="Output file path")

    flags, unused_flags = parser.parse_known_args()

    code_list, item_list = check_csv(flags.input_path)

    parse_list(code_list, item_list)


if __name__ == '__main__':
    main()
