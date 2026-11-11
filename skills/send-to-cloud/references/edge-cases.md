# Conditional handoff cases

Read only the relevant case.

## Mixed index or interrupted Git operation

Record the original branch, HEAD, status, staged paths, and staged/unstaged boundaries before mutation.
Keep unrelated staged content out of the checkpoint without unstaging or committing it.
Use a reviewed isolation method only when it preserves the original worktree and index and runs required hooks.
Do not use raw commit plumbing to avoid hooks.
If isolation cannot preserve staged intent, stop before changing the index. Return the exact recovery action instead.

Do not interrupt an active merge, rebase, cherry-pick, or unresolved conflict.
Preserve the operation and report the prerequisite for checkpoint creation.
A detached HEAD permits a new branch from that exact commit when otherwise safe.

## Repository and object dependencies

Process only authorized repositories. Record dependency relationships and omitted repositories or worktrees.
Do not initialize or create a remote for an unknown folder.
Missing authentication or remote configuration requires a recovery handoff, not an access-control workaround.

For submodules, record each required commit and its accessible remote. A parent commit cannot transfer dirty submodule files.
For LFS, verify the required objects reached the intended storage. A pointer commit alone does not prove object availability.
Missing objects or inaccessible commits block their dependent work, not unrelated portable work.

## Cloud prerequisites

Verify only requirements relevant to the next task, such as private packages, runtimes, service access, and essential assets.
Provide safe provisioning steps for excluded files. Do not copy credentials into documentation or source control.
Distinguish editing from platform-specific execution. For example, Linux access does not establish Xcode, simulator, or signing capability.
A repository push does not establish cloud access. A submitted launch request does not establish execution.
Use the selected provider's supported interface only when launch is separately authorized.

## Resume locally

Inspect local work before fetching cloud changes. Compare histories and preserve both sides.
Integrate only within existing authorization using the project's normal workflow.
Do not overwrite local changes or automatically merge across a dirty worktree.
