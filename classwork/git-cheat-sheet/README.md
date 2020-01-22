# Git Cheat Sheet

Test it out [here](https://learngitbranching.js.org/?NODEMO)! Or take a [github course](https://lab.github.com/githubtraining/introduction-to-github) for more examples.

## Setup

### Configuration

Run the following commands to configure your local git:

```
git config --global user.name [github-user]
```

```
git config --global user.email [github-email]
```

```
git config --global core.editor vim
```

### Initializing or cloning repos

Clone an existing repository using:

```
git clone [url]
```

Or initialize a directory as a repository:

```
git init
```

And then assign a remote:

```
git remote add [remote-alias] [url]
```

**Note**: the `alias` is usually `origin`.

## Staging area

Show modified and staged files:

```
git status
```

Add file to the staging area: 

```
git add [file-path]
```

Remove a file from staging area but retain changes: 

```
git reset [file-path]
```

Show changes of file from the last commit: 

```
git diff [file-path]
```

## Commits

Add current stage to a commit:

```
git commit -m "[message]"
```

Delete the last commit (with changes):

```
git reset --hard HEAD~1
```

Note: replace the `1` by `n` to delete the last `n` commits or use the commit ID (SHA) to delete up to that point in history.

Apply commits of current branch ahead of another: 

```
git rebase [branch]
```

## Branches

List current branches: 

```
git branch
```

Get (fetch) all branches from a remote: 

```
git fetch [remote-alias]
```

Change to an existing branch: 

```
git checkout [branch-name]
```

Create and change to a new branch from current one: 

```
git checkout -b [branch-name]
```

Merge branch history into current one: 

```
git merge [branch]
```

Merge remote branch history to update branch: 

```
git merge [remote-alias]/[branch]
```

Transmit local branch history to remote: 

```
git push [remote-alias] [branch]
```

Fetch and merge commits from remote branch: 

```
git pull [remote-alias] [branch]
```

## Inspect and compare

Show the commit history:

```
git log --oneline
```

Show the commit history graph:

```
git log --oneline --graph
```

Show commits on `branch-a` that are not on `branch-b`:

```
git log branch-b...branch-a
```

Show the diff of changes in `branch-a` that are not in `branch-b`:

```
git diff branc-b...branch-a
```
