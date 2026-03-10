class SegmentedMemoryManager:
    def __init__(self):
        self.RAM = [None] * 65536
        self.max_segment_size = 4096
        self.segments = {
            0b00: {"name": "Code",  "base": 32768, "bounds": 2048, "grows_positive": 1},
            0b01: {"name": "Heap",  "base": 40960, "bounds": 3072, "grows_positive": 1},
            0b11: {"name": "Stack", "base": 28672, "bounds": 2048, "grows_positive": 0},
        }

    def translate(self, virtual_address):
        segment = virtual_address >> 12
        offset = virtual_address & 0b111111111111

        if segment not in self.segments:
            raise Exception("Invalid segment")

        seg = self.segments[segment]

        if seg["grows_positive"] == 0:
            offset = offset - self.max_segment_size

        if abs(offset) >= seg["bounds"]:
            raise Exception("Out of bounds!")

        return seg["base"] + offset

    def load(self, virtual_address, value):
        self.RAM[self.translate(virtual_address)] = value

    def read(self, virtual_address):
        return self.RAM[self.translate(virtual_address)]


mm = SegmentedMemoryManager()

print("Code physical address:", mm.translate(0b00_000001101100))
print("Heap physical address:", mm.translate(0b01_000010000000))
print("Stack physical address:", mm.translate(0b11_100000010000))

try:
    mm.translate(0b00_111111111111)
except Exception as e:
    print("Error:", e)
