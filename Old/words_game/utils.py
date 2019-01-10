
import csv
from collections import OrderedDict
import os


def csv2odict(path):
    """
    从words_numbers_100.csv读取字典
    :return: 一个OrderedDict
    """
    print("Loading file : " + path)
    if not os.path.isfile(path):
        print("File Not Exists!")

    file = open(path, mode='r', encoding='utf-8')
    csvReader = csv.reader(file)

    # get rid of header row
    header = next(csvReader)
    # print(header)

    odict = OrderedDict()
    for row in csvReader:
        odict[row[0]] = row[1]
        # print(row)

    return(odict)


