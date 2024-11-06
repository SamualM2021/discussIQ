from setuptools import setup, find_packages

setup(
    name='discussIQ',
    version='0.1',
    description='A real-time chat system integrated with a data analysis dashboard, allowing users to upload, analyze, and share datasets in a collaborative environment. Offering both open-source and commercial license options for flexible usage.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Samual Martelli',
    author_email='smartelli@zoho.com',
    url='https://github.com/SamualM2021/discussIQ',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fastapi',
        'flask',
        'uvicorn',
        'gunicorn',  # For production deployments
        # Add other dependencies here
    ],
    extras_require={
        'dev': [
            'pytest',
            'black',
            'flake8',
            # Development tools
        ]
    },
    entry_points={
        'console_scripts': [
            'start-fastapi=fastapi_app.main:main',  # Replace with your entry point
            'start-flask=flask_app.main:main',      # Replace with your entry point
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: OpenPro License', # This will be a free-form entry
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
