class hashtable:
    def __init__(self):
        self.size=10
        self.arr=[None]*self.size
    def hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)+5
        return hash % self.size


    def set(self,key,value):
        h=self.hash(key)
        kv=(key,value)
        if self.arr[h] is None:
            self.arr[h]=kv

        else:
            ind1=self.search_slot(key,h)
            self.arr[ind1]=kv
        print(self.arr)


    def search_slot(self,key,h):
        list_ind=list(range(h,len(self.arr)))+list(range(0,h))
        for ind in list_ind:
            if self.arr[ind]==None:
                return ind
            if self.arr[ind][0][0]==key:
                return ind
        raise Exception("hashmap full")

    def get(self,key):
        h=self.hash(key)
        # if self.arr[h]==None:
        #     return
        list_ind = list(range(h, len(self.arr))) + list(range(0, h))
        for ind in list_ind:
            element=self.arr[ind]
            if element==None:
                return "not found"
            if element[0]==key:
                return element[1]

    def delete1(self, key):
        h = self.hash(key)
        list_ind = list(range(h, len(self.arr))) + list(range(0, h))

        for ind in list_ind:
            if self.arr[ind]!= None and self.arr[ind][0] == key:
                self.arr[ind]=None
                print(True)
        print(self.arr)

h = hashtable()
h.set('Bob','567-8888')
h.set('Ming','293-6753')
h.set('Ming','333-8233')
h.set('Ankit','293-8625')
h.set('Aditya','852-6551')
h.set('Alicia','632-4123')
h.set('Mike', '567-2188')
h.set('Aditya', '777-8888')
print(h.get('Bob'))
h.delete1('Mike')