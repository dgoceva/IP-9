while True:
    try:
        n = int(input('N='))
        if n > 0:
            break
        else:
            raise Exception('N must be greater than 0')
    except ValueError:
        print('Invalid number N')
    except Exception as e:
        print(e)
k = -1
while k <= 0:
    try:
        k = int(input('K='))
    except ValueError:
        print('Invalid number K')

nums = [int(input('X=')) for _ in range(n)]
print(nums)

nums1 = [x for x in nums if x > k]
print(nums1)

if len(nums1) > 0:
    mult = 1
    for i in range(1, len(nums1), 2):
        mult *= nums1[i]
    print(mult)

    print(nums1.index(min(nums1)))

nums2 = [x for x in nums if x <= k and x > 0]
print(nums2)

if len(nums2) > 0:
    print(max(nums2)-min(nums2))
