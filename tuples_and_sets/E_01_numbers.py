first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input()
    if command.startswith("Add"):
        numbers_to_add_str = command[10:]
        numbers_to_add_list = numbers_to_add_str.split()
        for index in range(len(numbers_to_add_list)):
            to_sequence = command[4:10]
            if "First" in to_sequence:
                first_sequence.add(int(numbers_to_add_list[index]))
            else:
                second_sequence.add(int(numbers_to_add_list[index]))
    elif command.startswith("Remove"):
        numbers_to_remove_str = command[13:]
        numbers_to_remove_list = numbers_to_remove_str.split()
        for index in range(len(numbers_to_remove_list)):
            to_sequence = command[7:13]
            if "First" in to_sequence:
                if int(numbers_to_remove_list[index]) in first_sequence:
                    first_sequence.remove(int(numbers_to_remove_list[index]))
            else:
                if int(numbers_to_remove_list[index]) in second_sequence:
                    second_sequence.remove(int(numbers_to_remove_list[index]))
    elif command == "Check Subset":
        if first_sequence < second_sequence or second_sequence < first_sequence:
            print("True")
        else:
            print("False")

first_sequence_sorted = sorted(first_sequence)
second_sequence_sorted = sorted(second_sequence)
for index1 in range(len(first_sequence_sorted)):
    if index1 != (len(first_sequence_sorted) - 1):
        print(first_sequence_sorted[index1], end=", ")
    else:
        print(first_sequence_sorted[index1])
for index2 in range(len(second_sequence_sorted)):
    if index2 != (len(second_sequence_sorted) - 1):
        print(second_sequence_sorted[index2], end=", ")
    else:
        print(second_sequence_sorted[index2])
