# I/O 바운드
# 1. 프로그램이 실행될 때 실행 속도가 I/O에 의해 제한됨을 의미
# 2. 사용자가 키보드로 숫자를 입력하는 경우 뿐만 아니라, 컴퓨터와 컴퓨터끼리 통신을 할 때도 I/O 바운드 발생
# 3. 어떤 프로그램에서 특정 웹에 요청을 하여 응답을 기다리는 코드가 있다고 하면 요청을 하는 것이 I가 되고 응답을 하는 것이 O가되는 I/O 바운드인 것

# 블로킹 : 바운드에 의해 코드가 멈추게 되는 현상이 일어나는 것

import requests


def io_bound_func():
    result = requests.get("https://google.com")
    return result


if __name__ == "__main__":
    for i in range(10):
        result = io_bound_func()
    print(result)
