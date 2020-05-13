# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 19:44:48 2019

@author: Admin
"""
"""
Viết chương trình thực hiện các yêu cầu sau:
    - Nhập: từ tập tin văn bản Cau2B.inp số nguyên dương N, N < 10^3 , 
            và dãy số nguyên K gồm N phần tử có giá trị nằm trong đoạn [-10^9,10^9] .
    - Xử lý: tìm giá trị lớn nhất MAX và vị trí đầu tiên POS của MAX trong dãy số K.
    - Xuất: ra tập tin văn bản Cau2B.out giá trị của MAX và POS, mỗi giá trị trên 1 dòng.
            Ví dụ: Nếu N = 8 và dãy K = (50, 40, 60, 10, 20, 60, 30, 10) thì MAX = 60
                   và POS = 3
"""

file_2_read = open("Cau2B.INP","r")
file_2_write= open("Cau2B.OUT","w")

indata = file_2_read.read(1) 
mat=file_2_read.read().split()

#Hàm nhập 
def nhap():   
   n=int(indata)
   return n

#hàm xử lý chương trình    
def xuly(n):
    max=0
    vt=0
    for i in range (0,n):
        if(int(mat[i]) > int(max)):
            max = mat[i]
    for i in range (0,n):
        if(int(mat[i]) == int(max)):
            vt =i+1
            break 
    file_2_write.write("MAX= "+ max + "\tvà POS= "+ str(vt))

# Hàm tương đương với hàm main trong C/C++
def main(): 
   m=nhap()    
   xuly(m)
   file_2_read.close() #đóng file input 
   file_2_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()