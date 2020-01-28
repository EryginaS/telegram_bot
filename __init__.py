import logging
import logging.config as logging_config
import os
import yaml

config_path = ''

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(module)s %(message)s')
print(config_path)

if os.path.exists(config_path):
    with open(config_path) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        if 'logging' in config:
            logging_config.dictConfig((config['logging']))
        logging.info('Файл конфигурации был загружен из файла "%s"', config_path)
else:
    logging.error('Файл конфигурации не найден.')