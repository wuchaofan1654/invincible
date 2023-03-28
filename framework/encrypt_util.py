# 加密
def encrypt(src_str, password='1938762450'):
    # 将字符串转换成字节数组
    data = bytearray(src_str.encode('utf-8'))
    # 把每个字节转换成数字字符串
    str_list = [str(byte) for byte in data]
    # 给每个数字字符串前面加一个长度位
    str_list = [str(len(s)) + s for s in str_list]
    # 进行数字替换
    for index0 in range(len(str_list)):
        temp_str = ""
        for index in range(len(str_list[index0])):
            temp_str += password[int(str_list[index0][index])]
        str_list[index0] = temp_str
    return "".join(str_list)


# 解密
def decrypt(src_str, password='1938762450'):
    # 数字替换还原
    temp_str = ""
    for index in range(len(src_str)):
        temp_str += str(password.find(src_str[index]))
    # 去掉长度位，还原成字典
    index = 0
    str_list = []
    while True:
        # 取长度位
        length = int(temp_str[index])
        # 取数字字符串
        s = temp_str[index + 1:index + 1 + length]
        # 加入到列表中
        str_list.append(s)
        # 增加偏移量
        index += 1 + length
        # 退出条件
        if index >= len(temp_str):
            break
    data = bytearray(len(str_list))
    for i in range(len(data)):
        data[i] = int(str_list[i])
    return data.decode('utf-8')
