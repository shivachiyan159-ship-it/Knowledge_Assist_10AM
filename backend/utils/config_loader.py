import os
import yaml

from dotenv import load_dotenv
from pathlib import Path
from backend.logger import GLOBAL_LOGGER as log

load_dotenv()


def __project_root():
    rootpath = Path(__file__).resolve().parents[2]
    return rootpath


def load_config(config_path: str = None):
    env_path = os.getenv("config_path")

    if config_path is None:
        config_path = env_path

    path = Path(config_path)  # "backend/config/config.yaml"

    if not path.is_absolute():
        path = __project_root()/path

    log.info("i am callong from custom logger")

    if not path.exists():
        raise FileNotFoundError("config.yaml file not found")

    with open(path) as f:
        return yaml.safe_load(f) or {}


res = load_config()
print(res)
