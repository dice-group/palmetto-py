def get_next_set_of_documents(byte_buffer):
    doc_ids = []
    length = convert_4_bytes_to_int(byte_buffer.read(4))
    for i in range(0, length):
        doc_id = convert_4_bytes_to_int(byte_buffer.read(4))
        doc_ids.append(doc_id)

    return doc_ids


def convert_4_bytes_to_int(_bytes):
    return int.from_bytes(_bytes, byteorder="big")


from palmettopy.palmetto import Palmetto
palmetto = Palmetto()
words = ["cake", "apple", "banana", "cherry", "chocolate"]
df = palmetto._get_df(words)
from io import BytesIO
_bytes_io = BytesIO(df)
doc_id_lists = []
while True:
    position_before_scan = _bytes_io.tell()
    doc_ids = get_next_set_of_documents(_bytes_io)
    if doc_ids:
        doc_id_lists.append(doc_ids)
    position_after_scan = _bytes_io.tell()
    if position_before_scan == position_after_scan:
        break

# convert to sets
doc_id_sets = []
for _list in doc_id_lists:
    doc_id_sets.append(set(_list))

_fix_set = doc_id_sets[0]
for i in range(1, len(doc_id_sets)):
    _fix_set.intersection_update(doc_id_sets[i])

coherence = len(_fix_set)
print(coherence)
