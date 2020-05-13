# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:55:41 2019

@author: Admin
"""
"""
- Nhập: từ tập tin văn bản Cau7B.inp 2 số nguyên dương M, N, M , N 10^2 , 
        và ma trận A kích thước M hàng, 
        N cột chứa các giá trị nguyên nằm trong đoạn 10^4 ,10^4 ] .
- Xử lý: tìm ma trận B là ma trận chuyển vị của A.
- Xuất: ra tập tin văn bản Cau7B.out ma trận B.
        Ví dụ: Nếu M = 2, N = 3 và ma trận A = [(50, 40, 60), (10, 20, 30)] 
        thì ma trận B = [(50, 10), (40, 20), (60, 30)]

"""
import numpy as np

file_7_read = open("Cau7B.INP")
file_7_write= open("Cau7B.OUT","w")
_m=file_7_read.read(1)
_n=file_7_read.read(2)
matrix=file_7_read.read()
matrix = [item.split() for item in matrix.split('\n')[:-1]]

# Hàm tương đương với hàm main trong C/C++
def main():
    A=np.array(matrix)
    file_7_write.write(str(A.T))#hàm chuyển vị của thư viện numpy
    file_7_read.close() #đóng file input 
    file_7_write.close() #đóng file đóng file output
    print ("done")
    
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()





