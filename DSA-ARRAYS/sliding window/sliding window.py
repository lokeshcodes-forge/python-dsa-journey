numbers =[4,2,7,3,5]
k =3
window_sum = 0

for i in range (k):
    window_sum+=numbers[i]
max_sum=window_sum

for i in range (k,len(numbers)):
    window_sum=window_sum-numbers[i-k]+numbers[i]
    max_sum=max(max_sum,window_sum)
print(max_sum)
    