# Status

- Phase: Education template baseline ready for course authoring
- Last update: the template is centered around `course/`, learner-facing docs, course-oriented bootstrap language, tracked security automation, CodeQL default-setup compatibility, filtered dependency auditing, and smoke-safe long identity replacements while keeping the Python support layer minimal
- Next step: Run bootstrap once and replace the sample modules in `course/` with your real lessons
- Blockers: None in template state
- License: MIT

## Checklist

- [x] Course-first content structure exists
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
- [ ] Course-specific bootstrap completed
- [ ] Third-party license inventory regenerated after dependency install
