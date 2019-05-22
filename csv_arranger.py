#! /usr/bin/env python

import argparse


def arrange_csv(csv_path, output_path):
    g = open(output_path, 'w', encoding="utf-8")

    with open(csv_path, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            sp = line.split(',', 1)
            sp[1] = sp[1][1:]
            sp[1] = sp[1].replace("\"", "\"\"")

            sp[1] = "\"" + sp[1].strip() + "\"\n"
            # print(sp[1])
            g.write(sp[0] + "," + sp[1])


def main():
    parser = argparse.ArgumentParser(description="Arrange Csv File")

    # I&O file
    parser.add_argument('--csv_path', dest="csv_path", type=str, default="./data/data.csv",
                        help="Input file path")

    parser.add_argument('--output_path', dest="output_path", type=str, default="./data/output.csv",
                        help="Output file path")

    args = parser.parse_args()

    arrange_csv(args.csv_path, args.output_path)


if __name__ == '__main__':
    main()
