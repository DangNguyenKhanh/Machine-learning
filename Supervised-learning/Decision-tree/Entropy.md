> Entropy

Entropy is a measure of impurity or uncertainty in a set of data

entropy = -p_A * log2(p_A) - p_B * log2(p_B)         

vẫn dùng log2 cho dù có nhiều categorical như yes, no, maybe. Có nơi dùng log sẽ là log tự nhiên loge

entropy of a set of data is 0 if all the members of the set belong to the same class, and it is 1 if the members are evenly distributed among all the classes. Giá trị entropy từ 0 đến 1

Suppose we have a dataset with 100 data points and two possible classifications: "yes" and "no". Out of the 100 data points, 80 belong to the "yes" class and 20 belong to the "no" class.

The initial entropy of the dataset can be calculated as follows:

p(yes) = 80/100 = 0.8

p(no) = 20/100 = 0.2

Entropy = -[p(yes) * log2(p(yes)) + p(no) * log2(p(no))] = -[0.8 * log2(0.8) + 0.2 * log2(0.2)] = 0.72

Now, suppose we have a feature that can be used to split the dataset into two subsets. One subset contains 50 data points, all of which belong to the "yes" class. The other subset contains 50 data points, 20 of which belong to the "no" class and 30 of which belong to the "yes" class.

The entropy of the first subset is 0, since all data points belong to the same class. The entropy of the second subset can be calculated as follows:

p(yes) = 30/50 = 0.6

p(no) = 20/50 = 0.4

Entropy = -[p(yes) * log2(p(yes)) + p(no) * log2(p(no))] = -[0.6 * log2(0.6) + 0.4 * log2(0.4)] = 0.97

To calculate the entropy of the entire dataset after the split, we take a weighted average of the entropy of each subset:

Entropy = (50/100) * 0 + (50/100) * 0.97 = 0.48

By splitting the dataset on this feature, we were able to decrease the entropy of the dataset from 0.72 to 0.48

The goal is to select the feature that results in the greatest reduction in entropy, nên ta sẽ thực hiện điều này cho tất cả feature còn lại, xem feature nào giảm nhiều nhất thì ta chọn làm spliting criteria

