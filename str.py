import numpy
def print_string(str ,height_number ,width_number):
    """_summary_
    1つ目の数値で縦、２つ目の数値で横に繰り返す文字列を返却する関数
    Args:
        str (_type_): ５文字以上１０文字以下の文字列
        height_number (_type_): 縦に繰り返す数を決める数値
        width_number (_type_): 横に繰り返す数を決める数値

    Returns:
        _type_: _description_
    """
    height_number = int(height_number)
    width_number = int(width_number)
    for i in range(height_number):
        for i in range(width_number):
            return str

if __name__ == "__main__":
    print_string('abc', numpy.random.randint(0,10), numpy.random.randint(0,10))