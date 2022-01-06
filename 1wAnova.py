# Python program to find out F value of a One Way Anova Table

import scipy.stats as stats


# level of significance
alpha = float(input("Enter level of significance in decimal: "))

# input datas as set of lists
input_row1 = input("Enter elements of first row seperated by a space:  ")
print("\n")
row1 = input_row1.split()

for i in range(len(row1)):
    row1[i] = int(row1[i])


input_row2 = input("Enter elements of first row seperated by a space:  ")
print("\n")
row2 = input_row2.split()

for i in range(len(row2)):
    row2[i] = int(row2[i])

input_row3 = input("Enter elements of first row seperated by a space:  ")
print("\n")
row3 = input_row3.split()

for i in range(len(row3)):
    row3[i] = int(row3[i])


F_val, p_val = stats.f_oneway(row1, row2, row3) 


print("F value:  " + str(F_val))
print("p value:  "+ str(p_val))

# Validating null hypothesis
if p_val < alpha:
    print("Null Hypothesis rejected!")
else:
    print("Null hypothesis accepted!")