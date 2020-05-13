# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:47:20 2019

@author: HadesSecurity
"""

"""
Viết chương trình thực hiện các yêu cầu sau:
- Nhập: từ tập tin văn bản Cau7C.inp xâu ký tự S có không quá 200 ký tự.
- Xử lý:
    + Loại bỏ các ký tự không phải ký tự chữ và khoảng trắng khỏi S.
    + Sau đó, chuyển thành xâu ký tự X là dạng tOGGLE cASE của S.
- Xuất: ra tập tin văn bản Cau7C.out xâu ký tự X.
    Ví dụ: Nếu S = ‘ Khoa1 Cong nghe thong@ tin’ thì X = ‘ kHOA cONG
    nGHE tHONG tIN’.
------------------------------------------------------------------------
"""

import os

#GET FILE
file_size = os.path.getsize("Cau7C.INP")
#Mở đọc file
file_7_read = open("Cau7C.INP","r")
data_file_7 = file_7_read.read() 
#Mở viết file
file_7_write= open("Cau7C.OUT","w")

#hàm xử lý chương trình
def xuly():
    #GET SIZE FILE
    output = ""
    for i in range(file_size):
        #kiểm tra xem ký tự đã truyền có phải là chữ cái không hoặc khoảng cách ko?.
        if data_file_7[i].isalpha() or data_file_7[i] == " ":
            output = output+data_file_7[i]
            x=output
            x=" ".join(x.split()) # xóa hai dau cach trùng nhau hoặc cuôi câu
            b=x.title()     # hàm in hoa chữ cái đầu tiên
            c=b.swapcase() # đảo ngược kiểu HOA thành kiểu thường và ngược lại.
    file_7_write.write(c)

# Hàm tương đương với hàm main trong C/C++
def main():
   print ("Cau7_Nhom C") 
   
   #CHECK EXIST FILE
   check_file = os.path.exists("Cau7C.INP")
   if check_file == False:
       print ("Ban can tao file input")
   
   print ("file_size_7: ",file_size)
   print ("Data_file_7: ",data_file_7)
   
   xuly()
   file_7_read.close() #đóng file input 
   file_7_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()