from pathlib import Path
from dotenv import load_dotenv

# get file directory
# CFG_FILE_PATH = Path(__file__).resolve().parent
REPO_ROOT_DIR = "../"

# load environment variables
ENV_FILE = Path(REPO_ROOT_DIR + ".env")
ENV_TEMPLATE_FILE = Path(REPO_ROOT_DIR + ".env_template")
if not ENV_FILE.exists():
    if ENV_TEMPLATE_FILE.exists():
        ENV_FILE.write_text(ENV_TEMPLATE_FILE.read_text())

DATASETS = {
    # kwargs for datasets.load_dataset(**kwargs)
    # https://huggingface.co/docs/datasets/package_reference/loading_methods#datasets.load_dataset

}
