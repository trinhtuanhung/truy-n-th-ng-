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
    Tính C(i, n)
    """
    return factorial(N)/(factorial(i)*factorial(N - i));

def prob(n, p, N):
    return combination(n, N)*(p ** n)*(1 - p)**(N - n);

def infoMeasure(n, p, N):
    return -math.log(prob(n, p, N), 2);

def sumProb(N, p):
    """
    Tính tổng của xác suất của các symbol n của nguồn thông tin binomial
    n chạy từ 1 đến N
    """
    sum = 0 ;
    for i in range(1, N + 1):
        sum += prob(i, p, N);

    return sum;

def approxEntropy(N, p):
    """
    Tính entropy của phân bố binomial
    """
    sumHx = 0;
    for i in range(1, N + 1):
        sumHx += prob(i, p, N)*infoMeasure(i, p, N);
    return sumHx;

print(approxEntropy(3, 0.5));
