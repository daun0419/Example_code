def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

def main():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    print("=== 계산기 ===")
    while True:
        expr = input("계산식 입력 (예: 3 + 4), 종료: q\n> ").strip()
        if expr.lower() == 'q':
            break
        try:
            a, op, b = expr.split()
            result = operations[op](float(a), float(b))
            print(f"결과: {result}\n")
        except (ValueError, KeyError):
            print("올바른 형식으로 입력하세요. (예: 3 + 4)\n")

if __name__ == "__main__":
    main()
