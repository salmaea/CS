def clock24_to_metric(s):
    h, m, sec = s.split(':')
    a = round((int(h) * 3600 + int(m) * 60 + int(sec)) * (1.157397964))
    b = a // 10000
    c = a % 10000 // 100
    d = a % 10000 % 100
    return b, c, d
print(clock24_to_metric('12:00:00'))
