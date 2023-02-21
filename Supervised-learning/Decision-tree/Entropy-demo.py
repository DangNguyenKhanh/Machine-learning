import math as m

# dataset is 100 elements 80 yes - 20 no
yes = 80 / 100
no = 20 / 100
entropy = -(yes * m.log(yes) + no * m.log(no))
print(entropy)      # 0.5

# suppose to feature A: split dataset to 2 subset 50(50yes) - 50(30yes, 20no)
print("feature A: 50y - 30y & 20n")
# subset 1
yes = 50/50
no = 0/50
entropy1 = -(yes * m.log(yes))
print(entropy1)     # 0

# subset 2
yes = 30/50
no = 20/50
entropy2 = -(yes * m.log(yes) + no * m.log(no))
print(entropy2)     # 0.67

# weight average
entropy = 50/100 * entropy1 + 50/100 * entropy2
print(entropy)      # 0.33 <- choose feature A for split criteria

# suppose to feature B: split dataset to 2 subset 50(40yes, 10no) - 50(30yes, 20no)
print("feature B: 40y & 10n - 40y & 10n")
# subset 1
yes = 40/50
no = 10/50
entropy1 = -(yes * m.log(yes) + no * m.log(no))
print(entropy1)     # 0.5

# subset 2
yes = 40/50
no = 10/50
entropy2 = -(yes * m.log(yes) + no * m.log(no))
print(entropy2)     # 0.5

# weight average
entropy = 50/100 * entropy1 + 50/100 * entropy2
print(entropy)      # 0.5

# suppose to feature C: split dataset to 2 subset 50(40yes, 10no) - 50(30yes, 20no)
print("feature C: 35y & 15n - 45y & 5n")
# subset 1
yes = 35/50
no = 15/50
entropy1 = -(yes * m.log(yes) + no * m.log(no))
print(entropy1)     # 0.61

# subset 2
yes = 45/50
no = 5/50
entropy2 = -(yes * m.log(yes) + no * m.log(no))
print(entropy2)     # 0.32

# weight average
entropy = 50/100 * entropy1 + 50/100 * entropy2
print(entropy)      # 0.46


