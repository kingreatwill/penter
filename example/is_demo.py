
import calendar

# 判断奇数偶数
print('even number.' if 3 % 2 == 0 else 'odd number.')

# 质数判断
# 素数（prime number）又称质数，有无限个。除了1和它本身以外不再被其他的除数整除。
# 一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），换句话说就是该数除了1和它本身以外不再有其他的因数。
def is_prime(num):
    # 质数大于 1
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                print(i, "*", num // i, "=", num)
                return False
                # break
        else:
            return True

    # 如果输入的数字小于或等于 1，不是质数
    else:
        return False

print("是否质数:", is_prime(6))

# 整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。
# 负数没有阶乘
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return factorial(n-1) * n

def factorial2(num):
    # 计算阶乘
    factorial = 1

    # 查看数字是负数，0 或 正数
    if num < 0:
        print("抱歉，负数没有阶乘")
    elif num == 0:
        print("0 的阶乘为 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("%d 的阶乘为 %d" % (num, factorial))

factorial2(3) # 6
print(factorial(3)) # 6

# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
def fibonacci(n):
  if n==0 :
      return 0
  elif n==1:
      return 1
  else:
      return fibonacci(n-1) + fibonacci(n-2)

print("{0}斐波那契数列".format(fibonacci(4)))

def fibonacci2(nterms):
    # 获取用户输入数据
    #nterms = int(input("你需要几项？"))

    # 第一和第二项
    n1 = 0
    n2 = 1
    count = 2

    # 判断输入的值是否合法
    if nterms <= 0:
        print("请输入一个正整数。")
    elif nterms == 1:
        print("斐波那契数列：")
        print(n1)
    else:
        print("斐波那契数列：")
        print(n1, ",", n2, end=" , ")
        while count < nterms:
            nth = n1 + n2
            print(nth, end=" , ")
            # 更新值
            n1 = n2
            n2 = nth
            count += 1
fibonacci2(10)

# 判断闰年
# 普通闰年:公历年份是4的倍数的，且不是100的倍数，为闰年。（如2004年就是闰年）；
# 世纪闰年:公历年份是整百数的，必须是400的倍数才是世纪闰年（如1900年不是世纪闰年，2000年是世纪闰年）；
def isleap(year):
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        print("{0}是闰年".format(year))
    else:
        print("{0}不是闰年(是平年)".format(year))


print(calendar.isleap(2008))
print(calendar.isleap(2000))
print(calendar.isleap(1900))

isleap(2008)
isleap(2000)
isleap(1900)
