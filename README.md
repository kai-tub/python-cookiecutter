# Opinionated Python Cookiecutter
Primarily for personal use, with the main features:
- GitHub Actions out of the box
- Python packaging with PDM
- Pre-commit hooks to ensure code quality
- `black` & `isort` by default
- `justfile`'s for modern & cross-platform Makefile alternative
- auto for CI/CD
- Modern Sphinx with furo theme and markdown by default
    - Usage of `livereload` to quickly serve docs and live-reload
- Also provided:
    - GitHub Welcome Bot Configuration
    - Code Of Conduct
    - Contributing guidelines


## After install:
- Activate welcome-bot if necessary
- Ensure that "main" branch is actually the `main` branch
- Add the following secrets to GitHub
    - PYPI_USER (pypi.yml)
    - PYPI_PWD (pypi.yml)
    - GH_ACCESS_TOKEN (main.yml)
- Setup `auto shipit` for repository
- Run `just install`
