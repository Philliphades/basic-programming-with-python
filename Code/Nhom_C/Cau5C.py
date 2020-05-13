# -*- coding: utf-8 -*-
"""
Viết chương trình thực hiện các yêu cầu sau:
- Nhập: từ tập tin văn bản Cau5C.inp xâu ký tự S có không quá 200 ký tự.
- Xử lý:
    + Loại bỏ các ký tự không phải ký tự chữ khỏi S để được xâu X.
    + Sau đó, kiểm tra xem X có phải là một xâu ghép. Biết: xâu ghép là 1 xâu ký tự
        được tạo thành bằng cách viết liên tiếp K lần (K > 1) 1 xâu có độ dài ngắn hơn.
- Xuất: ra tập tin văn bản Cau5C.out xâu ký tự X và 
        giá trị lớn nhất của K nếu X là xâu ghép.
        Ví dụ: Nếu S = ‘AB@1 A2 BA B$ A5B ’ thì X = ‘ABABABAB’ và K = 4.

"""

import os

#GET FILE
file_size = os.path.getsize("Cau5C.INP")
#Mở đọc file
file_5_read = open("Cau5C.INP","r")
data_file_5 = file_5_read.read() 
#Mở viết file
file_5_write= open("Cau5C.OUT","w")

#hàm xử lý chương trình
def xuly():
    #GET SIZE FILE
    output = ""
    b=""
    max=0
    for i in range(file_size):
        #kiểm tra xem ký tự đã truyền có phải là chữ cái không hoặc khoảng cách ko?.
        if data_file_5[i].isalpha() or data_file_5[i] == " ":
            output = output+data_file_5[i]
            x=output
            x="".join(x.split()) 
    
    for i in range(0,len(x)):
        if(x.count(x[i])>1):
           b="la xau ghep"
           x.count(x[i])>max
           max=x.count(x[i])
        else:
           b="khong phai xau ghep"
    print(b)
    file_5_write.write("X: "+ x + "\nK: " + str(max))

# Hàm tương đương với hàm main trong C/C++
def main():
   print ("Cau5_Nhom C") 
   
   #CHECK EXIST FILE
   check_file = os.path.exists("Cau5C.INP")
   if check_file == False:
       print ("Ban can tao file input")
   
   print ("file_size_5: ",file_size)
   print ("Data_file_5: ",data_file_5)
   
   xuly()
   file_5_read.close() #đóng file input 
   file_5_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()