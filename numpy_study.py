import numpy as np

# 넘파이 공부
# 1차원
def array_1():
    a1 = np.array([1, 2, 3, 4, 5])
    print(a1)
    print(type(a1)) # 차원을 의미하는 'numpy.ndarray' 타입
    print(a1.shape) # shape = 어레이(배열)의 모습을 알려주는 속성 / (5,) = 5개의 element가 있다. + 1차원 배열이다(2번째 자리가 공백일 경우)
    print(a1[0], a1[1], a1[2], a1[3], a1[4])
    a1[0] = 4
    a1[1] = 5
    a1[2] = 6
    print(a1)

# 2차원
def array_2():
    a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    print(a2)
    print(a2.shape) # (4, 3) = 4개의 상위 element 안에 3개의 하위 element가 있다. / 앞 숫자가 상위 단계를 의미하는 듯?
    print(a2[0, 0], a2[1, 1], a2[2, 2])

# 3차원
def array_3():
    a3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                   [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                   [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                   [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
    print(a3)
    print(a3.shape) # (4, 3, 3) = 4개의 상위 element 안에 3개의 중간 element가 있고 그 안에 3개의 하위 element가 있다.
    
def method_1():
    a1 = np.array([1, 2, 3, 4, 5])
    a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    a3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                   [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                   [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                   [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
    # zeros() = 모든 요소를 0으로 초기화
    zero = np.zeros(10) # 0으로 채워진 10개의 요소로 배열을 만듬
    print(zero)
    # ones() = 모든 요소를 1로 초기화
    one = np.ones((3, 3)) # 1로 채워진 (3x3)구조로 2차원 배열을 만듬(zeros도 동일)
    print(one) 
    # full() = 모든 요소를 지정한 값으로 초기화
    full = np.full((3, 3), 1.23) # 1.23으로 채워진 (3*3)구조로 2차원 배열을 만듬
    print(full)
    # eye() = 단위행렬(identity matrix) 생성 - 주대각선의 원소가 모두 1이고 나머지 원소는 모두 0인 정사각 행렬
    eye = np.eye(3) # 가로,세로가 3개인 (3*3)구조의 '정사각형' 2차원 배열 만듬 but, 왼쪽 위부터 오른쪽 아래를 잇는 대각선만 1이고 나머지는 0인 배열
    print(eye)
    # tri() = 삼각행렬 생성
    tri = np.tri(3) # 가로, 세로가 3개인 (3*3)구조의 '정사각형' 2차원 배열 만듬 but, 왼쪽 위부터 오른족 아래를 잇는 대각선과 왼쪽에 삼각형이 1이고 나머지는 0인 배열
    print(tri)
    # empty() = 초기화되지 않는 배열 생성
    # 장점 : 초기화가 없어서 배열 생성비용 저렴하고 빠름
    # 단점 : 초기화되지 않아서 기존 메모리 위치에 존재하는 값이 있음(어떤 값이 올지 모름)
    empty = np.empty(10) # 메모리 내에 있는 값을 바탕으로 10개의 1차원 배열 생성(메모리 내 값이 없으면 0으로 생성)
    print(empty)
    # _like() = 지정된 배열과 shape가 같은 행렬 생성
    zero_like = np.zeros_like(a1) # a1는 1차원 배열의 리스트로 0으로 만들어진 1차원 배열을 만듬
    one_like = np.ones_like(a2) # a2는 2차원 배열의 리스트로 1로 만들어진 2차원 배열을 만듬
    full_like = np.full_like(a3, 10) # a3는 3차원 배열의 리스트로 '10'으로 만들어진 3차원 배열을 만듬
    empty_like = np.empty_like(a3) # a3는 3차원 배열의 리스트로 메모리 내 값으로 만들어진 3차원 배열을 만듬
    print(zero_like)
    print(one_like)
    print(full_like)
    print(empty_like)

def method_2():
    # 생성한 값으로 배열 생성
    # arange() = 정수 범위로 배열 생성
    arange = np.arange(0, 30, 2) # 파이썬 기본 함수의 arange와 동일한 기능 + 배열로 생성(0부터, 30까지, 2의 간격으로)
    print(arange)
    # linspace() = 범위 내에서 균등 간격의 배열 생성
    linspace = np.linspace(0, 1, 5) # 0부터 1까지 균등한 간격으로 5개의 요소를 가진 배열 생성
    print(linspace)
    # logspace() = 범위 내에서 균등간격으로 로그 스케일로 배열 생성

if __name__ == "__main__":
    # array_1() # 1차원 배열
    # array_2() # 2차원 배열
    # array_3() # 3차원 배열
    # method_1() # 다양한 매소드(방법)1
    method_2() # 다양한 매소드(방법)2