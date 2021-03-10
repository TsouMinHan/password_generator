from pathlib import Path
import json
import random

def read_json(path):
    with open(path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

PASSWORD_JSON_PATH = Path("password.json")

combination_dc = read_json(PASSWORD_JSON_PATH)
input_ls = input("輸入字串（以空白鍵區隔）：").split()

combination_ls = [v for k, v in combination_dc.items()]
combination_ls.append(input_ls)
password = ""

for i in range(len(combination_ls)):
    data_ls = combination_ls[i]

    try:
        idx = random.randint(0, len(data_ls)-1)
        password += data_ls[idx]

    except IndexError as e:
        pass
    except ValueError as e:
        pass
    except Exception as e:
        print(e)

print(f"Password: {password}")