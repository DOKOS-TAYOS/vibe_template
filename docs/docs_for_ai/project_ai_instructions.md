# Project AI Instructions

## Mission

Use this template to build computational research projects with a stable Python core, explicit typing, reproducible experiments, and a clear boundary between human-verified research and AI-delegable work.

## Required Workflow

1. Read `docs/docs_for_ai/status.md` before making changes.
2. Read `research/question.md` and `research/protocol.md` before making changes that affect the research workflow or conclusions.
3. Bootstrap a fresh template copy before long-term development.
4. Treat `research/` as the only verified research area.
5. Add or update tests before changing behavior.
6. Run the security audit after dependency, workflow, or release-facing changes.
7. Update `CHANGELOG.md` for meaningful changes.
8. Update these AI docs when workflow, architecture, or constraints change.

## Non-Negotiable Rules

- Always include typing in function definitions.
- Keep the public API as small as possible.
- Only files under `research/` count as verified research decisions or conclusions.
- AI may draft code, notebooks, analyses, plots, summaries, and experiment scaffolding outside `research/`.
- Do not present anything outside `research/` as a checked conclusion until the researcher promotes it there.
- Treat notebooks as exploratory support, not as the authoritative source for final claims.
- Keep experiments reproducible and easy to rerun.
- Use TDD for behavior changes.
- Update `CHANGELOG.md` when adding, fixing, or changing something meaningful.
- Do not remove `.venv` or clean it as part of project cleanup.
- Prefer Windows-safe commands, but keep Linux support where practical.
- Prefer the stable wrappers in `bin/` while the template package name is still provisional.
- Treat `bootstrap` as a one-time setup command. If it already ran, do not try to re-run it.
- Treat `docs/api.md` and the example scripts as contract documentation.
- Keep Dependabot, dependency review, `pip-audit`, CodeQL default setup guidance, and secret-scanning guidance intact unless the derived project has a stronger security baseline.

## Completion Checklist

Before claiming a Python task is complete:

1. Run `ruff check . --fix`
2. Run `ruff format .`
3. Run `pytest`
4. Run `pyright`
5. Run `python scripts/run_template_command.py security` when dependencies or GitHub workflows changed
6. Update `docs/docs_for_ai/status.md`
7. Update `CHANGELOG.md`
8. If a new conclusion emerged, leave it clearly outside the verified boundary until the researcher confirms it in `research/claims.md`

## AI Handoff Checklist

- current status updated
- next step named clearly
- blockers captured
- tests added for new behavior
- docs synchronized with code
- verified research boundary respected
