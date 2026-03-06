class MemoryManager:
    def __init__(self):
        self.RAM = [None] * 256
        self.BOUNDS = 64
        self.free_list = [0,1,2,3]

    def load_process(self, name):
        if not self.free_list:
            raise Exception("No free slots")

        slot = self.free_list.pop(0)
        base = slot * self.BOUNDS

        self.RAM[base] = name
        return base

    def unload_process(self, base):
        for i in range(base, base + self.BOUNDS):
            self.RAM[i] = None

        slot = base // self.BOUNDS
        self.free_list.append(slot)

    def translate(self, base, vaddr):
        if vaddr < 0 or vaddr >= self.BOUNDS:
            raise Exception("Address out of bounds")

        phys = base + vaddr
        return phys


mm = MemoryManager()

base1 = mm.load_process("Process A")
base2 = mm.load_process("Process B")
base3 = mm.load_process("Process C")

print("Free list after loading 3 processes:", mm.free_list)

print("Process B virtual 0 ->", mm.translate(base2,0), "physical")
print("Process B virtual 10 ->", mm.translate(base2,10), "physical")

try:
    mm.translate(base1,64)
except Exception as e:
    print("Translation error:", e)

mm.unload_process(base1)
print("Free list after unloading Process A:", mm.free_list)

try:
    mm.load_process("Process D")
    mm.load_process("Process E")
    mm.load_process("Process F")
except Exception as e:
    print("Load error:", e)


mm2 = MemoryManager()

baseX = mm2.load_process("Process X")
baseY = mm2.load_process("Process Y")

print("Process X: virtual 5 ->", mm2.translate(baseX,5), "physical")
print("Process Y: virtual 5 ->", mm2.translate(baseY,5), "physical")
print("Same virtual address, different physical — this is process isolation!")
