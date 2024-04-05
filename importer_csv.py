import csv


def get_rows():
    with open("./data/klarna_customer_segments.csv", "r") as csvfile:
        spamreader = csv.reader(csvfile)
        list = []
        for row in spamreader:
            list.append(row)
        return list
