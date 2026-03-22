class PagingMemoryManager:
    def __init__(self):
        self.RAM = [None] * 256
        self.virtual_address_space = 64
        self.page_size = 16
        self.tlb = {}

        self.page_table = {
            0: 3,
            1: 7,
            2: 5,
            3: 2,
        }

    def translate(self, virtual_address):
        if virtual_address < 0 or virtual_address >= self.virtual_address_space:
            raise Exception("Invalid virtual address!")

        offset_bits = self.page_size.bit_length() - 1
        offset = virtual_address & (self.page_size - 1)
        page_num = virtual_address >> offset_bits

        if page_num in self.tlb:
            frame_num = self.tlb[page_num]
        else:
            if page_num not in self.page_table:
                raise Exception("Page fault!")

            frame_num = self.page_table[page_num]
            self.tlb[page_num] = frame_num

        physical_address = (frame_num << offset_bits) | offset
        return physical_address

    def load(self, virtual_address, value):
        physical_address = self.translate(virtual_address)
        self.RAM[physical_address] = value

    def read(self, virtual_address):
        physical_address = self.translate(virtual_address)
        return self.RAM[physical_address]
