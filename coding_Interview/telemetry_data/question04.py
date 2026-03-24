from collections import defaultdict

'''

[Tag (1–2 bytes)][Length (1 byte)][Value (N bytes)]

"9F02060000000010009F2608A1B2C3D4E5F6A7B8"

{
  "9F02": "000000001000",
  "9F26": "A1B2C3D4E5F6A7B8"
}

"00011111" (2)
"0x1F"     (16)

"9F" -> 10011111

'''

raw_data = "9F02060000000010009F2608A1B2C3D4E5F6A7B8"

expected = {
  "9F02": "000000001000",
  "9F26": "A1B2C3D4E5F6A7B8"
}



def extract_tag(data):

  first_byte = data[0] + data[1]
  print(first_byte)
  a = int(first_byte, 16) & int("1F", 16)
  if (a == int("1F", 16)):

    print("2 bytes tag")
    return (data[:4], 4)
  else:
    print("1 byte tag")
    return (data[:2], 2)

def process_raw_data(data):

  my_map = defaultdict(int)

  index = 0
  data_len = len(data)
  while index < data_len:
    tag, tag_len = extract_tag(data[index:])

    print("tag=" + tag)
    print("tag_len=" + str(tag_len))
    index += tag_len

    len_str = data[index:index+2]
    print(len_str)
    length = int(len_str, 16)
    print(length)

    index += 2


    value = data[index:index+(length*2)]

    my_map[tag] = value

    index += (length*2)

    print("value="+ value)

  return dict(my_map)


result = process_raw_data(raw_data)

print(result)

print(expected == result)