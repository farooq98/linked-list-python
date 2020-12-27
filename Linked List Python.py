class Node:
    
    def __init__(self, value):
        self.data = value
        self.next_data = None

class Linked_List:

    def __init__(self, *args):
        self.__head = None
        self.__tail = None
        self.__length = 0 
        self.__iterator = None
        if args != ():
            for i in args:
                self.append(i)

    def __repr__(self):
        display = "["
        x = self.__head
        while x:
            if x.next_data is not None:
                display += str(x.data) + ", "
            else:
                display += str(x.data)
            x = x.next_data
        return display + "]"
        

    def __len__(self):
        return self.__length

    def __getitem__(self, index):
        if isinstance(index, int):
            index = self.__neg_index_chk(index)
            
            if index < self.__length:
                x = self.__head
                i = 0
                while x:
                    if i == index:
                        return x.data
                    x = x.next_data
                    i += 1
            else:
                raise IndexError("index Out of range")

        if isinstance(index, slice):
            obj = Linked_List()

            if index.start == None and index.stop == None and index.step == None:
                return self.copy()

            if index.start == None and index.stop != None:
                if index.step != None:
                    for i in range(0, index.stop, index.step):
                        obj.append(self[i])
                    return obj
                else:
                    for i in range(0, index.stop):
                        obj.append(self[i])
                    return obj

            if index.stop == None and index.start != None:
                if index.step != None:
                    for i in range(index.start, self.__length, index.step):
                        obj.append(self[i])
                    return obj
                else:
                    for i in range(index.start, self.__length):
                        obj.append(self[i])
                    return obj

            if index.start != None and index.stop != None:
                if index.step != None:
                    for i in range(index.start, index.stop, index.step):
                        obj.append(self[i])
                    return obj
                else:
                    for i in range(index.start, index.stop):
                        obj.append(self[i])
                    return obj

            if index.step != None and index.start == None and index.stop == None:
                for i in range(0, self.__length, index.step):
                    obj.append(self[i])
                return obj

    def __setitem__(self, index, data):
        self.__insert(index, data, "setitem")

    def __delitem__(self, index):
        self.pop(index)

    def __add__(self, other):
        flag = False
        try:
            getattr(other, "__iter__")
            lst = Linked_List()
            for i in self:
                lst.append(i)
            for i in other:
                lst.append(i)
            return lst
        except:
            flag = True
        if flag:
            raise Exception(f"can not add list and object of type {type(other)}")

    def __iter__(self):
        self.__iterator = self.__head
        return self

    def __next__(self):
        if self.__iterator == None:
            self.__iterator = self.__head
            raise StopIteration
        current_val = self.__iterator.data
        self.__iterator = self.__iterator.next_data
        return current_val

    def __insert_first(self, data):
        x = Node(data)
        if self.__tail == None and self.__head == None:
            self.__tail = x
            self.__head = x
            self.__iterator = x
        else:
            temp = self.__head
            self.__head = x
            self.__head.next_data = temp
            self.__iterator = self.__head
        self.__length += 1

    def __insert(self, index, data, flag):
        if not isinstance(index, int):
            raise TypeError("list indexes must be inetgers")
        
        if index < self.__length:
            if index < 0:
                index = self.__neg_index_chk(index)
            i = 0
            x = self.__head
            if flag == "insert":
                if index == 0:
                    self.__insert_first(data)
                else:
                    node = Node(data)
                    while x:
                        if i == index - 1:
                            node.next_data = x.next_data
                            x.next_data = node
                            self.__length += 1
                            break
                        x = x.next_data
                        i += 1
            elif flag == "setitem":
                while x:
                    if i == index:
                        x.data = data
                        break
                    x = x.next_data
                    i += 1
        else:
            raise IndexError("index Out of range")

    def __neg_index_chk(self, index):
        if index < 0:
            index = abs(index)
            if index <= self.__length:
                index = self.__length - index
            else:
                raise IndexError("list index out of range")
            return index
        return index

    def append(self, data):
        x = Node(data)
        if self.__tail == None and self.__head == None:
            self.__tail = x
            self.__head = x
            self.__iterator = x
        else:
            self.__tail.next_data = x
            self.__tail = x
        self.__length += 1

    def insert(self, index, data):
        self.__insert(index, data, "insert")

    def extend(self, data):
        flag = False
        try:
            getattr(data, "__iter__")
            for i in data:
                self.append(i)
        except:
            flag = True
        if flag:
            raise Exception(f"can not extend list with object of type {type(other)}")

    def copy(self):
        lst = Linked_List()
        for i in self:
            lst.append(i)
        return lst

    def reverse(self):
        lst = Linked_List()
        self.__reverse(self.__head, lst)
        return lst

    def __reverse(self, x, lst):
        while x:
            self.__reverse(x.next_data, lst)
            lst.append(x.data)
            return x

    def remove(self, data):
        x = self.__head
        if self.__head == None and self.__tail == None:
            raise Exception("can not remove items from an empty list")
        elif self.__head == self.__tail and x.data == data:
            self.__head = None
            self.__tail = None
            self.__iterator = None
        elif x.data == data:
            self.__head = x.next_data
        else:
            flag = False
            while x:
                if x.next_data.data == data:
                    x.next_data = x.next_data.next_data
                    flag = True
                    break
                x = x.next_data
            if not flag:
                raise TypeError(f"value {data} not found")
        self.__length -= 1

    def pop(self, index = None):
        if not isinstance(index, int) and None:
            raise TypeError("list indexes must be integers")
        elif isinstance(index, int) and index > self.__length:
            raise IndexError("list index out of range")
        elif self.__head == None and self.__tail == None:
            raise Exception("can not pop items from an empty list")
        elif self.__head == self.__tail:
            data = self.__head.data
            self.__head = None
            self.__tail = None
            self.__iterator = None
            self.__length -= 1
            return data
        else:
            x = self.__head
            if index is None:
                while x:
                    if x.next_data.next_data == None:
                        data = x.next_data.data
                        x.next_data = None
                        self.__tail = x
                        self.__length -= 1
                        return data
                    x = x.next_data
            else:
                index = self.__neg_index_chk(index)
                i = 0
                if index == i:
                    data = self.__head.data
                    self.__head = self.__head.next_data
                    self.__length -= 1
                    return data
                while x:
                    if i == index - 1:
                        data = x.next_data.data
                        x.next_data = x.next_data.next_data
                        self.__length -= 1
                        return data
                    i += 1
                    x = x.next_data

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__iterator = None

    def count(self, data):
        ct = 0
        for i in self:
            if i == data:
                ct += 1
        return ct

    def index(self, data):
        index = 0
        for i in self:
            if i == data:
                return index
            index += 1
        raise TypeError("value not found")

    def sort(self):
        lst = Linked_List()
        for i in sorted(self):
            lst.append(i)
        return lst


if __name__ == "__main__":
    lst = Linked_List(1,99,5,6)
    x = lst + (7,8,48,45)
    print(x)
    print(x[:])
