import numpy
import math


def DCT_coefficients (matrix,position):
    
    shape=matrix.shape
    height=shape[0]
    width=shape[1]
    DCT_matrix =numpy.ones((height,width))
    for i in range(height):
        for j in range(width):
            #ci and cj depends on frequency as well as number of row and columns of specified matrix 
            if i==0 :
                ci=1/math.sqrt(height)

            else :
                ci = math.sqrt(2) / math.sqrt(height)

            if j==0 :
              cj = 1 / math.sqrt(width)

            else :
                cj = math.sqrt(2) / math.sqrt(width)

            sum=0 
            for k in range (height) :
                for l in range (width):
                 dct1= matrix[k][l][int(position)]*math.cos((2 * k + 1) * i * math.pi / (2 * width))*math.cos((2 * l + 1) * j * math.pi / (2 * width))
                
                 sum = sum + dct1

            DCT_matrix[i][j] = ci * cj * sum 
            

    return DCT_matrix                  



def IDCT_coefficients (matrix):
    shape =matrix.shape
    height=shape[0]
    width=shape[1]
    IDCT_matrix=numpy.ones((8,8))
    for x in range (height):
        for y in range(width):
            sum=0
            for i in range(height):
                for j in range(width):
                    if i==0 :
                      ci=1/math.sqrt(height)

                    else :
                      ci = math.sqrt(2) / math.sqrt(height)

                    if j==0 :
                      cj = 1 / math.sqrt(width)

                    else :
                      cj = math.sqrt(2) / math.sqrt(width)

                    idct1= matrix[i][j]*math.cos((2 * x + 1) * i * math.pi / (2 * height))*math.cos((2 * y + 1) * j * math.pi / (2 * width))
                    sum=sum+idct1*cj*ci

            IDCT_matrix[x][y]=  sum

    return IDCT_matrix           



