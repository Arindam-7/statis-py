# Python program to perform t-square test when two independent samples are given 

import scipy.stats as stats

# level of significance
alpha = float(input("Enter level of significance:  "))

# taking datas as input and converting that to list
input_data1 = input("Enter first set of data seperated by space:  ")
print("\n")
data1 = input_data1.split()

for i in range(len(data1)):
    data1[i] = int(data1[i])


input_data2 = input("Enter second set of data seperated by space:  ")
print("\n")
data2 = input_data2.split()

for i in range(len(data2)):
    data2[i] = int(data2[i])

# performing t test, considering equal variance as true
t, p = stats.ttest_ind(a = data1, b = data2, equal_var = True)

print("t value:  " + str(t))
print("p value:  " + str(p))

# validating null hypothesis
if (p <= alpha):
    print("Null Hypothesis (h0) rejected!")
else:
    print("Null Hypothesis (h0) accepted!")