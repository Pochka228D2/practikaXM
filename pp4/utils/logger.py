import logging
import os


def setup_logger():
    """Простая настройка логирования"""
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        handlers=[
            logging.FileHandler('logs/test.log', encoding='utf-8'),
            logging.StreamHandler()
        ],
        force=True
    )
    return logging.getLogger('test_logger')