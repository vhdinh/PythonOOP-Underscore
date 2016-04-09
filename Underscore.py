class Underscore(object):

    def map(self, list, mapLamb):
        for i in range(0, len(list)):
            list[i] = mapLamb(list[i])
        return list

    def reduce(self,list,lamb):
        # your code here
        sum = 0
        for i in range(0,len(list)):
            sum = sum + list[i]
        return sum

    def find(self, list, lamb):
        # your code here
        arr = []
        for i in list:
            if lamb(i):
                arr.append(i);
        arr = arr[0]
        return arr

    def filter(self, list,lamb):
        # your code
        arr = []
        for i in list:
            if lamb(i):
                arr.append(i);
        return arr


    def reject(self, list, lamb):
        # your code
        for i in list:
           if lamb(i):
               list.remove(i);
        return list

# you just created a library with 5 methods!
# let's create an instance of our class
top = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = top.reduce([1, 2, 3, 4, 5, 6], lambda x: x + 2)
# should return [2, 4, 6] after you finish implementing the code above

print evens
