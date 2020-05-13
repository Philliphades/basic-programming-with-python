# -*- coding: utf-8 -*-
"""
Viết chương trình thực hiện các yêu cầu sau:
- Nhập: từ tập tin văn bản Cau9C.inp xâu ký tự S có không quá 200 ký tự.
- Xử lý:
    + Loại bỏ các ký tự không phải ký tự chữ và khoảng trắng khỏi S.
    + Sau đó, chuyển thành xâu ký tự X là dạng câu chuẩn của S. Biết: câu
    chuẩn là 1 xâu ký tự mà không có 2 khoảng trắng liên tiếp, bắt đầu và kết thúc
    không phải là khoảng trắng, ký tự bắt đầu là ký tự chữ HOA.
- Xuất: ra tập tin văn bản Cau9C.out xâu ký tự X.
        Ví dụ: Nếu S = ‘ co@ng1 nghe2 34 th$ong tin5 ’ thì X = ‘Cong nghe
        thong tin’.
------------------------------------------------------------------------

"""

import os

#GET FILE
file_size = os.path.getsize("Cau9C.INP")
#Mở đọc file
file_9_read = open("Cau9C.INP","r")
data_file_9 = file_9_read.read() 
#Mở viết file
file_9_write= open("Cau9C.OUT","w")

#hàm xử lý chương trình
def xuly():
    #GET SIZE FILE
    output = ""
    for i in range(file_size):
        #kiểm tra xem ký tự đã truyền có phải là chữ cái không hoặc khoảng cách ko?.
        if data_file_9[i].isalpha() or data_file_9[i] == " ":
            output = output+data_file_9[i]
            x=output
            x=" ".join(x.split()) # xóa hai dau cach trùng nhau hoặc cuôi câu  
            b=x.capitalize() #hàm in hoa chữ cái đầu tiên của chuỗi.
    file_9_write.write(b)

# Hàm tương đương với hàm main trong C/C++
def main():
   print ("Cau9_Nhom C") 
   
   #CHECK EXIST FILE
   check_file = os.path.exists("Cau9C.INP")
   if check_file == False:
       print ("Ban can tao file input")
   
   print ("file_size_9: ",file_size)
   print ("Data_file_9: ",data_file_9)
   
   xuly()
   file_9_read.close() #đóng file input 
   file_9_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()