rows = int(input("ENTER ROW NUMBERS:"))
cols = int(input("ENTER COLUMN NUMBERS:"))
numOfMatrix = int(input("ENTER NUMBER OF MATRIX:"))

matrices = {}
#b = []
NOM = 0
while(NOM < numOfMatrix):
    matrix = []
    n = 0
    while (n < rows):
        x = 0
        row = []
        while (x < cols):
            i = int(
                input('ENTER NUMBER OF ROW ' + str(n + 1) + ' COLUMN ' +
                      str(x + 1) + ':'))
            row.append(i)
            x = x + 1
        matrix.append(row)
        n = n + 1
    # print(matrix)
    matrices['Matrix '+str(NOM+1)] = matrix
    NOM = NOM + 1
#print(l)



k = 0
while (k < len(matrices)):
    print("Matrix " + str(k+1))
    m = (matrices['Matrix '+ str(k+1)])
    p = 0
    while (p < len(m)):
        print(m[p])
        p = p + 1
    k = k + 1

#MADE BY ASAD AND FOUZ AND FAIQ AND ASDULLAH AND AMAN AND QAMBER ALI4