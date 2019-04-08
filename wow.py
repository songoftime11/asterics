def fibonacci(n):
    fibo=0
    if(n==0 or n==1):
      fibo=1
    else:
      fibo=fibonacci(n-1)+fibonacci(n-2)
    return fibo
      
