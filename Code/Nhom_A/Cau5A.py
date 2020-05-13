# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 09:11:53 2019

@author: DELL
"""

"""
Viết chương trình thực hiện các yêu cầu sau:
    - Nhập: Từ tập tin văn bản Cau5A.inp 2 số nguyên dương M,N , M,N <= 10^9.
    - Xử lý: tìm ước số chung lướn nhất U và Bội số chung nhỏ nhất B của 2 số M,N.
    - Xuất: ra tập tin văn bản Cau5A.out giá trị của U và B.
    VD: Nếu M= 24, và N= 36 thì U=12 và B= 72.
"""

in_file = open('Cau5A.INP','r') #với 'r' mở để đọc nội dung
out_file = open('Cau5A.OUT','w') # mở để đọc nội dung với 'w'

# hàm nhập m,n
def nhap():
    m,n = [int(i) for i in next(in_file).split()]
    return m,n

 # Hàm tính USCLN bằng thuật toán Euclid
def uscln(m, n):
     while n != 0:
         r = m % n
         m = n
         n = r
     return m
 
# Hàm BSCNN "gián tiếp" dựa vào USCLN
def bscnn(m,n):
    return (m * n) // uscln(m,n)

# Hàm tương đương với hàm main trong C/C++
def main():
    #Nhập và kiểm tr dữ liệu nhập
    while True:
        m,n = nhap()
        if m ** 2 + n ** 2 > 0:
            break
# Tìm BSCNN USCLN
    out_file.write("U = %d" %(uscln(m, n)))
    out_file.write("\tB = %d" %(bscnn(m, n)))    
    in_file.close() #đóng file input 
    out_file.close() #đóng file đóng file output
    print ("done")

    
# gọi thực hiên hàm main
if __name__=="__main__":
    main()    
    
  
     