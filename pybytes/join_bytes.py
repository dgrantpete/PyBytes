from .byte import Byte

def join_bytes(bytes_list, new_byte_length = None):

    joined_bytes = "0b"
    

    if not isinstance(bytes_list, list):
        raise TypeError("'bytes_list' must be of type 'list', not '" + type(bytes_list).__name__ + "'.")
    
    if len(bytes_list) <= 0:
        raise IndexError("'bytes_list' cannot be empty.")

    for byte in bytes_list:
        if not isinstance(byte, Byte):
            raise TypeError("Items in list must all be of type 'Byte'.")
        else:
            joined_bytes += byte.bin_data
      
    if new_byte_length is None:
        total_bits = 0
        for byte in bytes_list:
            total_bits += len(byte)
    else:
        total_bits = new_byte_length

    return Byte(joined_bytes, total_bits)
