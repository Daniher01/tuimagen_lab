import os

for key, value in os.environ.items():
    if 'DATABASE' in key or 'SECRET_KEY' in key or 'DEBUG' in key:
        print(f'{key}: {value}')
