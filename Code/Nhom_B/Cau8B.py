# -*- coding: utf-8 -*-
"""
Viết chương trình thực hiện các yêu cầu sau:
    - Nhập: từ tập tin văn bản Cau8B.inp số nguyên dương N, N < 10^3 , 
            và dãy số nguyên K gồm N phần tử có giá trị nằm trong đoạn [-10^9,10^9] .
    - Xử lý: đếm số phần tử âm C. Nếu C > 0 thì tính trung bình cộng AVE của
            các phần tử âm trong dãy số K, AVE làm tròn tới 2 số sau dấu chấm thập phân.
    - Xuất: ra tập tin văn bản Cau8B.out giá trị của C và AVE nếu C > 0, mỗi giá
            trị trên một dòng.
            Ví dụ: Nếu N = 6 và dãy K = (-50, 40, 60, -10, 20, -30) thì C = 3 và AVE = -30.00

"""

file_8_read = open("Cau8B.INP","r")
file_8_write= open("Cau8B.OUT","w")

indata = file_8_read.read(1)
matrix=file_8_read.read().split()

#Hàm nhập 
def nhap():   
   m=int(indata)
   return m

#hàm xử lý chương trình    
def xuly(m):
    dem = 0
    tong = 0
    for i in range (0,m):
        if(int(matrix[i])<0):
            dem=dem +1
            tong= tong + int(matrix[i])   
    tbc=tong/dem 
    file_8_write.write("C= "+ str(dem)+ "\nAVE= "+ str(tbc))

# Hàm tương đương với hàm main trong C/C++
def main(): 
   m=nhap()    
   xuly(m)
   file_8_read.close() #đóng file input 
   file_8_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()