"""Encrypt/decrypt given file by using the given key."""

class Cipher:
    """A class that consists of required methods to perform encryption/decryption using XOR."""

    @staticmethod
    def cipher(input_fp: str, output_fp: str, key: bytes, block_size: int = 8192) -> None:
        """Encrypt/decrypt the given file using the given key and XOR function,
           and write the results to the output path.

        :param input_fp: Path of the input file to be encrypted/decrypted
        :type input_fp: str
        :param output_fp: Path of the file to be created as the result of the encryption/decryption
        :type output_fp: str
        :param key: Encryption key
        :type key: bytes
        :param block_size: The input file is to be read and encrypted/decrypted in blocks
                           of size <block_size>, defaults to 8192
        :type block_size: int, optional
        """
        with open(input_fp, "rb") as file_in, open(output_fp, "wb") as file_out:
            while True:
                block = file_in.read(block_size)

                if not block:
                    break
                file_out.write(Cipher._cipher_data(block, key))

    @staticmethod
    def _cipher_data(inp: bytes, key: bytes) -> bytes:
        """Encrypt/decrypt the given input using the given key.

        :param inp: Input bytestring to be encrypted/decrypted
        :type inp: bytes
        :param key: Key of the encryption/decryption
        :type key: bytes
        :return: Result of the encryption/decryption
        :rtype: bytes
        """
        result = b""
        counter = 0
        key_length = len(key)
        input_length = len(inp)
        while key_length <= input_length - counter:
            result += Cipher.xor(inp[counter:counter+key_length], key)
            counter += key_length

        result += Cipher.xor(inp[counter:], key[:input_length - counter])
        return result

    @staticmethod
    def xor(inp: bytes, key: bytes) -> bytes:
        """Compute and return inp XOR key.

        :param inp, key: Operands of the XOR operation
        :type inp, key: bytes
        :return: inp XOR key
        :rtype: bytes
        """
        assert len(inp) == len(key)
        result = b""
        for i in range(len(inp)):
            result += bytes([inp[i] ^ key[i]])
        return result
