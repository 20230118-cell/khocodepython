def cong(a, b, c, d):
    # a/b + c/d
    return (a*d + b*c, b*d)

def tru(a, b, c, d):
    # a/b - c/d
    return (a*d - b*c, b*d)

def nhan(a, b, c, d):
    # a/b * c/d
    return (a*c, b*d)

def chia(a, b, c, d):
    # a/b : c/d
    return (a*d, b*c)

def hien_thi(tu, mau):
    return f"{tu}/{mau}"