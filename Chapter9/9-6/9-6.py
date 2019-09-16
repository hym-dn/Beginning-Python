def flatten(nested):
    try:
        # 不迭代类似于字符串的对象
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist): 
                result.append(element)
        except TypeError:
            result.append(nested)
        return result