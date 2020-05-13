# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:46:13 2019

@author: HadesSecurity
"""

"""
Viết chương trình thực hiện các yêu cầu sau:
- Nhập: từ tập tin văn bản Cau6C.inp xâu ký tự S có không quá 200 ký tự.
- Xử lý:
    + Loại bỏ các ký tự không phải ký tự chữ và khoảng trắng khỏi S.
    + Sau đó, tìm MAX là số ký tự của từ dài nhất trong xâu S. Biết: từ là một
    nhóm các ký tự liên tiếp khác khoảng trắng.
- Xuất: ra tập tin văn bản Cau6C.out giá trị của MAX.
        Ví dụ: nếu S = ‘ Cong1 nghe2 34 tho@ng tin5 ’ thì từ dài nhất là ‘thong’
        có số ký tự là MAX =5.
------------------------------------------------------------------------
"""

import os

#GET FILE
file_size = os.path.getsize("Cau6C.INP")
#Mở đọc file
file_6_read = open("Cau6C.INP","r")
data_file_6 = file_6_read.read() 
#Mở viết file
file_6_write= open("Cau6C.OUT","w")

#hàm xử lý chương trình
def xuly():
    #GET SIZE FILE
    output = ""  
    for i in range(file_size):
        #kiểm tra xem ký tự đã truyền có phải là chữ cái không hoặc khoảng cách ko?.
        if data_file_6[i].isalpha() or data_file_6[i] == " ":
            output = output+data_file_6[i]
            x=output
            x=" ".join(x.split()) # xóa hai dau cach trùng nhau hoặc cuôi câu
    
    # cắt từ theo khoảng trắng,đặt từ vào mảng mới        
    new_arr = x.split(" ")
    # đo chiều dài của từ
    # lấy một từ một lần, đếm các chữ cái liên tiếp
    # trả lại các chữ cái dài nhất liên tiếp
    file_6_write.write(str(len(max(new_arr, key=len))))        

# Hàm tương đương với hàm main trong C/C++
def main():
   print ("Cau6_Nhom C") 
   
   #CHECK EXIST FILE
   check_file = os.path.exists("Cau6C.INP")
   if check_file == False:
       print ("Ban can tao file input")
   
   print ("file_size_6: ",file_size)
   print ("Data_file_6: ",data_file_6)
   
   xuly()
   
   file_6_read.close() #đóng file input 
   file_6_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()