import sys


def transform(text):
    if text == "t":
        text = 'true'
    elif text == 'f':
        text = 'false'

    return text.strip('"')


columns = []
if len(sys.argv) != 2:
    print('Usage: CsvToXml.py <file.csv>')
else:
    with open(sys.argv[1]) as fd:
        header = True
        for line in fd:
            if header:
                for field in line.strip().split(","):
                    columns.append(field.strip('"'))
                header = False
            else:
                idx = 0
                output = []
                for field in line.strip().split(","):
                    if field != '""' and len(field) > 0:
                        output.append('{}="{} "'.format(columns[idx], transform(field)))
                    idx += 1
                print("".join(output))
