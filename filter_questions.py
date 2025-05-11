import re

def filter_questions(input_file, single_choice_file, true_false_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    single_choice = []
    true_false = []
    current = []
    for line in lines + ['\n']:
        if re.match(r'^\d+、', line):
            if current:
                qtext = ''.join(current)
                # 判断是否为选择题
                options = re.findall(r'^[A-D]、', qtext, re.M)
                answer = re.search(r'答案：([A-D])', qtext)
                if len(options) == 4 and answer:
                    single_choice.append(qtext.strip() + '\n')
                # 判断是否为判断题
                elif re.search(r'答案：([正确|错误]+)', qtext):
                    tf_answer = re.search(r'答案：([正确|错误]+)', qtext)
                    if tf_answer:
                        true_false.append(qtext.strip() + '\n')
            current = [line]
        else:
            current.append(line)
    # 处理最后一题
    if current:
        qtext = ''.join(current)
        options = re.findall(r'^[A-D]、', qtext, re.M)
        answer = re.search(r'答案：([A-D])', qtext)
        if len(options) == 4 and answer:
            single_choice.append(qtext.strip() + '\n')
        elif re.search(r'答案：([正确|错误]+)', qtext):
            tf_answer = re.search(r'答案：([正确|错误]+)', qtext)
            if tf_answer:
                true_false.append(qtext.strip() + '\n')
    with open(single_choice_file, 'w', encoding='utf-8') as f:
        f.writelines(single_choice)
    with open(true_false_file, 'w', encoding='utf-8') as f:
        f.writelines(true_false)

if __name__ == '__main__':
    filter_questions('新建 文本文档 (2).txt', 'single_choice.txt', 'true_false.txt') 