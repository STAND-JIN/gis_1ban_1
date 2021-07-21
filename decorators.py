def decorator(func):
    def decorated(input_text):
        print('함수 시작')
        func(input_text)
        print('함수 끝!')
    return decorated

# 적용하고자 하는 함수 위에 @함수이름으로 표시해주기
@decorator
def hello_world(input_text):
    print(input_text)

hello_world('Hello_World!')
