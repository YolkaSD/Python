def rec():
    global val
    min_ = min(val)
    max_ = max(val)
    for i in range(len(val)):
        if val[i] == max_:
            val[i] = min_


val = [1, 3, 3, 3, 4]
rec()
print(val)
