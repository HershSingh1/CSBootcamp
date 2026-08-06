git add . - adds everything that you've not saved yet
git commit - permanently saves a copy of staged changes to local git repository's history
git push - command uploads local repository commits to a remote repository

add a note after local repository commits - 
"git commit -m "this is a note"

git status - shows staged changes, unstaged changes, and untracked files

git diff - shows unstaged changes line by line

git diff --staged - shows staged changes and what "git commit" will record in the local repository

git log - commit history

git log --oneline --graph - compact history of commits with branch structure

git pull	Fetches + merges remote changes into your current branch
git fetch	Downloads remote changes but doesn't merge them
git clone <url>	Copies a whole repo down for the first time
git remote -v	Shows which remote(s) you're connected to


git branch	List branches, or git branch <name> to create one
git switch <name>	Move to a different branch
git switch -c <name>	Create and switch to a new branch in one step
git merge <name>	Merge another branch into your current one


git restore <file>	Discards uncommitted changes to a file	Yes — changes are gone
git restore --staged <file>	Unstages a file, keeps the edits	No
git reset --soft HEAD~1	Undoes last commit, keeps changes staged	No
git reset --hard HEAD~1	Undoes last commit, deletes the changes entirely	Yes
git revert <commit>	Creates a new commit that undoes an old one	No — preserves history

git stash	Shelves uncommitted changes, gives you a clean working directory
git stash pop	Brings the most recent stash back
git stash list	Shows everything you've stashed