from pathlib import Path

STRUCTURE = {
    "app": {
        "__init__.py": "",
        "config.py": "",
        "daily_runner.py": "",
        "runner.py": "",
        "example.env": "",
        "agent": {
            "__init__.py": "",
            "curator_agent.py": "",
            "digest_agent.py": "",
            "email_agent.py": "",
        },
        "database": {
            "__init__.py": "",
            "connection.py": "",
            "create_tables.py": "",
            "models.py": "",
            "repository.py": "",
        },
        "profiles": {
            "__init__.py": "",
            "user_profile.py": "",
        },
        "scrapers": {
            "__init__.py": "",
            "anthropic.py": "",
            "openai.py": "",
            "youtube.py": "",
        },
        "services": {
            "__init__.py": "",
            "email.py": "",
            "process_anthropic.py": "",
            "process_curator.py": "",
            "process_digest.py": "",
            "process_email.py": "",
            "process_youtube.py": "",
        },
    },
    "docker": {
        "docker-compose.yml": "",
    },
    ".gitignore": "",
    ".python-version": "",
    "README.md": "",
    "pyproject.toml": "",
    "main.py": "",
}


def create_structure(base_path: Path, structure: dict):
    for name, content in structure.items():
        path = base_path / name

        if isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)
        else:
            path.touch(exist_ok=True)


if __name__ == "__main__":
    create_structure(Path.cwd(), STRUCTURE)
    print("Project structure created.")