import json
import random
from faker import Faker


def generate_fake_data(fake, count=100):
    data = []
    for _ in range(0, count):
        row = {
            'username': fake.user_name(),
            'email': fake.email(),
            'bio': fake.text(max_nb_chars=140, ext_word_list=None),
        }
        data.append(row)
    return data



if __name__ == '__main__':
    fake = Faker()
    data = generate_fake_data(fake, count=200)
    print(json.dumps(data, indent=2))
