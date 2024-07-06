from setuptools import setup, find_packages

setup(
    name='adventure_planning',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'prompt_toolkit',
        'peewee',
    ],
    entry_points='''
        [console_scripts]
        ap=ap.entry_points:cli
    ''',
    cmdclass={
    },
    package_data={
        '': ['database/data/ap.db'],
    },
)
