#!/usr/bin/env python3

from PIL import Image, ImageDraw
import argparse, os

# Amount in percent
funding_minimum = 12000
funding_target = 40000

RED = "#ff7c78"
GREEN = "#64d498"
WIDTH, HEIGHT = 250, 250


def read_income(filename):
    with open(filename) as fh:
        income = fh.read()
    income = (line.split() for line in income.strip().splitlines())
    income = (line for line in income if len(line) == 5)
    income = [[line[0],
               int(line[1]), float(line[2]),
               int(line[3]), float(line[4])]
              for line in income]
    amount = sum(l[2] for l in income[3:]) + sum(l[4] for l in income[3:])
    return amount, income


def gen_image(filename, percent_funded):
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    draw.rectangle(((0,0), (WIDTH, HEIGHT)), RED)

    if percent_funded >= 1:
        level = HEIGHT / 100 * percent_funded
        draw.rectangle(((0,level), (WIDTH,0)), GREEN)

    minimum_limit = HEIGHT / funding_target * funding_minimum
    draw.line(((0,minimum_limit), (WIDTH,minimum_limit)), "black", width=2)

    img = img.rotate(180)
    with open(filename, "wb") as fh:
        img.save(fh, "PNG")


TEXT_BELOW_MINIMUM = '''\
Minimum funding for this year has :funding-red:`not` been reached yet.
'''


def gen_status(filename, amount):
    if amount < funding_minimum:
        text = TEXT_BELOW_MINIMUM
    elif amount < funding_target * 0.9:
        text = TEXT_BELOW_TARGET
    else:
        text = TEXT_FUNDED
    with open(filename, "w") as fh:
        print(text, file=fh)


def gen_income_table(filename, amount, income):
    LF = "{0:<10s} {2: 8.2f} {1: 8.2f} {4: 8.2f} {3: 8.2f}"
    fh = open(filename, "w")

    print("Total amount this year:", amount, "€.", file=fh)

    print("""
========== ======== ======== ======== ========
.              Onetime           Recurring
---------- ----------------- -----------------
Month       sum        avg.     sum     avg.
========== ======== ======== ======== ========""", file=fh)

    for line in income:
        onetime = line[2]
        recurring = line[4]
        print(LF.format(line[0],
                        onetime, onetime / int(line[1]),
                        recurring, recurring / int(line[3])), file=fh)

    print("========== ======== ======== ======== ========", file=fh)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", default="_funding_status.txt")
    parser.add_argument("--table-filename", default="_funding_table.txt")
    parser.add_argument("--image-filename", default="_static/funding-chart.png")
    #parser.add_argument("amount", type=float)
    #parser.add_argument("next_year", metavar="amount-next-year", type=float)
    args = parser.parse_args()

    amount, income = read_income("_funding_2020.cfg")

    percent_funded = (amount or 0.00001) / funding_target * 100
    print("Funded:", int(amount), "=", percent_funded, "percent")
    gen_image(args.image_filename, percent_funded)

    ## next_year_image_filename = "-next".join(
    ##     os.path.splitext(args.image_filename))
    ## percent_funded = funding_target / (args.next_year or 0.00001)
    ## gen_image(next_year_image_filename, percent_funded)

    gen_income_table(args.table_filename, amount, income)
    gen_status(args.filename, amount)


if __name__ == "__main__":
    main()
