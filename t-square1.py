# Python program to perform t-square test when one sample is given 

import scipy.stats as stats

# level of significance
alpha = float(input("Enter level of significance:  "))

# mean data given
mean_val = int(input("Enter mean value given:  "))

# taking datas as input and converting that to list
input_data = input("Enter datas seperated by space:  ")
print("\n")
data = input_data.split()

for i in range(len(data)):
    data[i] = int(data[i])

# performing t test
t, p = stats.ttest_1samp(data, mean_val)

print("t value:  " + str(t))
print("p value:  " + str(p))

# validating null hypothesis
if (p <= alpha):
    print("Null Hypothesis (h0) rejected!")
else:
    print("Null Hypothesis (h0) accepted!")