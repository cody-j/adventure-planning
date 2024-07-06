from setuptools import setup, find_packages

setup(
    name='adventure_planning',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'prompt_toolkit',
    ],
    entry_points='''
        [console_scripts]
        ap=adventure_planning.entry_points:cli
    ''',
    package_data={
        '': ['ap.db'],
    },
)
