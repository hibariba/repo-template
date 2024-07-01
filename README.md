# Repo Template

## repo structure

```
project-name/
│
├── nbs/                    # Jupyter notebooks for experiments
│   ├── 1.01-eda.ipynb
|   ├── 2.01-baseline.ipynb
│   └── 3.01-eval.ipynb
│
├── src/                    # Python source code for the nbs
│   ├── __init__.py
│   ├── cfg.py
│   ├── make_dataset.py     # Code to download or generate data.
│   └── utils.py            # Utility functions
│
├── data/                   # Data files (if needed)
│   ├── external            # Data from third party sources.
│   ├── interim             # Intermediate data that has been transformed.
│   ├── processed           # The final, canonical data sets for modeling.
│   └── raw                 # The original, immutable data dump.
│
├── docs/                   # Documentation in Markdown
│   └── README.md           # Project overview and instructions
│
├── refs/                   # Data dictionaries, manuals, papers, other materials 
├── .nosync/                # folder for venv and cache, not synced by iCloud Drive
├── .gitignore              # Specify files to ignore in version control
├── .env_template           # list of variables expected in .env
├── project.toml            # project info
├── requirements.txt        # dependencies
└── README.md               # Repository overview
```

## development

1. create venv
    ```
    python3 -m venv .nosync/venv
    source .nosync/venv/bin/activate
    ```
2. Install pip-tools if you haven't already:
    ```
    pip install pip-tools
    ```
3. Add dependencies to `project.toml`:
    ```toml
    ...
    dependencies = [
        "package1",
        "package2",
    ]
    ```
4. Use pip-compile to generate a requirements.txt file:
    ```
    pip-compile pyproject.toml
    ```
5. To install your local project in editable mode along with its dependencies, use:
    ```
    pip install -e . -r requirements.txt
    ```

    - Alternatively, you can use pip-sync to install the exact versions specified in requirements.txt:
        ```
        pip-sync requirements.txt
        ```
    - 