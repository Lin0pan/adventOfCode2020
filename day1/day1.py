def importNumbers(file):
    f = open(file, "r")
    nums = list(map(int, f.readlines()))
    f.close()
    return nums

def findPair(sum, nums):
    for i in nums:
        if (sum - i) in nums:
            return (i, (sum - i))


def main():
    pair = findPair(2020, importNumbers('input.txt'))
    solution = pair[0] * pair[1]
    print(solution)

if __name__ == "__main__":
    main()