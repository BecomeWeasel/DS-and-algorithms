class Array:
    def __init__(self):
        self.length=0
        self.data={}
    
    def get(self,index): # O(1)
        return self.data[index]
    
    def push(self,item): # O(1)
        self.data[self.length]=item
        self.length+=1

    def pop(self): # O(1)
        last_item=self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1

        return last_item

    def delete(self,index): # O(n)
        deleted_item=self.data[index]
        
        def shift_items(index):
            for i in range(index,self.length-1):
                self.data[i]=self.data[i+1]
        shift_items(index)

        del self.data[self.length-1]
        self.length-=1

        return deleted_item
    

new_array=Array()
new_array.push(3)
new_array.push(10)
new_array.push(4)
new_array.push(7)

print(new_array.get(0))
print(new_array.get(1))

print(new_array.delete(1))
print(new_array)