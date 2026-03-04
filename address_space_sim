# address_space_sim.py

class AddressSpace:
    def __init__(self):
        self.memory = [None] * 100
        self.heap_pointer = 0
        self.stack_pointer = 99

    def allocate_heap(self, value):
        if self.heap_pointer > self.stack_pointer:
            raise Exception("Out of memory")

        self.memory[self.heap_pointer] = value
        self.heap_pointer += 1

    def push_stack(self, value):
        if self.stack_pointer < self.heap_pointer:
            raise Exception("Out of memory")

        self.memory[self.stack_pointer] = value
        self.stack_pointer -= 1

    def pop_stack(self):
        if self.stack_pointer == 99:
            raise Exception("Stack is empty")

        self.stack_pointer += 1
        val = self.memory[self.stack_pointer]
        self.memory[self.stack_pointer] = None
        return val


# Demo

p = AddressSpace()

p.allocate_heap("A")
p.allocate_heap("B")
p.allocate_heap("C")

p.push_stack(1)
p.push_stack(2)
p.push_stack(3)

print("Popped:", p.pop_stack())
print("Heap pointer:", p.heap_pointer)
print("Stack pointer:", p.stack_pointer)
print("Memory:", p.memory)


pOver = AddressSpace()

try:
    while True:
        pOver.allocate_heap("H")
        pOver.push_stack("S")
except Exception as e:
    print("Collision detected:", e)

print("Memory:", pOver.memory)


p1 = AddressSpace()
p2 = AddressSpace()

p1.allocate_heap("Process 1")
p2.allocate_heap("Process 2")

print("Process 1 Memory:", p1.memory)
print("Process 2 Memory:", p2.memory)
