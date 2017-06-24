import random
import json
import random
from faker import Faker


def generate_fake_data(fake, authors):
    tags = fake.words(nb=20)
    data = []
    for author in authors:
        for _ in range(0, random.randrange(0, 3)):
            row = {
                'title': fake.text(max_nb_chars=64, ext_word_list=None),
                'content': fake.text(max_nb_chars=1000, ext_word_list=None),
                'created_at': fake.date(pattern="%Y-%m-%d"),
                'author': author['username'],
                'tags': fake.words(nb=random.randrange(1, len(tags) // 2), ext_word_list=tags)
            }
            data.append(row)
    return data


if __name__ == '__main__':
    fake = Faker()
    with open('old_authors.json', 'r') as old_authors_json_file:
        authors = json.loads(old_authors_json_file.read())
    data = generate_fake_data(fake, authors)
    print(json.dumps(data, indent=2))
