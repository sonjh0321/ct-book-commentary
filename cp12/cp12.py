"""
문제1
    기본 인수, 함수 선언 줄에서 괄호 안에서 이름을 설정해주면 됨.
    def function(arg1, arg2)
"""

"""
문제2
    선택 인수, 함수 선언 줄에서 괄호 안에서 이름을 설정해주면 됨.
    대신 선택하지 않은 경우, 기본 값 적용을 위해서 기본 값을 설정해야 함.
    def function(arg1=1, arg2='a')
"""

"""
문제3
    stop, start=0, step=1
    문제가 살짝 이상함. range는 원래 인수가 1개일 때, 인수가 2개일 때, 인수가 3개일 때 각 경우를 나눠서 작동하므로 위치 기반 인수들만 존재하면 됨.
"""

"""
문제4
    *, **
    위치 기반 인수를 패킹 할 때는 *
    키워드 기반 인수를 패킹 할 때는 **
    
    def function(*arg, **kwarg)에서
    function(1, 2, 3, 4, a=1, b=2, c=3)을 호출하면
    arg에는 (1, 2, 3, 4)가, kwarg에는 {'a':1, 'b':2, 'c':3}이 들어감.
"""

"""
문제5
    def function(*fruit):
        for i in fruit:
            print(i)
"""

"""
문제6
    def print_fruit(*args):
        fruit = list(args)
        print(len(fruit))
        print(fruit)
"""

"""
문제7
    전체 키워드 인수 중 중간 인수를 생략할 때는, 반드시 키워드 형태로 사용해야 한다.
    예를 들어 아래 함수에서 arg1과 arg3만 설정하고자 할 때는 반드시 키워드 형태로 호출해야 한다. function(arg1=10, arg3=False)
    그러나 arg1, arg2, arg3 모두 설정할 때는 위치 형태로 호출해도 된다. function(10, 0, False)
    def function(arg1=None, arg2=2, arg3=True):
"""

"""
문제8
    *, **
    위치 기반 인수를 언패킹 할 때는 *
    키워드 기반 인수를 언패킹 할 때는 **
    
    def function(a1, a2, a3, b1=1, b2=2)에서
    function(*(1, 2, 3), **{'b1':10, 'b2':20})을 호출하면
    a1에는 1, a2에는 2, a3에는 3,
    b1에는 10, b2ㅇ에는 20이 들어감. 
"""
