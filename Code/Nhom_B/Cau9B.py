# -*- coding: utf-8 -*-
"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Viết chương trình thực hiện các yêu cầu sau:   
    - Nhập: từ tập tin văn bản Cau2.inp số nguyên dương N, N 10^3 , và dãy số
            nguyên K gồm N phần tử có giá trị nằm trong đoạn [10^9,109] . 
    - Xử lý: Sắp xếp dãy K theo thứ tự tăng dần.    
    - Xuất: ra tập tin văn bản Cau2.out dãy số K sau khi đã sắp xếp, mỗi phần tử
            cách nhau đúng 1 khoảng trắng.
            Ví dụ: Nếu N = 8 và dãy K = (50, 40, 60, 10, 20, 60, 30, 10) thì dãy K sau
                    khi sắp xếp tăng dần là K = (10, 10, 20, 30, 40, 50, 60, 60).
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

file_9_read = open("Cau9B.INP","r")
file_9_write= open("Cau9B.OUT","w")

indata = file_9_read.read(1)
matrix=file_9_read.read().split()

#Hàm nhập 
def nhap():   
   m=int(indata)
   return m

#hàm xử lý chương trình    
def xuly(m):
    x=0
    for i in range (0,m):
        for j in range (i,m):
            if(matrix[i]> matrix[j]):
                x=matrix[i]
                matrix[i]=matrix[j]
                matrix[j]=x    
    file_9_write.write("K= "+ str(matrix))    

# Hàm tương đương với hàm main trong C/C++
def main(): 
   m=nhap()    
   xuly(m)
   file_9_read.close() #đóng file input 
   file_9_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()