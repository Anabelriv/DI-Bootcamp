# # Represents a citizen of the city, it has the following attributes: id_number (str), name (str), age (int), priority (bool) and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.

# # This class has no methods.


# class Human:
#     def __init__(self, id_number, name, age, priority, blood_type):
#         self.id_number = str(id_number)
#         self.name = str(name)
#         self.age = int(age)
#         self.priority = bool(priority)
#         self.blood_type = blood_type


# # Represents a queue of humans waiting for their vaccine.
# # It has the following attribute : humans, the list containing the humans that are waiting. It is initialized empty.

# # This class is useful to manage who will get vaccinated in priority. It has the following methods:

# # add_person(self, person) : Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the list (at index 0) before every other.

# # find_in_queue(self, person) : Returns the index of a human in the queue.

# # swap(self, person1, person2): Swaps person1 with person2.

# # get_next(self) : Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.

# # get_next_blood_type(self, blood_type) : Returns the first human with this specific blood type.

# # sort_by_age(self) : Sorts the queue
# # first the priority people
# # then, the older people
# # then the younger people
# # Every human returned by get_next and get_next_blood_type is removed from the list.
# # Those functions return None if the list is empty (ie. no one in the list).

# # Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.


# class Queue:
#     humans = []

#     def add_person(self, person):
#         if self.age in Human > 60 or Human.priority:
#             Queue.humans.insert(0, person)
#         else:
#             Queue.humans.append(person)

#     def find_in_queue(self, person):
#         for index, p in enumerate(Queue.humans):
#             if p.id_number == person.id_number:
#                 return index
#         return None

#     def swap(self, person1, person2):
#         self.humans[person1], self.humans[person2] = (
#             self.humans[person2],
#             self.humans[person1],
#         )

#         return self.humans

#     def get_next(self):
#         if Queue.humans:
#             return self.humans.pop(0)
#         return None

#     # def get_next(self):
#     #     humans_index = Queue.humans.index[0]
#     #     next_human = Queue.humans[humans_index + 1]

#     #     return next_human()

#     def get_next_blood_type(self, blood_type):
#         blood_type = Human.blood_type()

#         return (self.humans[0], blood_type)

#     def sort_by_age(self):
#         sorted_list = []
#         for human in self.humans:
#             if Human.priority == True:
#                 sorted_list += human
#             elif Human.age >= 60:
#                 sorted_list += human
#             elif Human.age < 60:
#                 sorted_list += human
#             else:
#                 sorted_list += human
#         return sorted_list


# if __name__ == "__main__":
#     h1 = Human("ID001", "John", 30, False, "A")
#     h2 = Human("ID002", "Alice", 65, True, "B")
#     h3 = Human("ID003", "Bob", 70, False, "O")
#     h4 = Human("ID004", "Eva", 25, False, "AB")


# print("Initial Queue:", [person.name for person in Queue.humans])

# next_person = Queue.get_next("John")
# print("Next Person to be Vaccinated:", next_person.name)
# print("Updated Queue after Vaccination:", [person.name for person in Queue.humans])

# Queue.sort_by_age()
# print("Queue Sorted by Age:", [person.name for person in Queue.humans])

# Queue.rearrange_queue()
# print("Queue after Rearrangement:", [person.name for person in Queue.humans])


# ----------------------- Fixed ---------------------


class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
            person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.priority or person.age > 60:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        for index, p in enumerate(self.humans):
            if p.id_number == person.id_number:
                return index
        return None

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        if index1 is not None and index2 is not None:
            self.humans[index1], self.humans[index2] = (
                self.humans[index2],
                self.humans[index1],
            )

    def get_next(self):
        if self.humans:
            return self.humans.pop(0)
        return None

    def get_next_blood_type(self, blood_type):
        for index, person in enumerate(self.humans):
            if person.blood_type == blood_type:
                return self.humans.pop(index)
        return None

    def sort_by_age(self):
        def sort_key(person):
            return (not person.priority, person.age)

        self.humans.sort(key=sort_key)

    def rearrange_queue(self):
        for i in range(len(self.humans) - 1):
            if (
                self.humans[i].family
                and self.humans[i + 1].family
                and self.humans[i].family == self.humans[i + 1].family
            ):
                self.swap(self.humans[i], self.humans[i + 1])


# Test
if __name__ == "__main__":
    h1 = Human("ID001", "John", 30, False, "A")
    h2 = Human("ID002", "Alice", 65, True, "B")
    h3 = Human("ID003", "Bob", 70, False, "O")
    h4 = Human("ID004", "Eva", 25, False, "AB")

    queue = Queue()
    queue.add_person(h1)
    queue.add_person(h2)
    queue.add_person(h3)
    queue.add_person(h4)

    print("Initial Queue:", [person.name for person in queue.humans])

    next_person = queue.get_next()
    print("Next Person to be Vaccinated:", next_person.name)
    print("Updated Queue after Vaccination:", [person.name for person in queue.humans])

    queue.sort_by_age()
    print("Queue Sorted by Age:", [person.name for person in queue.humans])

    queue.rearrange_queue()
    print("Queue after Rearrangement:", [person.name for person in queue.humans])

    h1.add_family_member(h2)
    h1.add_family_member(h3)

    print(h1.name, "Family Members:", [person.name for person in h1.family])
    print(h2.name, "Family Members:", [person.name for person in h2.family])
    print(h3.name, "Family Members:", [person.name for person in h3.family])
    print(h4.name, "Family Members:", [person.name for person in h4.family])
