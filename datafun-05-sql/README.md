# datafun-05-sql

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![marimo](https://img.shields.io/badge/marimo-reactive_notebook-FF6B6B)](https://docs.marimo.io/)
[![SQLite](https://img.shields.io/badge/SQLite-database-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: relational data and SQL analytics with a marimo app
> for parameterized queries (e.g. choose a region to update the chart)

Notebooks combine narration and code.
This project works on **related tabular data files** using SQL and Python.
It includes a reactive marimo app for interacting with the related data.

Note: With marimo, analysts can build interactive web apps!
It's a whole new skill set, and not easy, but it does create
engaging reports that showcase your analytic skills.

## Motivation

We've mostly worked with data stored in files.
Organizations often keep larger collections of related data in databases,
where we can ask for the information we need
instead of loading everything at once.

In this project, we'll use SQL to ask questions of data stored in a database.
We'll select useful records, filter and organize results,
summarize groups, and combine related information
so it can be used in further analysis.

## This Project

This project introduces **relational data and SQL**
used when storing structured data in tables.
Analysts are typically highly skilled at both SQL and Python.

Sample datasets are provided in the `data/raw` folder
across several topic domains:

- **retail** - with regions / stores / employees (the worked example)
- **library** - with state / branch / books
- **health** - with clinic / patient / visit
- **movies** - using the **MovieLens** small dataset

Each domain has related tables.
Run the retail example,
and implement a similar project either by expanding the retail work,
or choosing one of the other recommended domains.

## Produced Artifacts

This project produces the same results in several useful forms.

- [**Reactive App (marimo)**](https://rlorey.github.io/datafun-05-sql/app/)
  - run the analysis interactively in a browser

- [**Reactive Notebook (marimo)**](./src/datafun/notebook.py)
  - view the Python source used to create the reactive app

## Initial Results

![One analyst-selected chart](docs/images/first-chart.png)

![Marimo reactive app preview](docs/images/marimo-local-preview.png)

## Important Folders and Files

- **data/*** - raw CSV input files
- **artifacts/** - generated database files, logs, or reports
- **docs/** - project narrative and documentation
- **src/datafun/** - project logic
- **zensical.toml** - update documentation site metadata



## Success

Running the example script will print out:

```shell
===================================
END main() - Executed successfully!
===================================
```

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

Open a machine terminal in your `Repos` folder,
change directory (cd) into the new folder,
and run `code .` to open only this example project in VS Code:

```shell
git clone https://github.com/rlorey/datafun-05-sql

cd datafun-05-sql
code .
```

### In a VS Code terminal
Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal**
in the root project folder.
Copy each command, paste into your terminal, and hit ENTER,
to run each command one at a time.

```shell
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made by pre-commit tasks
git add -A
uv run pre-commit run --all-files

# run the Python module
uv run python -m datafun.app

# run marimo nb as a reactive app
# press Ctrl + C in the terminal to exit
uv run marimo run src/datafun/notebook.py

# Or: run marimo nb as a notebook
uv run marimo edit src/datafun/notebook.py

# do chores
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
uv run python -m zensical build

# save progress as you work
git add -A
git commit -m "your message here"
# repeat if changes were made (try the UP ARROW)
git add -A
git commit -m "your message here"

git push -u origin main
```

</details>


## As Needed

If VS Code does not automatically use the new `.venv` environment:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Python: Select Interpreter**.
3. Select the interpreter from this project's `.venv` folder.

If VS Code still does not recognize the environment or newly installed tools:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Developer: Reload Window**.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Documentation

- [Documentation](https://rlorey.github.io/datafun-05-sql/)

## Data Card

- [Palmer Penguins Data Card](./docs/data-card.md)

## Annotations

- [.annotations/annotations.md](./.annotations/annotations.md)

## Citation

- [CITATION.cff](./CITATION.cff)

## License

This project is licensed under the [MIT License](./LICENSE).
