height = [ 1,2,4,5,6,7,8,9,15]
left = 0
right = len(height)-1
max =0
while left<right:
    width = right -left
    h = min(height[left],height[right])
    area = width * h
    if area > max:
        max= area

    if height[left]<height[right]:
        left+=1
    else:
        right-=1
print(max)       