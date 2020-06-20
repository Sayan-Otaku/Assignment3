sub=int(input("Enter the number of subjects: - "))
c=0
for i in range(sub):
    marks=float(input("\nEnter the subject marks: - "))
    if marks>=35:
        print("Passed in this subject!!! Good Job!!!")
        c+=1
    else:
        print("Better luck next time!!!")
    marks=0
print("\nTotal number of subjects = {}\nPassed in subjects = {}".format(sub,c))
