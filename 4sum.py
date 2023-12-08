# https://leetcode.com/problems/4sum/

def solution(nums, target):
    sorted_nums = sorted(nums)
    print(sorted_nums)
    results = []
    a,b,c,d = 0,1,2,3 

    while a < len(nums)-4:
        
        # collect values
        a_val = sorted_nums[a]
        b_val = sorted_nums[b]
        c_val = sorted_nums[c]
        d_val = sorted_nums[d]
        this_val = [a_val, b_val, c_val, d_val]
        print(sorted_nums)
        print(this_val)

        # check if fitting target
        if sum(this_val)== target:
            print('fits target')
            results.append(this_val)
            if a >= len(nums) -3:
                break
            a+=1 
            b,c,d=a+1, a+2, a+3
            continue
                
        # check if greater than target, if so break and reset
        # if sum(this_val) >= target:
        #     print('past target')
        #     if a == len(nums) -4:
        #         break
        #     a+=1 
        #     b,c,d=a+1, a+2, a+3
        #     continue

        # move pointer d
        if d < len(nums) -1:
            print('move d', d)
            d+=1
            continue
        # move pointer c
        if c < len(nums) -2:
            print('move c')
            c+=1
            continue
        # move pointer b
        if b < len(nums) -3:
            print('move b')
            b+=1
            continue

    return results


nums = [1,0,-1,0,-2,2]
target = 0
expect= [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
result = solution(nums, target)
print(f'{nums=}, {target=}, \n{expect=}, \n{result=}')

nums = [2,2,2,2,2]
target = 8
expect= [[2,2,2,2]]
result = solution(nums, target)
print(f'{nums=}, {target=}, \n{expect=}, \n{result=}')
