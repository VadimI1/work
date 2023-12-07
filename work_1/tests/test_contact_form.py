import main
import pytest


@pytest.mark.parametrize(
    'Websites, Popularity, Front_end, Back_end, Database, Notes',
    [
        ('Google', 2800000000, 'JavaScript,TypeScript', 'C,C++,Go,[3]Java,Python,Node', 'Bigtable,[4]MariaDB[5]', 'The most used search engine in the world.'),

        ('Facebook', 1120000000, 'JavaScript,TypeScript', 'C,C++,Go,[3]Java,Python,Node', 'Bigtable,[4]MariaDB[5]', 'The most used search engine in the world.')
    ]
)

def test_valid_popularity(Websites, Popularity, Front_end, Back_end, Database, Notes):
    #form = {'Websites': 'Google', 'Popularity': 2800000000, 'Front-end': 'JavaScript,TypeScript', 'Back-end': 'C,C++,Go,[3]Java,Python,Node', 'Database': 'Bigtable,[4]MariaDB[5]', 'Notes': 'The most used search engine in the world.'}

    for item in main.p:
        if Websites == item["Websites"]:
            assert Popularity >= item["Popularity"], f"{item['Websites']} (Frontend: {item['Front-end']}|Backend: {item['Back-end']}) has {Popularity} " \
                                                     f"unique visitorsper month. (Expected more than {item['Popularity']})"


