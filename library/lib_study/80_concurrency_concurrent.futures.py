import concurrent.futures
import shutil

print("-------------------ThreadPoolExecutor")

"""
def myPrint(a, b):
    print(a, b)
    return 3


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:
    s1 = e.submit(myPrint, 'src1.txt', 'dest1.txt')
    s2 = e.submit(myPrint, 'src2.txt', 'dest2.txt')
    # e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
    # e.submit(shutil.copy, 'src2.txt', 'dest2.txt')
    # e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
    # e.submit(shutil.copy, 'src4.txt', 'dest4.txt')
    # 获取返回值1
    # for future in concurrent.futures.as_completed([s1, s2]):
    #     print(future.result())  # 获取返回值;
    # 获取返回值2
    # finished, pending = concurrent.futures.wait([s1, s2], return_when=concurrent.futures.ALL_COMPLETED)
    # for future in finished:
    #     print(future.result())  # 获取返回值;

import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']


# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
"""
print("-------------------ProcessPoolExecutor")

# ProcessPoolExecutor

import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

# if __name__ == '__main__':
#     main()
