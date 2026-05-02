# Status

- Phase: Cheap template tuned for low-token, low-usage agent workflows
- Last update: default quality is now cheap Ruff-only, full verification is explicit, AI docs are shorter, and CI defaults are lighter
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
- [x] Minimal stable wrappers exist
- [x] Cleanup command protects `.venv`
- [x] Cleanup tolerates inaccessible subtrees conservatively
- [ ] Project-specific bootstrap completed
- [ ] Third-party license inventory regenerated after dependency install
