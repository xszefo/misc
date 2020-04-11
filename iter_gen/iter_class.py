#!/usr/bin/python3

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        value_to_return = self.start
        self.start += 1

        return value_to_return


class MyRange2:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        while self.start < self.end:
            curr = self.start
            self.start += 1
            yield curr

nums = MyRange(1,10)
nums2 = MyRange2(11,20)

print('n1 n2')
for n1, n2 in zip(nums,nums2):
    print('{}  {}'.format(n1, n2))
