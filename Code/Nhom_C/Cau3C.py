# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 09:22:32 2019

@author: HadesSecurity
"""

"""
Viết chương trình thực hiện các yêu cầu sau:
- Nhập: từ tập tin văn bản Cau3C.inp xâu ký tự S có không quá 50 ký tự là họ tên
        Việt Nam của 1 người, trong đó có một số ký tự gõ nhầm 
        (không phải ký tự chữ và gõ thừa khoảng trắng).
- Xử lý:
    + Loại bỏ các ký tự không phải ký tự chữ và khoảng trắng khỏi S.
    + Sau đó, tìm xâu ký tự X là tên của người đó.
- Xuất: ra tập tin văn bản Cau3C.out xâu ký tự X.
    Ví dụ: Nếu S = ‘ Nguyen1 Van234 A5n67h ’ thì X = ‘Anh’
"""

import os

#GET FILE
file_size = os.path.getsize("Cau3C.INP")
#Mở đọc file
file_3_read = open("Cau3C.INP","r")
data_file_3 = file_3_read.read() 
#Mở viết file
file_3_write= open("Cau3C.OUT","w")

#hàm xử lý chương trình
def xuly():
    #GET SIZE FILE
    output = ""
    for i in range(file_size):
        #kiểm tra xem ký tự đã truyền có phải là chữ cái không hoặc khoảng cách ko?.
        if data_file_3[i].isalpha() or data_file_3[i] == " ":
            output = output+data_file_3[i]
            x=output
            x=" ".join(x.split()) # xóa hai dau cach trùng nhau hoặc cuối câu
    
    #tim tên
    for i in range(0,len(x)):
        if (x[i]==" "):
            a=(x[i:]) # lấy tất cả các ki tu trong chuổi từ vị trí i đên hết
            b=a.strip()    #xóa dau cach đầu và cuối câu
    file_3_write.write(b)
    
# Hàm tương đương với hàm main trong C/C++
def main():
   print ("Cau3_Nhom C") 
   
   #CHECK EXIST FILE
   check_file = os.path.exists("Cau3C.INP")
   if check_file == False:
       print ("Ban can tao file input")
   
   print ("file_size_3: ",file_size)
   print ("Data_file_3: ",data_file_3)
   
   xuly()
   file_3_read.close() #đóng file input 
   file_3_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()
