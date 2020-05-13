# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 09:35:22 2019

@author: HadesSecurity
"""

"""
Viết chương trình thực hiện các yêu cầu sau:
- Nhập: từ tập tin văn bản Cau4C.inp xâu ký tự S có không quá 200 ký tự.
- Xử lý:
    + Loại bỏ các ký tự không phải ký tự chữ và khoảng trắng khỏi S.
    + Sau đó, chuyển thành xâu ký tự X là dạng xâu chuẩn của S. Biết: xâu
        chuẩn là 1 xâu ký tự mà không có 2 khoảng trắng liên tiếp, 
        bắt đầu và kết thúc không phải là khoảng trắng.
- Xuất: ra tập tin văn bản Cau4C.out xâu ký tự X.
        Ví dụ: Nếu S = ‘ Co@ng1 nghe2 34 th$ong tin5 ’ thì X = ‘Cong nghe thong tin’

"""

import os

#GET FILE
file_size = os.path.getsize("Cau4C.INP")
#Mở đọc file
file_4_read = open("Cau4C.INP","r")
data_file_4 = file_4_read.read() 
#Mở viết file
file_4_write= open("Cau4C.OUT","w")

#hàm xử lý chương trình
def xuly():
    #GET SIZE FILE
    output = ""
    for i in range(file_size):
        #kiểm tra xem ký tự đã truyền có phải là chữ cái không hoặc khoảng cách ko?.
        if data_file_4[i].isalpha() or data_file_4[i] == " ":
            output = output+data_file_4[i]
            x=output
            # xóa hai dau cach trùng nhau hoặc cuôi câu
            x=" ".join(x.split())     
    file_4_write.write(x)

# Hàm tương đương với hàm main trong C/C++
def main():
   print ("Cau4_Nhom C") 
   
   #CHECK EXIST FILE
   check_file = os.path.exists("Cau4C.INP")
   if check_file == False:
       print ("Ban can tao file input")
   
   print ("file_size_4: ",file_size)
   print ("Data_file_4: ",data_file_4)
   
   xuly()
   file_4_read.close() #đóng file input 
   file_4_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()