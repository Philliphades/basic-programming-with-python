# -*- coding: utf-8 -*-
"""
Viết chương trình thực hiện các yêu cầu sau:
    - Nhập: từ tập tin văn bản Cau4B.inp số nguyên dương N, N < 10^3 , và dãy số
            nguyên K gồm N phần tử có giá trị nằm trong đoạn  [-10^9,10^9] .
    - Xử lý: đếm số phần tử dương C và tính trung bình cộng AVE của dãy số K,
            AVE làm tròn tới 2 số sau dấu chấm thập phân.
    - Xuất: ra tập tin văn bản Cau4B.out giá trị của C và AVE, mỗi giá trị trên một dòng
            Ví dụ: Nếu N = 6 và dãy K = (-50, -40, -60, -10, -20, -30) 
                    thì C = 0 và AVE= -35.00.
"""

file_4_read = open("Cau4B.INP","r")
file_4_write= open("Cau4B.OUT","w")
indata = file_4_read.read(1)
matrix=file_4_read.read().split()

#Hàm nhập 
def nhap():   
   m=int(indata)
   return m

#hàm xử lý chương trình    
def xuly(m):
    dem = 0
    for i in range (0,m):
        if(int(matrix[i])>0):
            dem=dem +1
    
    tong=0
    for i in range (0,m):
        tong=tong+int(matrix[i])
    TB=tong/m
    file_4_write.write("C= "+ str(dem) + "\nAVE= "+str(TB)) 

# Hàm tương đương với hàm main trong C/C++
def main(): 
   m=nhap()    
   xuly(m)
   file_4_read.close() #đóng file input 
   file_4_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()


