len_packet_marker = 4
len_message_marker = 14

with open("data/puzzle_06.txt", "r") as fi:
    line = fi.readline()
    for i in range(0, len(line)):
        packet_marker = line[i: i + len_packet_marker]
        if len(set(packet_marker)) == len_packet_marker:
            print(f"part_1 = {i + len_packet_marker}")
            break

    for i in range(0, len(line)):
        packet_marker = line[i: i + len_message_marker]
        if len(set(packet_marker)) == len_message_marker:
            print(f"part_2 = {i + len_message_marker}")
            break
