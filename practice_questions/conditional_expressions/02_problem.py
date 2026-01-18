# 40 percent total marks needed by a student to pass and 30 percent in each subject. assume we have 3 subjects and write a program to find out if the student passed or failed 

subjects_marks = {

}

for i in range(0,3):
    subjects=input("enter subject name: ")
    marks=int(input("enter marks of the student"))
    subjects_marks.update({subjects:marks})

highest_score = int(input("enter the max marks a student can score: "))
minimum_pass_each_subject = (highest_score*30)/100
print("the minimum passing marks for each subject is: ",minimum_pass_each_subject)

total_passing_marks_overall = ((highest_score*3)*40)/100
print("overall passing marks required is: ",total_passing_marks_overall)

student_total_marks=sum(subjects_marks.values())
if(student_total_marks<total_passing_marks_overall):
    print("Student has failed")
else:
    failed_subject = False

    for subject, marks in subjects_marks.items():
        if marks < minimum_pass_each_subject:
            print(f"❌ Failed in {subject}")
            failed_subject = True

    if failed_subject:
        print("❌ Student has FAILED (subject-wise criteria not met)")
    else:
        print("✅ Student has PASSED")

