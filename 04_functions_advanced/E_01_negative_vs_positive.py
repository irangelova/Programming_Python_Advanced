def define_number(num_list):
    positive_nums = []
    negative_nums = []
    for el in num_list:
        positive_nums.append(int(el)) if int(el) > 0 else negative_nums.append(int(el))

    sum_positive = sum(positive_nums)
    sum_negative = sum(negative_nums)
    message = "The negatives are stronger than the positives" if abs(sum_negative) > sum_positive else "The positives are stronger than the negatives"

    return sum_positive, sum_negative, message


numbers = input().split()
sum_positive_nums, sum_negative_nums, message_to_print = define_number(numbers)
print(sum_negative_nums)
print(sum_positive_nums)
print(message_to_print)
