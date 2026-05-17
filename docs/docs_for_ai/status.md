# Status

- Phase: Research-first computational template with an explicit human verification boundary
- Last update: verified research files, research-first docs, notebook checkpoint cleanup, research-oriented examples, tracked security automation, CodeQL default-setup compatibility, filtered dependency auditing, and post-bootstrap test cleanup are aligned
- Next step: Create a project from the template, run bootstrap once, and confirm `research/question.md` plus `research/protocol.md`
- Blockers: None in template state
- License: MIT

## Checklist

- [x] Verified research area exists
- [x] Experiments and notebooks working areas exist
- [x] Python support package structure exists
- [x] CLI commands exist
- [x] Human documentation baseline exists
- [x] AI documentation baseline exists
- [x] Bootstrap resyncs the editable install
- [x] Bootstrap refuses re-running after template setup is complete
- [x] Bootstrap removes template-only test harness self-tests from derived projects
- [x] CI validates a fresh template copy through bootstrap plus quality
- [x] Dependabot config is tracked for Python tooling and GitHub Actions
- [x] Security workflow runs dependency review and pip-audit
- [x] CodeQL is documented as a GitHub default-setup repository setting
- [x] Minimal stable wrappers exist
- [x] Cleanup command protects `.venv`
- [x] Cleanup tolerates inaccessible subtrees conservatively
- [ ] Project-specific bootstrap completed
- [ ] Research question validated for the real project
- [ ] Research protocol validated for the real project
- [ ] Research claims reviewed for the real project
- [ ] Third-party license inventory regenerated after dependency install
