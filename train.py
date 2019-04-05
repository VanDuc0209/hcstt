import connectdb as conn

def setHamphuthuoc(taptiende, train_set):
    phuthuoc = [[]]
    count = 0
    # print(type(A[0]))
    for tmp in train_set:
        phuthuoc.append([])
        for i in range(len(taptiende)):
            phuthuoc[count].append(abs(tmp[i] - taptiende[i]))
        count += 1
    del phuthuoc[count]
    return phuthuoc

    
def setConfidence(phuthuoc_class, phuthuoc_full):
    sum0 = 0.0
    sum1 = 0.0
    for row in phuthuoc_class:
        tich = 1
        for i in range(0, len(row)):
            tich *= row[i]
        sum0 += tich
    for row in phuthuoc_full:
        tich = 1
        for i in range(0, len(row)):
            tich *= row[i]
        sum1 += tich
    return (sum0/sum1)

A0 = conn.getTapTienDe('class0')
A1 = conn.getTapTienDe('class1')

train0 = conn.getTrainSet('class0')
train1 = conn.getTrainSet('class1')
train_full = conn.getTrainSet('all')

phuthuoc0 = setHamphuthuoc(A0, train0)
phuthuoc0_full = setHamphuthuoc(A0, train_full)

phuthuoc1 = setHamphuthuoc(A1, train1)
phuthuoc1_full = setHamphuthuoc(A1, train_full)

confidence0 = setConfidence(phuthuoc0, phuthuoc0_full)
confidence1 = setConfidence(phuthuoc1, phuthuoc1_full)
print(confidence0)
print(confidence1)

conn.setConfidence('class0', confidence0)
conn.setConfidence('class1', confidence1)