# Python program to find out Pearson's Correlation Coefficient(r)
import scipy.stats as stats 

# taking datas as input and converting that to list
input_data1 = input("Enter elements of first data seperated by a space:  ")
print("\n")
data1 = input_data1.split()

for i in range(len(data1)):
    data1[i] = float(data1[i])


input_data2 = input("Enter elements of first data seperated by a space:  ")
print("\n")
data2 = input_data2.split()

for i in range(len(data2)):
    data2[i] = float(data2[i])

# input_data3 = input("Enter elements of first data seperated by a space:  ")
# print("\n")
# data3 = input_data3.split()

# for i in range(len(data3)):
#     data3[i] = int(data3[i])

# calculating correlation coefficient
correlation_coefficient, p_val = stats.pearsonr(data1, data2)

print("Correlation Coefficient:  " + str(correlation_coefficient))