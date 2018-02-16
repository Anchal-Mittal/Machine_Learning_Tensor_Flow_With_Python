# tensor algebra
def fun():
    from numpy import array
    A= array([
        [[1,2,3],[4,5,6],[7,8,9]],
        [[11,12,13],[24,15,16],[17,18,19]],
        [[20,21,22],[23,24,25],[26,27,28]],
        ])
    B= array([
        [[12,23,35],[74,85,96],[73,85,93]],
        [[11,72,83],[22,45,36],[17,18,19]],
        [[90,21,22],[13,22,25],[36,27,38]],
        ])
    print("shape of the matrix A\n",A.shape)
    print("The matrix A is\n",A)
    print("shape of the matrix B\n",B.shape)
    print("The matrix B is\n",B)
    C=A + B
    print("shape of the matrix C after addition \n",C.shape)
    print("The matrix C after addition is\n",C)
    C=A - B
    print("shape of the matrix C after subtraction \n",C.shape)
    print("The matrix C after subtraction is\n",C)
    C=A*B
    print("shape of the matrix C after multipication \n",C.shape)
    print("The matrix C after multipication is\n",C)
    C=A / B
    print("shape of the matrix C after division \n",C.shape)
    print("The matrix C after division is\n",C)

fun()    
