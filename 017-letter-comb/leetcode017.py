class Solution(object):

    def letterCombinations0(self, digits):
        """
        Python: one line solution using reduce
        # Tutorial on reduce() at http://www.python-course.eu/lambda.php
        """
        if (len(digits) == 0):
            return []
        kvmap = {'2': 'abc',
                 '3': 'def',
                 '4': 'ghi',
                 '5': 'jkl',
                 '6': 'mno',
                 '7': 'pqrs',
                 '8': 'tuv',
                 '9': 'wxyz'}
        return reduce(lambda acc, dgt: [x+y for x in acc for y in kvmap[dgt]], digits, [''])
        # So the third argument of reduce is an initializer

        #return reduce(lambda a, d: [x+y for x in kvmap[a] for y in kvmap[d]], digits)
        # This is a working version without initializer


        '''
        Note: Why does reduce(lambda x,y:x+y, L) returns the sum of the whole list?
        See https://docs.python.org/3/library/functools.html#functools.reduce for an Python equivalent of what reduce() does.
        def reduce(function, iterable, initializer=None):
            it = iter(iterable)
            if initializer is None:
                value = next(it)
            else:
                value = initializer
            for element in it:
                value = function(value, element)
            return value
        '''
    def letterCombinations(self, digits):
        # Without using reduce().
        if (len(digits) == 0):
            return []
        kvmap = {'2': 'abc',
                 '3': 'def',
                 '4': 'ghi',
                 '5': 'jkl',
                 '6': 'mno',
                 '7': 'pqrs',
                 '8': 'tuv',
                 '9': 'wxyz'}
        res = ['']
        for d in digits:
            tmp = []
            for item in res:
                for y in kvmap[d]:
                    tmp.append(item + y)
                #print "res:", res
            res = tmp
        return res

if __name__ == "__main__":
    s = Solution()
    print "that of '23': ", s.letterCombinations("23")
