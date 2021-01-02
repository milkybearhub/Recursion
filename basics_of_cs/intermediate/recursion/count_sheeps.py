def sheeps(count):
    if count <= 1: return str(count) + " sheep ~ "
    return sheeps(count - 1) + str(count) + " sheep ~ "
