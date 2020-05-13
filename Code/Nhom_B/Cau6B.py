"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Viết chương trình thực hiện các yêu cầu sau:
    - Nhập: từ tập tin văn bản Cau6B.inp số nguyên dương N, N < 10^3 ,
            và dãy số nguyên K gồm N phần tử có giá trị nằm trong đoạn [10^9,10^9] .
    - Xử lý: tìm giá trị nhỏ nhất MIN và vị trí cuối cùng POS của MIN trong dãy số K.
    - Xuất: ra tập tin văn bản Cau6B.out giá trị của MIN và POS, mỗi giá trị trên 1 dòng.
            Ví dụ: Nếu N = 8 và dãy K = (50, 40, 60, 10, 20, 60, 30, 10)    
                   thì MIN = 10 và POS = 8
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

file_6_read = open("Cau6B.INP","r")
file_6_write= open("Cau6B.OUT","w")

indata = file_6_read.read(1)
matrix=file_6_read.read().split()

#Hàm nhập 
def nhap():   
   m=int(indata)
   return m

#hàm xử lý chương trình    
def xuly(m):
    min=matrix[0]
    vt=0
    for i in range (0,m):
        if(int(min) > int(matrix[i])):
            min=matrix[i]
    for i in range (0,m):        
        if(int(min)==int(matrix[i])):
            vt = i+1
#            break
    file_6_write.write("MIN= "+ min + "\nPOS= "+ str(vt))

# Hàm tương đương với hàm main trong C/C++
def main(): 
   m=nhap()    
   xuly(m)
   file_6_read.close() #đóng file input 
   file_6_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()




