# balance : 초기 잔액을 설정하는 변수 초기화. 금액은 여러분 마음대로

# 사용자로부터 atm기계에 사용 목적에 맞는 기능을 선택할 수 있도록 사용기능 입력을 받는 기능을 구현

balance = 100000000

while True:
    num = input("사용하실 기능을 선택해 주세요. (1. 입금, 2. 출금, 3. 입출금 내역 영수증, 4. 종료)")
    
    if num == '4':
        break

    if num == '1':
        pass

    if num == '2':
        pass

    if num == '3':
        pass
    
print(f'서비스를 종료합니다.현재 잔액은 {balance}원 입니다.')