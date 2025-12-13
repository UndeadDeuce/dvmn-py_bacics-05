import os
import random

import file_operations

from faker import Faker


def make_cards():
    fake = Faker("ru_RU")
    for card_num in range(1, 11):

        name, last_name = fake.first_name_male(), fake.last_name_male()
        city_name = fake.city()
        job = fake.job()

        list_skills = [
            'Стремительный прыжок',
            'Электрический выстрел',
            'Ледяной удар',
            'Стремительный удар',
            'Кислотный взгляд',
            'Тайный побег',
            'Ледяной выстрел',
            'Огненный заряд'
        ]

        letters_mapping = {
            'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
            'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
            'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
            'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
            'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
            'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
            'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
            'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
            'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
            'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
            'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
            'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
            'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
            'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
            'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
            'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
            'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
            'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
            'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
            'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
            'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
            'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
            ' ': ' '
        }

        person_skills = random.sample(list_skills, 3)
        runic_skills = []

        for skill in person_skills:
            runic_word = ""
            for letter in skill:
                runic_word += letters_mapping[letter]
            runic_skills.append(runic_word)

        context = {
            "first_name": name,
            "last_name": last_name,
            "job": job,
            "town": city_name,
            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18),
            "skill_1": runic_skills[0],
            "skill_2": runic_skills[1],
            "skill_3": runic_skills[2]
        }

        cards_path = os.path.join("cards_set", "form_{num}.svg".format(num=card_num))
        card_resources_path = os.path.join("resources", "charsheet.svg")
        os.makedirs("cards_set", exist_ok=True)
        file_operations.render_template(card_resources_path, cards_path, context)


def main():
    make_cards()

if __name__ == '__main__':
    main()
