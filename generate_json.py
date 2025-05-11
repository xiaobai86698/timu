import re
import json

# 单选题转换
def convert_single_choice(txt_path, json_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
    out = []
    i = 0
    while i < len(lines):
        l = lines[i].strip()
        if re.match(r'^\d+、', l):
            q = l[l.find('、')+1:]
            opts = [lines[i+1].strip()[2:], lines[i+2].strip()[2:], lines[i+3].strip()[2:], lines[i+4].strip()[2:]]
            ans = ord(lines[i+5].strip()[-1]) - 65
            out.append({'question': q, 'options': opts, 'answer': ans, 'type': 'single'})
            i += 6
        else:
            i += 1
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

# 判断题转换
def convert_true_false(txt_path, json_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
    out = []
    i = 0
    while i < len(lines):
        l = lines[i].strip()
        if re.match(r'^\d+、', l):
            q = l[l.find('、')+1:]
            ans = 1 if '正确' in lines[i+1] else 0
            out.append({'question': q, 'answer': ans, 'type': 'truefalse'})
            i += 2
        else:
            i += 1
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    convert_single_choice('single_choice.txt', 'single_choice.json')
    convert_true_false('true_false.txt', 'true_false.json') 