import numpy as np 
def handle(req):


    try:
        m = int(req)
        mat1 = np.random.rand(m, m)
        mat2 = np.random.rand(m, m)
        matrix_result = np.multiply(mat1, mat2)

        return "result: " + str(matrix_result.shape)
    except:
        return "the input is not a number"
