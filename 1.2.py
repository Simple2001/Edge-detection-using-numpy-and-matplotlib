import numpy as np

def vert_edge(w,h,big_matrix):
    try:
        size_of_square_matrix = 3 
        vef = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
        
        no_of_square_matrices = ((w-size_of_square_matrix)+1)*((h-size_of_square_matrix)+1)
        sosm=size_of_square_matrix
        row=(h-size_of_square_matrix)+1                     
        column=(w-size_of_square_matrix)+1                  
        max_val=0
        result = []
        r = (h-3)+1                                         
        c = (w-3)+1                                         

        for i in range(row):
            for j in range(column):
                sq = big_matrix[i:i+sosm,j:j+sosm]
                sum = 0
                for k in range(3):
                    for l in range(3):
                        sum += (sq[k,l] * vef[k,l])
                result.append(sum)
        result_matrix = np.asarray(result).reshape(r,c)     
        return result_matrix

    except Exception as e:
        print("Invalid Input, Try again",str(e))
#importing the numpy library
import numpy as np

def hor_edge(w,h,big_matrix):
    try:
        size_of_square_matrix = 3 
        vef = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        
        no_of_square_matrices = ((w-size_of_square_matrix)+1)*((h-size_of_square_matrix)+1)
        sosm=size_of_square_matrix
        row=(h-size_of_square_matrix)+1                     
        column=(w-size_of_square_matrix)+1                  
        result = []
        r = (h-3)+1                                         
        c = (w-3)+1                                         
        for i in range(row):
            for j in range(column):
                sq = big_matrix[i:i+sosm,j:j+sosm]
                sum = 0
                for k in range(3):
                    for l in range(3):
                        sum += (sq[k,l] * vef[k,l])
                result.append(sum)
        result_matrix = np.asarray(result).reshape(r,c)     
        return result_matrix

    except Exception as e:
        print("Invalid Input, Try again",str(e))        
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = mpimg.imread('pp.png') #put name of the image here    
black_n_white = img.mean(axis=2)   
h,w = black_n_white.shape          

vertical = vert_edge(w,h,black_n_white)  
horizontal = hor_edge(w,h,black_n_white) 
image = np.sqrt((vertical**2) + (horizontal**2)) 
plt.imshow(image, cmap='gray', interpolation='nearest') 
plt.show() 