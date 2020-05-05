import lzma
import zlib
from Base64.file_handler import write_to_bin


def compress_xz(file_path="", data=b""):
    with lzma.LZMAFile(file_path, mode="wb") as file:
        file.write(data)


def decompress_xz(compressed_file_path="", uncompressed_file_path=""):
    with open(compressed_file_path, mode="rb") as compressed_file:
        data = compressed_file.read()
        decompressed_data = lzma.decompress(data)
        write_to_bin(uncompressed_file_path, decompressed_data)


def compress_string(string=b"", level=-1):
    return zlib.compress(string, level=level)


def decompress_string(string=b""):
    return zlib.decompress(string)
