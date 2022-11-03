## Contributing

First off, thank you for considering contributing to Active Admin. It's people like you that make Active Admin such a great tool.

Where do I go from here?
If you've noticed a bug or have a feature request, make one! It's generally best if you get confirmation of your bug or approval for your feature request this way before starting to code.

If you have a general question about activeadmin, you can post it on Stack Overflow, the issue tracker is only for bugs and feature requests.

## Fork & create a branch

If this is something you think you can fix, then fork Active Admin and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

git checkout -b ${your github name}

## Make a Pull Request

At this point, you should switch back to your master branch and make sure it's up to date with Active Admin's master branch:

git remote add upstream git@github.com:turtle601/python-calculator.git
git checkout master
git pull upstream master
Then update your feature branch from your local copy of master, and push it!

git checkout ${your github name}
git rebase master
git push --set-upstream origin ${your github name}
Finally, go to GitHub and make a Pull Request :D
