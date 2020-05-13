# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 19:21:50 2019

@author: DELL
"""
"""
Viết chương trình thực hiện các yêu càu sau:
    - Nhập: từ tập tin văn bản Cau8.inp sood nguyên dương N, N <10^6.
    - Xử lý: Tìm tất cả các số hoàn hảo không lớn hơn N.
             Biết X là một số hoàn hảo nếu X bằng tổng các ước số của nó, không kể X.
    - Xuất: ra tập tin văn bản Cau8.outdanh sách các số hoàn hảo nếu có và giá trị C là số lượng số hoàn hảo tìm được.
"""

in_file = open('Cau8A.INP','r') #với 'r' mở để đọc nội dung
out_file = open('Cau8A.OUT','w') # mở để đọc nội dung với 'w'

#hàm Nhập
def nhap():
    indata = in_file.read() #đọc dữ liệu từ file
    n = int(indata)
    return n

# Hàm kiểm tra 1 số nguyên dương x có phải là số hoàn hảo?
def isPerfectNumber(n):
    if n <= 1:
        return False;
    else:
        sumDivision = 0
        for i in range(1, n):        
            if n % i == 0:
                sumDivision += i    #sumDivision = sumDivision + i     
        return True if sumDivision == n else False
        #return sumDivision == number ? True : False; 
                
# hàm xử lý bài toán
def xuly(n):
   for i in range(1,n):
       if isPerfectNumber(i) == 1 :
           out_file.write('%d\n'%i)
    
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
