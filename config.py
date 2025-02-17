class Config():
    def __init__(self, data):
        ENVS = ['dev', 'qa']

        if data.lower() not in ENVS:
            raise ValueError(f'{data} is not a supported environment (supported envs {ENVS})')

        self.base_url = {
            'dev': 'https://dev.ambitionhire.ai/login',
            'qa': 'https://dev.ambitionhire.ai/login',
            'services':'https://services-recruiter.ambitionhire.ai/login'

        }[data.lower()]
