def importInput(file):
    f = open(file, "r")
    trees = f.readlines()
    f.close()
    return trees

def countTrees(trees, right, down):
    width = len(trees[0]) - 1 #there is a blank space at the end for some reason
    col = 0
    n_trees = 0

    for t in trees[::down]:
        if t[col] == '#':
            n_trees += 1
        
        col = (col + right) % width
    return n_trees

def main():
    trees = importInput('input.txt')
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    result = 1
    for s in slopes:
        tmp = countTrees(trees, s[0], s[1])
        result *= tmp
        print('The result for slope '+str(s)+' is '+str(tmp))

    print('the Product of all results is '+str(result))

if __name__ == "__main__":
    main()