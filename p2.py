import re

dart_result = input("dartResult: ")
re_shot = re.compile(r"\d{1,2}[SDT][\*#]{0,1}")
shots = re_shot.findall(dart_result)

re_score = re.compile(r"\d{1,2}")
re_zone = re.compile(r"[SDT]")
re_option = re.compile(r"[\*#]{1}")

prev_score = 0
whole_score = 0

for shot in shots:
    score = int(re_score.search(shot).group())
    zone = int(re_zone.search(shot).group().replace('S', '1').replace('D', '2').replace('T', '3'))
    option = re_option.search(shot)
    cur_score = score**zone
    if option == None:
        whole_score += cur_score
        prev_score = cur_score
    elif option.group() == '*':
        whole_score += cur_score*2+prev_score
        prev_score = (cur_score)*2
    elif option.group() == '#':
        whole_score += (cur_score)*-1
        prev_score = (cur_score)*-1

print(whole_score)
