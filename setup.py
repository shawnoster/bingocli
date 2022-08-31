from setuptools import setup

setup(
    name = 'bingocli',
    version = '0.1.0',
    description = ('Command-line interface project skeleton using best practices'),
    author = 'Shawn Oster',
    author_email = 'shawn.oster@gmail.com',
    url = 'https://github.com/shawnoster/nightowlcli',
    license = 'MIT License',
    packages = ['bingocli'],
    entry_points = {
        'console_scripts': [
            'nightowlcli = nightowlcli.__main__:main'
        ]
    })
