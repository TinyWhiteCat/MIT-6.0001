# Problem Set 4A
# Name: cococat
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutations = []
    new_permutations = []
    i = 0
    
    if len(sequence) == 1:
        permutations = [sequence[0]]
        return permutations
    else:
        str = sequence[0]
        permutations = get_permutations(sequence[1:])
        while i < len(permutations):
            sequence = permutations[i]
            j = 0
            while j < len(sequence) + 1:
                new_sequence = sequence[:j] + str + sequence[j:]
                new_permutations.append(new_sequence)
                j += 1
            i += 1
        k = 0
        
        while k < len(new_permutations):
            string = new_permutations[k]
            index = k + 1
            for e in new_permutations[(k+1):]:
                if e == string:
                    new_permutations.pop(index)
                else:
                    index += 1
            k += 1                   
            
        return new_permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'aba'
    print('Input:', example_input)
    print('Expected Output:', ['aba', 'aab', 'baa'])
    print('Actual Output:', get_permutations(example_input))    
