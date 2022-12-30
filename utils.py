import json


def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_all():
    ms = []
    for i in load_candidates():
        ms.append(i['name'])
    return ms


def get_by_pk(pk):
    for i in load_candidates():
        if i['pk'] == pk:
            return i


def get_by_skill(skill_name):
    result = ''
    for i in load_candidates():
        i['skills'] = i['skills'].lower()
        skill_name = skill_name.lower()
        if skill_name in i['skills']:
            result += f'Имя кандидата - {i["name"]}<br>' \
                      f'Позиция кандидата - {i["position"]}<br>' \
                      f'{i["skills"]}<br>\n'
    return result + '</pre>'


def show_candidates():
    result = '<pre>'
    for i in load_candidates():
        result += f'Имя кандидата - {i["name"]}\n' \
                  f'Позиция кандидата - {i["position"]}\n' \
                  f'{i["skills"]}\n'
    return result + '</pre>'


def show_pictures(x):
    result = '<pre>'
    for i in load_candidates():
        if str(i['pk']) == str(x):
            link = i['picture']
            text = f'<img src="{link}">'
            result += f'{text}\nИмя кандидата - {i["name"]}\n' \
                      f'Позиция кандидата - {i["position"]}\n' \
                      f'{i["skills"]}\n'
            return result + '</pre>'

print(show_pictures('https://picsum.photos/200'))