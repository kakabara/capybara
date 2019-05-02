from setuptools import find_packages, setup

setup(
    name='capybara',
    version='0.12',
    description='Capybara validation attributes',
    author='Vlasov Sergei',
    author_email='sergei_vlasov@icloud.com',
    url='https://github.com/kakabara/capybara',
    packages=find_packages(),
    install_requires=[
        'ipaddress==1.0.22',
        'jsonschema==2.6.0'
    ]
)
