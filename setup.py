from setuptools import setup, find_packages

setup(
    name = 'django-mosquare',
    version = __import__('django_mosquare').__version__,
    license = 'BSD',

    install_requires = [
        'Django==1.3',
        'PIL==1.1.7',
        'smartmin==0.0.3',
        'sorl-thumbnail==11.01',
        'django-uniform'
        ],
    dependency_links = [],
    description = "",
    long_description = open('README.org').read(),
    author = 'Nyaruka Ltd.',
    author_email = 'code@nyaruka.com',
    url = 'http://www.nyaruka.com/#open',
    download_url = 'http://github.com/nyaruka/django-mosquare',

    include_package_data = True,
    packages = find_packages(),
    zip_safe = False,
    
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
    )
