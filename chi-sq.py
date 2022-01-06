# Python program to perform chi-square test

import scipy.stats as stats

# level of significance
alpha = float(input("Enter level of significance in decimal: "))

# taking datas as input and converting that to list
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

# input_row3 = input("Enter elements of first row seperated by a space:  ")
# print("\n")
# row3 = input_row3.split()

# for i in range(len(row3)):
#     row3[i] = int(row3[i])

# input_row4 = input("Enter elements of first row seperated by a space:  ")
# print("\n")
# row4 = input_row4.split()

# for i in range(len(row4)):
#     row4[i] = int(row4[i])


# performing chi-square test
categories = [row1, row2]
chi2, p, dof, exp = stats.chi2_contingency(categories)

print("Chi Square Value:  " + str(chi2))
print("Degrees of Freedom:  " + str(dof))

# validating null hypothesis
if p < alpha:
    print("Null Hypothesis rejected!")
else:
    print("Null hypothesis accepted!")