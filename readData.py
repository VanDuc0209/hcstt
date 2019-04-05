import csv
import settings

def readDataTrain():
    data = [[]]
    with open(settings.DATA_TRAIN_PATH) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                data.append([])
                for num in range(0, 8):
                    data[line_count].append(row[num])
                line_count += 1
        print(f'Processed {line_count-1} lines.')
    del data[0]
    return data