# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:13:28 2019

@author: DELL
"""

"""
------------------------------------------------------------------------
Viết chương trình thực hiện các yêu cầu sau:
    - Nhập: từ tập tin văn bản Cau2A.inp số nguyên dương N, N < <= 10^6.
    - Xử lý: tìm tất cả các ước số nguyên tố của N.
    - Xuất ra tập tin văn bản Cau2A.out các ước số nguyên tố của N trên cùng cột dòng, 
    các số cách nhau đúng một khoảng trắng.
    VD:  nếu N=360 thì N có các ước số nguyên tố là 2, 3, 5
------------------------------------------------------------------------
"""
import math

in_file = open('Cau2A.INP','r') #với 'r' mở để đọc nội dung
out_file = open('Cau2A.OUT','w') # mở để đọc nội dung với 'w'

#hàm Nhập
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

#Hàm xử lý bài toán
def xuly(n):
     for i in range(2, n+1):
          if n%i==0:
              if ktnt(i) == True :
                  out_file.write('%d, '%i) #ghi nội dung vào file
#                  print("%d"%(i))
                  
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


              