mPay = 3000000
sRate = 20/100
yRate = 2.5/100

sMoney = mPay * sRate
mRate = 1 + yRate/12

tSave = 0

for a in range(12):
    tSave = (tSave + sMoney) * mRate
    print(a, tSave)