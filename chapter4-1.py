intA = 3
floatB = 345678.14
stringC = "abcdefg"

print(intA, floatB, stringC)
print(intA, floatB, stringC, sep=" --> ")
print("Interger %d, Float %f, String %s" % (intA, floatB, stringC)) #Tuple 변화
print("Interger %5d, Float %7.2f, String %20s" % (intA, floatB, stringC))
print("{} + {} - {}".format(intA, floatB, stringC))
print("{2} + {0} - {1}".format(intA, floatB, stringC))
print("{2:20s} + {0:8d} - {1 : ^15f}" .format(intA, floatB, stringC))
print("{2:20s} + {0:8d} - {1 : ^15, 3f}" .format(intA, floatB, stringC))