"""
Viết chương trình thực hiện các yêu cầu sau:
- Nhập: từ tập tin văn bản Cau1C.inp xâu ký tự S có không quá 200 ký tự.
- Xử lý:
    + Loại bỏ các ký tự không phải ký tự chữ và khoảng trắng khỏi S.
    + Sau đó, đếm số từ C của S. Biết: từ là một nhóm các ký tự liên tiếp khác
    khoảng trắng.
- Xuất: ra tập tin văn bản Cau1C.out giá trị của C.
    Ví dụ: nếu S = ‘ Cong1 nghe2 34 tho@ng tin5 ’ thì S có C = 4 từ là
            ‘Cong’, ‘nghe’, ‘thong’, ‘tin’.

"""
import os

#GET FILE
file_size = os.path.getsize("Cau1C.INP")
#Mở đọc file
file_1_read = open("Cau1C.INP","r")
data_file_1 = file_1_read.read() 
#Mở viết file
file_1_write= open("Cau1C.OUT","w") 

#hàm xử lý chương trình
def xuly():
    #GET SIZE FILE
    output = ""
    dem=0
    for i in range(file_size):
        #kiểm tra xem ký tự đã truyền có phải là chữ cái không hoặc khoảng cách ko?.
        if data_file_1[i].isalpha() or data_file_1[i] == " ":
            output = output+data_file_1[i]
            x=output
            x=" ".join(x.split()) # xóa hai dau cach trùng nhau hoặc cuối câu
            
    for i in range (file_size): # dem so chu trong day
        if data_file_1[i]==" ":
            dem=dem+1    
    file_1_write.write("S=" + x+"\nC= "+str(dem))


# Hàm tương đương với hàm main trong C/C++
def main():
   print ("Cau1_Nhom C") 
   
   #CHECK EXIST FILE
   check_file = os.path.exists("Cau1C.INP")
   if check_file == False:
       print ("Ban can tao file input")
   
   print ("file_size_1: ",file_size)
   print ("Data_file_1: ",data_file_1)
   
   xuly()
   file_1_read.close() #đóng file input 
   file_1_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()
