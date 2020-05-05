import base64


def encode_string(message="", encoding="ascii"):
    return message.encode(encoding)


def decode_string(message=b"", encoding="ascii"):
    return message.decode(encoding)


def encode64_string(message="", encoding="ascii"):
    message_bytes = encode_string(message, encoding)
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode(encoding)


def decode64_string(message="", encoding="ascii"):
    base64_bytes = message.encode(encoding=encoding)
    message_bytes = base64.b64decode(base64_bytes)
    return decode_string(message_bytes, encoding)


def encode64_file(path="", encoding="utf-8", as_bytes=True):
    with open(path, mode="rb") as file:
        data = file.read()
        base64_data = base64.b64encode(data)
    return base64_data.decode(encoding=encoding) if not as_bytes else base64_data


def decode64_file(output_file="", base64_data="", encoding="utf-8", as_bytes=True):
    with open(output_file, mode="wb") as file:
        base64_bytes = base64_data.encode(encoding=encoding) if not as_bytes else base64_data
        decoded_file_data = base64.b64decode(base64_bytes)
        file.write(decoded_file_data)
