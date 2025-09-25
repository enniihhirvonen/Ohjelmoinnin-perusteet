print("Program starting.\nEstimate how many minutes you spent on programming...")

T1=input("A1_T1: ")
T2=input("A1_T2: ")
T3=input("A1_T3: ")
T4=input("A1_T4: ")
T5=input("A1_T5: ")
T6=input("A1_T6: ")
T7=input("A1_T7: ")

T1=int(T1)
T2=int(T2)
T3=int(T3)
T4=int(T4)
T5=int(T5)
T6=int(T6)
T7=int(T7)

Numbers=[T1, T2, T3, T4, T5, T6, T7]

print("In total you spent", sum(Numbers), "minutes on programming.")

Average=round(sum(Numbers)/len(Numbers), 2)

Integer=round(int(Average))

print("Average per task was", Average, "and same rounded to the nearest integer", Integer, "min.")

print("Program ending.")