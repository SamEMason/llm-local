import yaml
from pathlib import Path
from dotenv import load_dotenv
from typing import Any, Dict
import os


def load_config(path: str = "config.yml") -> Dict[str, Any]:
    load_dotenv()

    # create dict to merge .env and config.yml
    combined_config: Dict[str, Any] = {}

    # Load config.yml
    with open(Path(path), "r") as f:
        yaml_config = yaml.safe_load(f)
        combined_config.update(yaml_config)

    # Inject .env values (e.g., ENV=dev)
    # Only add known keys - or dump everything if needed
    if "ENV" in os.environ:
        combined_config["env"] = os.getenv("ENV")
    
    return combined_config