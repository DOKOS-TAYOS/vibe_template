# Status

- Phase: Template hardened for Windows-first bootstrap and maintenance
- Last update: test isolation, cleanup walking, bootstrap guardrails, wrapper/runtime behavior, fresh-copy CI smoke coverage, public-template licensing, security automation, and post-bootstrap test cleanup were tightened
- Next step: Create a project from the template and run bootstrap once
- Blockers: None in template state
- License: MIT

## Checklist

- [x] Library-first package structure exists
- [x] CLI commands exist
- [x] Human documentation baseline exists
- [x] AI documentation baseline exists
- [x] Bootstrap resyncs the editable install
- [x] Bootstrap refuses re-running after template setup is complete
- [x] Bootstrap removes template-only test harness self-tests from derived projects
- [x] CI validates a fresh template copy through bootstrap plus quality
- [x] Dependabot config is tracked for Python tooling and GitHub Actions
- [x] Security workflow runs dependency review, CodeQL, and pip-audit
- [x] Minimal stable wrappers exist
- [x] Cleanup command protects `.venv`
- [x] Cleanup tolerates inaccessible subtrees conservatively
- [ ] Project-specific bootstrap completed
- [ ] Third-party license inventory regenerated after dependency install
