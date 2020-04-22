from distutils.core import setup

setup(name='scrapemimula',
    version='1.0',
    description="scrapes my bank info so I don't have to do it and then writes reports for me on googlesheets",
    packages=['scrape', 'scrape.my_banks'],
    scripts=['scripts/wrt'], 
    install_requires=['beautifulsoup4', 'helium', 'requests']
)