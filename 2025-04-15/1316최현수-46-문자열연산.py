n = input("문장 입력 : ") # "Hello. I am studying Python."
print("#"*28)
print(f'대문자 변환 : {n.upper()}')
print(f'소문자 변환 : {n.lower()}')
print(f'문자열 길이 : {len(n)}')
print(f'공백으로 분리 : {n.split()}')
print(f'마침표로 분리 : {n.split(".")}')
print(f'o의 위치 : {n.index("o")}')
print(f'o의 개수 : {n.count("o")}')
print(f'Python을 AI로 교체 : {n.replace("Python", "AI")}')