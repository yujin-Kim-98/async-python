from black import re
import requests


def io_bound_func():
    result = requests.get("https://google.com")
    return result


if __name__ == "__main__":
    for i in range(10):
        result = io_bound_func()
    print(result)

# 블로킹 : 바운드에 의해 코드가 멈추게 되는 현상이 일어나는 것
