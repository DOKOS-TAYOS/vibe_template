# Architecture

## High-Level Shape

This template uses a hybrid research-first structure with a thin CLI and a small Python core.

- `research/`: the only human-verified source of truth for research decisions and conclusions
- `experiments/`: reproducible working area for runs, scripts, configs, and outputs
- `notebooks/`: optional exploratory area for analysis and communication
- `src/`, `scripts/`, `tests/`, `examples/`, and `bin/`: delegable implementation and maintenance area

Inside the Python package, the structure stays intentionally small:

- `domain`: stable concepts and immutable metadata
- `app`: orchestration and use-case services
- `infrastructure`: adapters for filesystem and process execution when needed
- `cli.py`: presentation layer for command-line entrypoints

## Research Boundary

The key design rule is separating checked research from draft work.

- Only files under `research/` count as approved research intent, methodology, or claims.
- AI-generated code, notebooks, summaries, plots, and scaffolding may live outside `research/`.
- Nothing outside `research/` should be treated as a checked conclusion until the researcher promotes it there.

This keeps the critical review surface small and legible for a researcher, while still leaving plenty of room for AI-assisted execution.

## Python Layer Guidance

Not every research project needs a large framework on day one. This template keeps the Python side small and layered:

- model-like concepts live in `domain`
- controller-like orchestration lives in `app`
- user-facing adapters live in CLI, APIs, or future UI layers

This avoids empty scaffolding while keeping the code easy to grow when an experiment turns into reusable software.

## Bootstrap Strategy

The template starts with placeholder metadata and a placeholder package name. Bootstrap:

1. validates user answers
2. rewrites tracked text files
3. renames `src/project_name`
4. writes the chosen project license

The new research files use the same placeholder values already supported by bootstrap, so the research template does not need extra bootstrap prompts.

Relative imports inside the package reduce the amount of fragile rename logic.
