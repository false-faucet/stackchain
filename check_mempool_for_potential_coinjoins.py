def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        print ("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  
    
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 
   

if __name__ == "__main__":
    subset_sum(x, y) #where x is an array with the USD denominations of current mempool stacks
                     #where y is the current stack height + 1, or any stack height you are looking for.

    #Outputs:
    #sum([3, 8, 4])=15
    #sum([3, 5, 7])=15
    #sum([8, 7])=15
    #sum([5, 10])=15

# Thank you 
# https://stackoverflow.com/questions/4632322/finding-all-possible-combinations-of-numbers-to-reach-a-given-sum
