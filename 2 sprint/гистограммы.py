
histogram: list[int] = [2,7,6,9,7,5,7,3,5]
maximum: int = histogram[0]
for i in range(len(histogram)):
    h_min:int = histogram[i]
    for j in range(i+1, len(histogram)):
        if histogram[j] < h_min: h_min = histogram[j]
        if (j - i + 1) * h_min > maximum:
            maximum = (j - i + 1) * h_min
            print(maximum)
print(maximum)