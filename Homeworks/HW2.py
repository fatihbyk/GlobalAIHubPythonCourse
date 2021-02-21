Grades=[]
Students=[]
Dict=dict()
for i in range(0,5):
    SName=str(input("Please write Student name:"))
    Students.append(SName)
    TempGradeList = []
    for k in range(0,3):
        Grade=int(input("Please enter value"))
        if (Grade > 0) &(Grade<=100):
            TempGradeList.append(Grade)
    Grades.append(TempGradeList)
print(Grades)
print(Students)
Dict={Students[0]:(Grades[0][0]+Grades[0][1]+Grades[0][2])//3,Students[1]:(Grades[1][0]+Grades[1][1]+Grades[1][2])//3,
       Students[2]:(Grades[2][0]+Grades[2][1]+Grades[2][2])//3,Students[3]:(Grades[3][0]+Grades[3][1]+Grades[3][2])//3,
      Students[4]:(Grades[4][0]+Grades[4][1]+Grades[4][2])//3}
Sorted_dict=sorted(Dict.items(), key=lambda x: x[1], reverse=True)
print(Sorted_dict)
print(f"{Sorted_dict[0][0]} Congratulations you are the best !!")
