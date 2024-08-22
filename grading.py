students_list: list = [['Umar',78],['Ali',89],['Ahmad',93]]
for listItem in students_list:
    marks = listItem[1]
    if marks >= 90:
        grade =  "A"
    elif marks >= 80:
        grade =  "B"
    elif marks >= 70:
        grade =  "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade =  "F"
    print(f"Student: {listItem[0]}, Marks: {marks}, Grade: {grade}")

    
