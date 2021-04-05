import yaml

with open("./animals.yaml",encoding='utf-8') as f:
    str1=yaml.safe_load(f)
    print(str1)
    f.close()