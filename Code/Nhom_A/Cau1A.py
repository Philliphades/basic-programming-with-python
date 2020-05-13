# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:31:19 2019

@author: DELL
"""

"""
------------------------------------------------------------------------
Câu 1:
    Viết chương trình thực hiện các yêu càu sau:
        - Nhập: từ tập tin văn bản Cau1A.inp số nguyên dương N, N <= 10^6.
        - Xử lý: tìm tất cả các số nguyên tố không lớn hơn N.
        - Xuất: ra tập tin văn bản Cau1A.out số lượng C của số nguyên tố.
    VD: Nếu N = 11 thì C = 5 số nguyên tố không lớn hơn 11 là 2, 3, 5, 7, 11.
------------------------------------------------------------------------
"""
import math

in_file = open('Cau1A.INP','r') #với 'r' mở để đọc nội dung
out_file = open('Cau1A.OUT','w') # mở để đọc nội dung với 'w'

#hàm nhập    
def nhap():
    indata = in_file.read() #đọc dữ liệu từ file
    n = int(indata)
    return n

# Hàm kiểm tra 1 số nguyên dương x có phải là số nguyên tố?
def ktnt(n):
    k = int(math.sqrt(n)) + 1
    for i in range(2, k):
        if n % i == 0:
            return False
    return True

# hàm xử lý bài toán
def xuly(n):
   for i in range(2,n+1):
       if ktnt(i) == True:          
          out_file.write('%d\n'%i) #ghi nội dung vào file              
         
# Hàm tương đương với hàm main trong C/C++
def main():
    n=nhap()
    xuly(n)
    in_file.close() #đóng file input 
    out_file.close() #đóng file đóng file output
    print ("done")
    
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()


        