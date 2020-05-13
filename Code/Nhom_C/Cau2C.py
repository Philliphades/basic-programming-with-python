# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:00:10 2019

@author: HadesSecurity
"""

"""
Viết chương trình thực hiện các yêu cầu sau:
- Nhập: từ tập tin văn bản Cau2C.inp xâu ký tự S có không quá 200 ký tự.
- Xử lý:
    + Loại bỏ các ký tự không phải ký tự chữ và khoảng trắng khỏi S.
    + Sau đó, chuyển thành xâu ký tự X là dạng Title Case của S.
- Xuất: ra tập tin văn bản Cau2C.out xâu ký tự X.
        Ví dụ: Nếu S = ‘ Khoa1 Cong nghe thong@ tin’ thì X = ‘ Khoa Cong Nghe Thong Tin’.
------------------------------------------------------------------------------------------
"""

import os

#GET FILE
file_size = os.path.getsize("Cau2C.INP")
#Mở đọc file
file_2_read = open("Cau2C.INP","r")
data_file_2 = file_2_read.read() 
#Mở viết file
file_2_write= open("Cau2C.OUT","w")

#hàm xử lý chương trình
def xuly():
    #GET SIZE FILE
    output = ""
    for i in range(file_size):
        #kiểm tra xem ký tự đã truyền có phải là chữ cái không hoặc khoảng cách ko?.
        if data_file_2[i].isalpha() or data_file_2[i] == " ":
            output = output+data_file_2[i]
            x=output
            x=" ".join(x.split()) # xóa hai dau cach trùng nhau hoặc cuôi câu
            b=x.title()     # hàm in hoa chữ cái đầu tiên
    file_2_write.write(b)

# Hàm tương đương với hàm main trong C/C++
def main():
   print ("Cau2_Nhom C") 
   
   #CHECK EXIST FILE
   check_file = os.path.exists("Cau2C.INP")
   if check_file == False:
       print ("Ban can tao file input")
   
   print ("file_size_2: ",file_size)
   print ("Data_file_2: ",data_file_2)
   
   xuly()
   file_2_read.close() #đóng file input 
   file_2_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()