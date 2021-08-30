class Byte:


    def __init__(self, input_data, bit_count = None):

        if bit_count is False:
            raise TypeError("Cannot inherit 'bit_count' from prior state since Byte object was not previously instantiated.")

        if input_data is None:
            raise TypeError("Cannot inherit 'input_data' from prior state since Byte object was not previously instantiated.")

        self.update(input_data, bit_count)


    def update(self, input_data = None, updated_bit_count = False):

        if input_data is None:
            input_data = self.raw_data

        if isinstance(input_data, str):
            try:
                self.raw_data = int(input_data, 0)
            except ValueError:
                raise ValueError("Could not convert string '" + input_data + "' to integer. Please enter integer (i.e. '8') or datatype literal which can implicitly be converted to integer (i.e. '0b1000').")
        elif isinstance(input_data, int):
            self.raw_data = input_data
        else:
            raise TypeError("Expected input of type 'str' or 'int', not '" + type(input_data).__name__ + "'.")
        
        if self.raw_data < 0:
            raise ValueError("Input integer must be unsigned (non-negative).")

            
        self.significant_bits = bin(self.raw_data)[2:]

        if updated_bit_count is None:
            self.bit_len = len(self.significant_bits)
        elif updated_bit_count is False:
            pass
        elif isinstance(updated_bit_count, int):
            self.bit_len = updated_bit_count
        else:
            raise TypeError("'bit_count' must be integer, NoneType, or 'False'.")

        self.leading_zeros = self.bit_len - (len(self.significant_bits))

        if self.leading_zeros < 0:
            needed_bits = -self.leading_zeros
            raise ValueError("Not enough bits (" + str(self.bit_len) + ") to hold value '" + str(self.raw_data) + "', minimum of " + str(self.bit_len + needed_bits) + " bits required.")
        
        self.bin_data = ("0" * self.leading_zeros) + self.significant_bits
        self.bin_data_prefixed = "0b" + self.bin_data

    def __repr__(self):
        return self.bin_data_prefixed
    
    def __len__(self):
        return self.bit_len
    
    def __int__(self):
        return self.raw_data
    
    def __index__(self):
        return self.raw_data

    def __iter__(self):
        return (int(byte) for byte in self.bin_data)

    def __reversed__(self):
        return (int(byte) for byte in reversed(self.bin_data))
        
    def __getitem__(self, key):
        if isinstance(key, int):
            return int(self.bin_data[key])
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self.bin_data))
            binary_slice = ""
            for i in range(start, stop, step):
                binary_slice += self.bin_data[i]
            return Byte("0b" + binary_slice, len(binary_slice))
    
    def __add__(self, operand):
        return Byte(self.raw_data + operand, self.bit_len)
    
    def __sub__(self, operand):
        return Byte(self.raw_data - operand, self.bit_len)
    
    def __mul__(self, operand):
        return Byte(self.raw_data * operand, self.bit_len)
    
    def bit_shift(self, amount, direction):
        shifted_bits = ""
        preserved_bits= ""
        if direction.lower() == "r":
            preserved_bits = self.bin_data[:-amount]
            shifted_bits = ("0" * amount) + preserved_bits
        elif direction.lower() == "l":
            preserved_bits = self.bin_data[amount:]
            shifted_bits = preserved_bits + ("0" * amount)
        return Byte("0b" + shifted_bits, self.bit_len)

    def __lshift__(self, shift_amount):
        return self.bit_shift(shift_amount, "l")

    def __rshift__(self, shift_amount):
        return self.bit_shift(shift_amount, "r")

    def to_bytearray(self, byte_length = 8):
        bit_list = [bit for bit in self.bin_data]
        bytearray_list = []
        while len(bit_list) > 0:
            current_byte = []
            for _ in range(min([len(bit_list), byte_length])):
                current_byte.insert(0, bit_list.pop())
            bytearray_list.insert(0, int("".join(current_byte), 2))
        return bytearray(bytearray_list)
        