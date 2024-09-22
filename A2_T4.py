print('Program starting.\nEstimate how many minutes you spent on programming...\n')
T1=float(input('A1_T1: '))
T2=float(input('A1_T2: '))
T3=float(input('A1_T3: '))
T4=float(input('A1_T4: '))
T5=float(input('A1_T5: '))
T6=float(input('A1_T6: '))
T7=float(input('A1_T7: '))
Lis1=[T1,T2,T3,T4,T5,T6,T7]
print(f'\nIn total you spent {int(round(sum(Lis1)))} minutes on programming.')
Avg=sum(Lis1)/len(Lis1)
if Avg % 1 ==0:
    print(f'Average per task was {sum(Lis1)/len(Lis1):.1f} min and same rounded to the nearest integer {int(round(sum(Lis1)/len(Lis1)))} min.\n')
else:
    print(f'Average per task was {sum(Lis1)/len(Lis1):.2f} min and same rounded to the nearest integer {int(round(sum(Lis1)/len(Lis1)))} min.\n')
print('Program ending.')