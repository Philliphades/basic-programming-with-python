"""
Viết chương trình thực hiện các yêu cầu sau:
    -Nhập: từ tập tin văn bản Cau3B.inp số nguyên dương N, N < 10^2 , 
            và ma trận vuông A kích thước N hàng,
            N cột chứa các giá trị nguyên nằm trong đoạn [10^4 ,10^4] .
    -Xử lý: tìm giá trị lớn nhất MAXC trên đường chéo chính và giá trị nhỏ
            nhất MINP trên đường chéo phụ của ma trận A.
    -Xuất: ra tập tin văn bản Cau3B.out giá trị của MAXC và MINP, mỗi giá trị trên 1 dòng.
    Ví dụ: Nếu N = 3 và ma trận A = [(50, 40, 60), (10, 20, 80), (90, 0, 70)] thì
            MAXC = 70 và MINP = 20.

"""

file_3_read = open("Cau3B.INP")
file_3_write= open("Cau3B.OUT","w")
_m=file_3_read.read(1)
matrix=file_3_read.read()
matrix = [item.split() for item in matrix.split('\n')[:-1]]

#Hàm nhập 
def nhap():   
   m=int(_m)
   return m

#hàm xử lý chương trình    
def xuly(m):
    max=0 
    min=9999
    #print("max",max)
    for i in range (0,m):
        for j in range (0,m):
            if(int(matrix[i][i]) > int(max)):
                max=matrix[i][i]
                
    for i in range (0,m):
        for j in range (0,m):
            if(int(matrix[i][m-i-1]) < int(min)):
                min=matrix[i][m-i-1]
    file_3_write.write("MAXC= "+ max + "\nMINP= "+ min)
    
# Hàm tương đương với hàm main trong C/C++
def main(): 
   m=nhap()    
   xuly(m)
   file_3_read.close() #đóng file input 
   file_3_write.close() #đóng file đóng file output
   print ("done")
   
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()

