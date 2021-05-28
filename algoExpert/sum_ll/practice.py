


class Link:   
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
k = Link(3)


def store_digits(num):
    new_list = Link(num % 10)
    num //= 10

    while num > 0:
      
        last_digit = num % 10 
        new_list.value, new_list.next = last_digit, Link(new_list.value, new_list.next)
        num //= 10
    
    return new_list

# k = store_digits(123)
# print(k)

# while k is not None:
#     print(k.value)
#     k = k.next 


#   num = num // 10
#    while num > 0:
#        all_but_last, last = num // 10, num % 10
#        store.first, store.rest =  last, Link(store.first, store.rest)
#        num = all_but_last
#    return store
num = 2219
list_nums = [int(d) for d in str(num)]
print(list_nums)
