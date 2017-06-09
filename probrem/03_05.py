def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
# 定義に則って書かれていていいですね
# これは，速度がかなり遅いのですが，もっと早くするにはどうすればいいでしょう？
# ヒントは，fib(n) = fib(n-1) + fib(n-2) = fib(n-2) + fib(n-3) + fib(n-2)
# この時点ですでにfib(n-2)を2度計算していて無駄が出てますね
# 前の計算を，覚えておくようにするとどうでしょう？
