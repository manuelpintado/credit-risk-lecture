# Git Exercise

## Example

Assuming you are on the `master` branch of a local repository, create a new branch named\
 `bugfix` from an existing branch called `feature-1`

* `git checkout feature-1`
* `git checkout -b bugfix`

## A - Cloning

Consider the following github repository:
* https://github.com/RHDZMOTA/bitso-market-consumer

How would you clone the repository and change to the `stage` branch? Add your commands:

* `git clone https://github.com/RHDZMOTA/bitso-market-consumer`
* `cd bitso-market-consumer`
* `git checkout stage`


## B - Git status

Consider the following output from the `git status` command:


```text
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	LICENSE.md
```

According to git, what's the difference between the `README.md` and `LICENSE.md` file? 

* `READ.me file will be modified and is ready for commit and LICENCE.md will not be added to the branch`

## C - Local merging

Assuming you are on a repository that contains the following branches:
* `master`
* `develop`

You are currently on `master`. Create a branch from `develop` named `deploy` and merge into `master`.

* `git ckeckout develop`
* `git chechout -b deploy`
* `git merge deploy/master`


## D - Sync from remote

Assuming you are on a repository with two remotes: 
* `origin`
* `upstream`

How can you update the `master` branch from `origin` with the latest changes from the `upstream` `master` branch? 
* `git chechout master`
* `git fetch upstream`
* `git merge upstream/master`
* `git push origin master`
