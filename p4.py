import re

def main():
    n = int(input('n(0 < n <= 10): '))
    assert (n > 0 & n <= 10), 'out of boundary'
    t = int(input('t(0 < t <= 60): '))
    assert (t > 0 & t <= 60), 'out of boudary'
    m = int(input('m(0 < m <= 45): '))
    assert (m > 0 & m <= 60), 'out of boudary'
    timetable = input('timetable: ').strip()
    assert (timetable[0] == '[' & timetable[-1] == ']'), 'invalid input format'
    re_time = re.compile(r'[0-2]\d:[0-5]\d')
    timetable = re_time.findall(timetable)

if __name__ == '__main__':
    main()