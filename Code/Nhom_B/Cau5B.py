# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:41:31 2019

@author: HadesSecurity
"""
"""
        - Nhập: từ tập tin văn bản Cau5B.inp số nguyên dương N, N < 10^2 , 
            và ma trận vuông A kích thước N hàng, 
            N cột chứa các giá trị nguyên nằm trong đoạn [10^4 ,10^4 ] .
    	- Xử lý: tìm ma trận B là ma trận tích của A nhân với A.
    	- Xuất: ra tập tin văn bản Cau5B.out ma trận B.
            Ví dụ: Nếu N = 3 và ma trận A = [(1, 0, 1), (0, 1, 2), (3, 2, 0)] 
            thì ma trận B= [(4, 2, 1), (6, 5, 2), (3, 2, 7)].

"""
import numpy as np

file_5_read = open("Cau5B.INP")
file_5_write= open("Cau5B.OUT","w")
_n=file_5_read.read(1)
matrix=file_5_read.read()
matrix = [item.split() for item in matrix.split('\n')[:-1]] 

# Hàm tương đương với hàm main trong C/C++
def main():
    A=np.array(matrix)# khoiwrtao ma tran với numpy
    
    file_5_write.write(str(np.multiply(A,A)))
    file_5_read.close() #đóng file input 
    file_5_write.close() #đóng file đóng file output
    print ("done")
    
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()