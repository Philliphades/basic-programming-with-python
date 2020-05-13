# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:39:34 2019

@author: HadesSecurity
"""

"""

Viết chương trình thực hiện các yêu cầu sau:
- Nhập: từ tập tin văn bản Cau10C.inp xâu ký tự S có không quá 200 ký tự.
- Xử lý:
    + Loại bỏ các ký tự không phải ký tự chữ khỏi S để được xâu X.
    + Sau đó, kiểm tra xem X có phải là một xâu ghép. Biết: xâu ghép là 1 xâu
    ký tự được tạo thành bằng cách viết liên tiếp K lần (K > 1) 1 xâu có độ dài ngắn
    hơn.
- Xuất: ra tập tin văn bản Cau10C.out xâu ký tự X và kết luận.
        Ví dụ: Nếu S = ‘AB@1 A2 BA B$ A5B ’ thì X = ‘ABABABAB’ là xâu ghép

"""

import os

#GET FILE
file_size = os.path.getsize("Cau10C.INP")
#Mở đọc file
file_10_read = open("Cau10C.INP","r")
data_file_10 = file_10_read.read() 
#Mở viết file
file_10_write= open("Cau10C.OUT","w")

#hàm xử lý chương trình
def xuly():
    #GET SIZE FILE
    output = ""
    b=""
    for i in range(file_size):
        #kiểm tra xem ký tự đã truyền có phải là chữ cái không hoặc khoảng cách ko?.
        if data_file_10[i].isalpha() or data_file_10[i] == " ":
            output = output+data_file_10[i]
            x=output
            x="".join(x.split()) # xóa hai dau cach trùng nhau hoặc cuôi câu
    
    for i in range(0,len(x)):
        if(x.count(x[i])>1):
           b="la xau ghep"           
        else:
           b="khong phai xau ghep"
    file_10_write.write("X= "+ x + " " + b)

# Hàm tương đương với hàm main trong C/C++
def main():
   print ("Cau10_Nhom C") 
   
   #CHECK EXIST FILE
   check_file = os.path.exists("Cau10C.INP")
   if check_file == False:
       print ("Ban can tao file input")
   
   print ("file_size_10: ",file_size)
   print ("Data_file_10: ",data_file_10)
   
   xuly()
   file_10_read.close() #đóng file input 
   file_10_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()