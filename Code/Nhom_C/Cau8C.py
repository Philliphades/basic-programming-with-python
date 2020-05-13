# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:08:39 2019

@author: HadesSecurity
"""

"""
- Nhập: từ tập tin văn bản Cau8C.inp xâu ký tự S có không quá 50 ký tự là họ tên
        Việt Nam của 1 người, trong đó có một số ký tự gõ nhầm 
        (không phải ký tự chữ và gõ thừa khoảng trắng).
- Xử lý:
        + Loại bỏ các ký tự không phải ký tự chữ và khoảng trắng khỏi S.
        + Sau đó, tìm xâu ký tự X là họ của người đó.
- Xuất: ra tập tin văn bản Cau8C.out xâu ký tự X.
        Ví dụ: Nếu S = ‘ Nguyen1 Van234 A5n67h ’ thì X = ‘Nguyen’.
"""

import os

#GET FILE
file_size = os.path.getsize("Cau8C.INP")
#Mở đọc file
file_8_read = open("Cau8C.INP","r")
data_file_8 = file_8_read.read() 
#Mở viết file
file_8_write= open("Cau8C.OUT","w")

#hàm xử lý chương trình
def xuly():
    #GET SIZE FILE
    output = ""
    for i in range(file_size):
        #kiểm tra xem ký tự đã truyền có phải là chữ cái không hoặc khoảng cách ko?.
        if data_file_8[i].isalpha() or data_file_8[i] == " ":
            output = output+data_file_8[i]
            x=output
            x=" ".join(x.split()) # xóa hai dau cach trùng nhau hoặc cuôi câu
            p=x.split()  # chia chuỗi str thành một dãy các token được phân biệt riêng rẽ bởi dấu tách d
    file_8_write.write(p[0])

# Hàm tương đương với hàm main trong C/C++
def main():
   print ("Cau8_Nhom C") 
   
   #CHECK EXIST FILE
   check_file = os.path.exists("Cau8C.INP")
   if check_file == False:
       print ("Ban can tao file input")
   
   print ("file_size_8: ",file_size)
   print ("Data_file_8: ",data_file_8)
   
   xuly()
   file_8_read.close() #đóng file input 
   file_8_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()