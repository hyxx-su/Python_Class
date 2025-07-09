with open("attendance.txt", "r") as f:
    print("출석한 학생들 : ")
    for line in f:
        print(line.strip())