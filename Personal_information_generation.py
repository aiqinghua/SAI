import random


def generate_random_phone_number():
    # 生成随机的区号（前三位，不包括特殊号码）
    area_code = random.randint(130, 199)  # 130-199是合法区号范围
    # 生成随机的用户号码（后8位）
    user_number = "".join([str(random.randint(0, 9)) for _ in range(8)])
    # 拼接区号和用户号码
    phone_number = f"{area_code}{user_number}"
    return phone_number

# 生成随机的区域码，前6位数字
def generate_region_code():
    while True:
        region_code = "{:06d}".format(random.randint(110000, 820000))
        if not region_code.startswith('7'):
            return region_code

# 生成随机的出生日期，8位数字，格式为YYYYMMDD
def generate_birthday():
    year = random.randint(1950, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # 简化处理，不考虑闰年
    return "{:04d}{:02d}{:02d}".format(year, month, day)

# 生成随机的顺序码，3位数字
def generate_sequence_code():
    return "{:03d}".format(random.randint(1, 999))

# 生成随机的校验位
def generate_check_digit(id17):
    weight_factors = [int(x) for x in "7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2".split()]
    check_code_map = {
        0: "1", 1: "0", 2: "X", 3: "9", 4: "8", 5: "7", 6: "6", 7: "5", 8: "4", 9: "3", 10: "2"
    }
    weighted_sum = sum([int(id17[i]) * weight_factors[i] for i in range(17)])
    check_digit = check_code_map[weighted_sum % 11]
    return check_digit

# 生成随机身份证号
def generate_random_id():
    region_code = generate_region_code()
    birthday = generate_birthday()
    sequence_code = generate_sequence_code()
    id17 = region_code + birthday + sequence_code
    check_digit = generate_check_digit(id17)
    id_number = id17 + check_digit
    return id_number
# if __name__ == '__main__':
#     generate_random_phone_number()
#     generate_random_id()