# Status

- Phase: Cheap template tuned for low-token, low-usage agent workflows
- Last update: cheap Ruff-first defaults, lighter CI, tracked security automation, CodeQL default-setup compatibility, filtered dependency auditing, and post-bootstrap test cleanup are in place
- Next step: Create a project from the template and run bootstrap once
- Blockers: None in template state
- License: MIT

## Checklist

- [x] Library-first package structure exists
- [x] CLI commands exist
- [x] Human documentation baseline exists
- [x] Cheap-first AI documentation baseline exists
- [x] Default `quality` flow stays cheap
- [x] Full verification path exists through `quality --full`
- [x] Bootstrap resyncs the editable install
- [x] Bootstrap refuses re-running after template setup is complete
- [x] CI defaults are lighter than the main template
- [x] Fresh-copy smoke validation still exists
- [x] Bootstrap removes template-only test harness self-tests from derived projects
- [x] CI validates a fresh template copy through bootstrap plus full quality
- [x] Dependabot config is tracked for Python tooling and GitHub Actions
- [x] Security workflow runs dependency review and pip-audit
- [x] GitHub code scanning and secret scanning settings are documented for derived projects
- [x] CodeQL is documented as a GitHub default-setup repository setting
- [x] Minimal stable wrappers exist
- [x] Cleanup command protects `.venv`
- [x] Cleanup tolerates inaccessible subtrees conservatively
- [ ] Project-specific bootstrap completed
- [ ] Third-party license inventory regenerated after dependency install
