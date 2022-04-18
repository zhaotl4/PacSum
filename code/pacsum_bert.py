def bert_summary():
    ans = ""
    file_path = '/home/ztl/nlp/PacSum/code/PacSum_bert.txt'
    with open(file_path,'r') as f:
        lines=f.readlines()
        for line in lines:
            ans += line
    return ans