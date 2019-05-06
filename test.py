import connectdb as conn

def getInfo():
    return

def setHamPhuThuoc(testSet, classID):
    # if(classID != 'class0' or classID != 'class1'):
    #     return
    phuthuoc = []
    A = conn.getTapTienDe(classID)
    for i in range(len(testSet)):
        phuthuoc.append(abs(testSet[i] - A[i]))
    return phuthuoc

# def setPhanLop(HamPhuThuoc):
#     confidence0 = conn.getConfidence('class0')
#     confidence1 = conn.getConfidence('class1')
#     phuthuoc = 1
#     for i in range(len(HamPhuThuoc)):
#         phuthuoc *= HamPhuThuoc[i]
#     phanLop0 = confidence0 * phuthuoc
#     phanLop1 = confidence1 * phuthuoc
#     if phanLop0 > phanLop1:
#         return 0
#     else: 
#         return 1
def phanlop(hamphuthuoc0, hamphuthuoc1):
    confidence0 = conn.getConfidence('class0')
    confidence1 = conn.getConfidence('class1')
    phuthuoc0 = 1
    phuthuoc1 = 1
    for i in range(0, 7):
        phuthuoc0 *= hamphuthuoc0[i]
        phuthuoc1 *= hamphuthuoc1[i]
    phanLop0 = confidence0 * phuthuoc0
    phanLop1 = confidence1 * phuthuoc1
    if phanLop0 > phanLop1:
        return 0
    else: 
        return 1
def readTest():
    print("FFMC: ", end = '')
    FFMC = float(input())
    print("DMC: ", end = '')
    DMC = float(input())
    print("DC: ", end = '')
    DC = float(input())
    print("ISI: ", end = '')
    ISI = float(input())
    print("temp: ", end = '')
    temp = float(input())
    print("RH: ", end = '')
    RH = float(input())
    print("wind: ", end = '')
    wind = float(input())
    test = [FFMC, DMC, DC, ISI, temp, RH, wind]
    return test
# test = readTest()
def result(test):
    phuthuoc0 = setHamPhuThuoc(test, 'class0')
    phuthuoc1 = setHamPhuThuoc(test, 'class1')
    print(phanlop(phuthuoc0, phuthuoc1))
    return phanlop(phuthuoc0, phuthuoc1)
# phuthuoc0 = setHamPhuThuoc(test, 'class0')
# # print(phuthuoc0)
# phuthuoc1 = setHamPhuThuoc(test, 'class1')
# print(phanlop(phuthuoc0, phuthuoc1))