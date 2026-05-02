# Architecture

## High-Level Shape

This template is course-first. The learning content lives in `course/`, while the Python package and CLI support bootstrap, verification, and light automation.

- `course/`: source of truth for the educator-written learning path
- `domain`: stable concepts and immutable metadata
- `app`: orchestration and use-case services
- `infrastructure`: adapters for filesystem and process execution when needed
- `cli.py`: presentation layer for command-line entrypoints

## Content Flow

The intended flow is deliberately simple:

1. An educator edits `course/README.md` and the numbered modules.
2. Learners consume those Markdown files in order, without needing custom tooling.
3. The Python layer stays available when the course needs bootstrap, testing, cleanup, or future automation.

This keeps the editable surface small while preserving room for code-backed helpers later.

## Bootstrap Strategy

The template starts with placeholder metadata and a placeholder package name. Bootstrap:

1. validates user answers
2. rewrites tracked text files
3. renames `src/project_name`
4. writes the chosen project license

Because `course/` is plain Markdown, educators can keep working there even if they never touch the Python internals.
