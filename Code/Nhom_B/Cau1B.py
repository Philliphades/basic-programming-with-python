"""
Viết chương trình thực hiện các yêu cầu sau:
    - Nhập: từ tập tin văn bản Cau2.inp số nguyên dương N, N < 10^2 , và ma trận
            vuông A kích thước N hàng, N cột chứa các giá trị nguyên nằm trong đoạn
            [-10^4 ,10^4 ] .
    - Xử lý: tìm giá trị lớn nhất MAX của ma trận A và tổng SC của các phần tử
            trên đường chéo chính.
    - Xuất: ra tập tin văn bản Cau2.out giá trị của MAX và SC, mỗi giá trị trên một dòng.
            Ví dụ: Nếu N = 3 và ma trận A = [(50, 40, 60), (10, 20, 80), (90, 0, 70)] thì
                    MAX = 90 và SC = 50 + 20 + 70 = 140.
"""

file_1_read = open("Cau1B.INP")
file_1_write= open("Cau1B.OUT","w")
_m=file_1_read.read(1)
matrix=file_1_read.read()
matrix = [item.split() for item in matrix.split('\n')[:-1]]

#Hàm nhập 
def nhap():   
   m=int(_m)
   return m

#hàm xử lý chương trình    
def xuly(m):
    max=0
    sum=0
    for i in range (0,m):
        for j in range (0,m):
            if(int(matrix[i][j]) > int(max)):
                max=matrix[i][j]
    for i in range (0,m):
        for j in range (0,m):
            if (i==j):
                sum+=int(matrix[i][j])
    file_1_write.write("MAX= "+ str(max) + "\nSC= "+ str(sum))    

# Hàm tương đương với hàm main trong C/C++
def main(): 
   m=nhap()    
   xuly(m)
   file_1_read.close() #đóng file input 
   file_1_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()

