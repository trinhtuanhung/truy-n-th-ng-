import math

def prob(n, p):
    return ((1-p)**(n-1))*p;

def infoMeasure(n, p):
    return -math.log(prob(n, p), 2);

def sumProb(N, p):
    """
    Có nhiều cách để chứng minh tổng xác suất của phân bố geometric bằng 1, ví dụ ta có thể cho N = 1000 và p = 0.5 để mô phỏng việc tung đồng xu.
    Sau đó kiểm chứng kết quả bằng cách in ra giá trị hàm sumProb.
    """
    sum = 0;
    for i in range(1, N + 1):
        sum += prob(i, p);
    return sum;

def approEntropy(N, p):
    """
    Vì entropy là giá trị trung bình của các nguồn tin nên hàm này sẽ tính được các nguồn tin geometric.
    Để chứng minh entropy của nguồn tin này bằng 0.5 ta lấy N = 1000, p = 0.5.
    """
    sumHx = 0;
    for i in range(1, N + 1):
        sumHx += prob(i, p) * infoMeasure(i, p);
    return sumHx;
        
