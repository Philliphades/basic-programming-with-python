"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Viết chương trình thực hiện các yêu cầu sau:
    - Nhập: từ tập tin văn bản Cau2.inp số nguyên dương N, N <10^3 , và dãy số
    nguyên K gồm N phần tử có giá trị nằm trong đoạn [-10^9,10^9] .
    - Xử lý: đếm số phần tử dương C của dãy K. Nếu C > 0 thì tìm giá trị dương
            nhỏ nhất MIN.  
    - Xuất: ra tập tin văn bản Cau2.out giá trị của C và MIN nếu C > 0, mỗi giá
            trị trên 1 dòng.  
    Ví dụ: Nếu N = 8 và dãy K = (50, 40, 60, -10, 20, -60, 30, 10) thì C = 6 và MIN = 10
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

file_10_read = open("Cau10B.INP","r")
file_10_write= open("Cau10B.OUT","w")
indata = file_10_read.read(1)
matrix=file_10_read.read().split()

#Hàm nhập 
def nhap():   
   m=int(indata)
   return m

#hàm xử lý chương trình    
def xuly(m):
    dem = 0
    min=9999999
    for i in range (0,m):
        if(int(matrix[i])>0):
            dem=dem +1
            if (int(matrix[i])<int(min)):
                min=matrix[i]
    file_10_write.write("C= "+ str(dem) + "\nMIN= "+ str(min))
    
# Hàm tương đương với hàm main trong C/C++
def main(): 
   m=nhap()    
   xuly(m)
   file_10_read.close() #đóng file input 
   file_10_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()