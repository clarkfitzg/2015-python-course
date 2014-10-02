
# Introduction to Git
# Git is a version control system, which means it tracks versions of files,
# making it easier to collaborate and providing a backup copy in case of
# mistakes.

# ----- Local Git -----
# If at any time time you need help with a COMMAND, use:
#     man COMMAND
# This won't work on Windows (sorry Windows users). Instead see the
# documentation online.
man git
man git init

# A git repository is a set of files tracked by git. To initialize a new git
# repository, use the command:
#     git init [NAME]
git init git_demo

# Alternatively, we can clone a repository from the web using:
#     git clone URL
git clone https://github.com/nick-ulle/2015-python-course.git

# The new repository starts empty, as we can see with the command:
#     git status
cd git-demo
git status

# Nothing interesting happens until we add files.
vim README.md
# ...

# Now back to git! 
git status

# Git tells us that the new file is untracked, and says that to track the file,
# we have to add it using:
#     git add FILE
git add README.md

# To add every file in the directory, use
#     git add --all

# Now git knows we want to track the file, but we still need to commit this
# version. Making a commit permanently saves the current version of the repo.
# Do this using the command:
#     git commit
git commit

# The commit command will ask you to type a message to save with your changes.
# The first line should be a single sentence summarizing the changes, no more
# 50 characters long. If you need to write more, insert a blank line. Example:
#
#     Add a description of the repository.
#
#     This commit adds a README.md file which describes the repository and
#     chronicles future plans for it.

# If we examine the repo status, git no longer sees any changes. This is
# because we committed them.
git status

# What if we made a mistake with the commit? Fix it with:
#     git commit --amend
vim README.md
git add README.md
git commit --amend

# We can see a history of the last N commits with the command:
#     git log [-N]
git log
git log -3

# ----- Remote Git -----
# Now what if we want to publish our work online (say, GitHub)? First we need
# to tell git about our local repo using:
#     git remote [add NAME URL]
git remote
git remote add origin https://github.com/nick-ulle/demo-repo.git

# Now we can push the work to the repo with the command:
#     git push [LOCATION BRANCH]
# Use the option -u the first time you push to a GitHub repository to set it as
# upstream.
git push -u origin master

# Given permission, other people can push commits to the repository, and we
# can pull down the changes.
#     git pull [LOCATION BRANCH]
git pull origin master
git pull

# When working with a clone of someone else's GitHub repository, you can keep a
# personal copy on GitHub by forking their repository. For example, you'll want
# to fork this workshop's repository.

# ----- Advanced Local Git -----
# Git supports keeping multiple working versions of a repo at once. These are
# represented as branches. To make a new branch and switch to it, use:
#     git branch NAME
#     git checkout NAME
# There's also a shortcut for this:
#     git checkout -b NAME

git branch experimental
git checkout experimental

git branch
git status

# We can delete a branch with the following command:
#     git branch -d NAME
git checkout master
git branch -d experimental

git branch
git checkout -b experimental

# If we make some changes on the branch and commit them, they don't get applied
# to any other branch.
vim testing.py
git add testing.py
git commit

ls
git log

git checkout master
ls
git log

git branch -v

# To merge commits from another branch into the current branch, use:
#     git merge BRANCH
git merge experimental

git status
git log
ls

# Changes that haven't been committed appear on all branches. Sometimes this is
# annoying, so you can also stash changes you don't want to work on right now,
# with the command:
#     git stash [pop]
touch LICENSE
ls
git add LICENSE
git stash

ls
git stash pop
ls

# This is a very bare-bones intro to git. For further reference, see:
#     http://www.git-scm.com/doc
