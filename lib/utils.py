import json
import logging
import sys
from typing import Dict, Any


logger: logging.Logger = logging.getLogger('RukmanBot')
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


TOKENS_PATH: str = 'tokens.json'
try:
    with open(TOKENS_PATH, 'r') as f:
        TOKENS: Dict[str, Any] = json.load(f)
except Exception as e:
    logger.error(e)
    exit(1)
