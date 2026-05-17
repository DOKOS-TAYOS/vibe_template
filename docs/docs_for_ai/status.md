# Status

- Phase: Strong AI template baseline ready for high-rigor agent work
- Last update: design-first AI workflow guardrails, full verification, tracked security automation, CodeQL default-setup compatibility, filtered dependency auditing, and post-bootstrap test cleanup are in place
- Next step: Create a project from the template and run bootstrap once
- Blockers: None in template state
- License: MIT

## Checklist

- [x] Library-first package structure exists
- [x] CLI commands exist
- [x] Human documentation baseline exists
- [x] AI documentation baseline exists
- [x] Strong workflow guidance for AI contributors is explicit
- [x] Bootstrap resyncs the editable install
- [x] Bootstrap refuses re-running after template setup is complete
- [x] Bootstrap removes template-only test harness self-tests from derived projects
- [x] CI validates a fresh template copy through bootstrap plus quality
- [x] Full verification stays the default quality gate
- [x] Dependabot config is tracked for Python tooling and GitHub Actions
- [x] Security workflow runs dependency review and pip-audit
- [x] CodeQL is documented as a GitHub default-setup repository setting
- [x] Minimal stable wrappers exist
- [x] Cleanup command protects `.venv`
- [x] Cleanup tolerates inaccessible subtrees conservatively
- [ ] Project-specific bootstrap completed
- [ ] Third-party license inventory regenerated after dependency install
