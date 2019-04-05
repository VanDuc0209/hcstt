import mysql.connector
from readData import readDataTrain

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'duc0209',
    database = 'forest'
)
mycursor = mydb.cursor()


def setDataTrain():
    data = readDataTrain()
    for row in data:
        sql = "insert into train_set (FFMC, DMC, DC, ISI, temp, RH, wind, area) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = row
        # val.insert(0, NULL)
        mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def getTapTienDe(classID):
    A = []
    if classID == 'class0':
        sql = "select AVG(FFMC) as ffmc, avg(dmc) as dmc, avg(DC) as dc, avg(ISI) as isi, avg(temp) as temp, avg(RH) as rh, avg(wind) as wind from train_set where area = 0"
    elif classID == 'class1':
        sql = "select AVG(FFMC) as ffmc, avg(dmc) as dmc, avg(DC) as dc, avg(ISI) as isi, avg(temp) as temp, avg(RH) as rh, avg(wind) as wind from train_set where area <> 0"
    else:
        print('No Class')
        return
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for x in result:
        for i in range(0, 7):
            A.append(x[i])
    return A

def getTrainSet(classID):
    trainset = [[]]
    if classID == 'class0':
        sql = "select FFMC, DMC, DC, ISI, temp, RH, wind from train_set where area = 0"
    elif classID == 'class1':
        sql = "select FFMC, DMC, DC, ISI, temp, RH, wind from train_set where area <> 0"
    elif classID == 'all':
        sql = "select FFMC, DMC, DC, ISI, temp, RH, wind from train_set"
    else:
        print('No class')
        return
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    count = 0
    for tmp in myresult:
        trainset.append([])
        for i in range(0, 7):
            trainset[count].append(tmp[i])
        count += 1
    del trainset[count]
    return trainset
def setConfidence(classID, value):
    sql = "insert into confidence (id, value) values(%s, %s)"
    val = ""
    if classID == 'class0':
        val = ('class0', value)
    elif classID == 'class1':
        val = ('class1', value)
    else: 
        print("No class")
        return
    mycursor.execute(sql, val)
    mydb.commit()

def getConfidence(classID):
    sql = "select value from confidence where id = \'" + classID + "\'"
    # print(sql)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    confidence = 0
    for i in result:
        confidence = i[0]
    return confidence