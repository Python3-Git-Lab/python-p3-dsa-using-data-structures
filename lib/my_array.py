class MyArray:
    def __init__(self):
        self.dictionary = {}
        self.length = 0
    
    def push(self, value):
        """Add element to the end of array"""
        self.dictionary[self.length]= value
        self.length +=1
    
    def pop(self):
        """Remove and return last occurrence of specified value from array"""
        if self.length==0:
            return None
        self.length-=1
        return self.dictionary.pop(self.length)
    
arr= MyArray()
arr.push("Hello")
arr.push("World")
arr.push("I")
arr.push("am")
print(arr.dictionary) # Output: {0: 'Hello', 1: 'World', 2: 'I', 3: 'am'}

print(arr.pop())
print(arr.pop())

print(arr.dictionary) # Output: {0: 'Hello', 1: 'World'}