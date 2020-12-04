import math
def factorial(n):
    """
    Tính giai thừa của n
    """
    if n <= 1:
        return 1;
    else:
        return n * factorial(n - 1);

def combination(i, N):
    """
    Tính c(i, N)
    """
    return factorial(N)/(factorial(i)*factorial(N - i));

def prob(n, p, r):
    return combination(n - r + 1, n)*(p ** n)*(1 - p)**r;

def infoMeasure(n, p, r):
    return -math.log(prob(n, p, r), 2);

def sumProb(N, p, r):
    """
    Tính tổng xác suất của các symbol n từ nguồn thông tin negbinomial
    n chạy từ 1 tới N
    """
    sum = 0;
    for i in range(1, N + 1):
        sum += prob(i, p, r);

    return sum;

def approxEntropy(N, p, r):
    """
    Tính entropy của nguồn thông tin negbinomial
    """
    sumHx = 0;
    for i in range(1, N + 1):
        sumHx += prob(i, p, r)*infoMeasure(i, p, r);
    return sumHx;

print(approxEntropy(5, 0.5, 2));
