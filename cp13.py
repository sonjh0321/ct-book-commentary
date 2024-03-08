"""
문제1
    클래스는 객체를 만들기 위한 틀
"""

"""
문제2
    id
"""

"""
문제3
    import random
    print(random.randint(1, 20))
"""

"""
문제4
    class Name:
"""

"""
문제5
    클래스 변수는 클래스 정의 내부에 선언되지만 메서드 외부에 위치. 해당 클래스의 모든 인스턴스가 공유. 즉, 클래스 변수는 같은 클래스로 생성된 모든 객체가 접근할 수 있는 공통의 데이터를 저장.
    인스턴스 변수는 메서드 내부에서 self를 사용하여 선언되며, 각 인스턴스(객체)별로 독립적. 즉, 인스턴스 변수는 각 객체가 독립적으로 가지고 있는 데이터를 저장.
    아래는 실행 가능한 예시
"""
class MyClass:
    class_var = '클래스 변수'  # 클래스 변수

    def __init__(self, instance_var):
        self.instance_var = instance_var  # 인스턴스 변수


obj1 = MyClass('obj1의 인스턴스 변수')
obj2 = MyClass('obj2의 인스턴스 변수')
print(obj1.class_var)  # 출력: 클래스 변수
print(obj1.instance_var)  # 출력: obj1의 인스턴스 변수
print(obj2.class_var)  # 출력: 클래스 변수
print(obj2.instance_var)  # 출력: obj2의 인스턴스 변수

"""
문제6
   ['Python', 'Java', 'Ruby'] 
"""

"""
문제7
    def __init__(self):
        self.languages = list()
"""

"""
문제8
    import
"""
