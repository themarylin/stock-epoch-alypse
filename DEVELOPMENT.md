# Development

## Getting Started (Do Only Once)

To get started with this repository, you first need to clone it onto your local machine.

```bash
git clone <repo-url>
```

For example:

```bash
git clone git@usc.bootcampcontent.com:fireproofsocks/fpg0.git
```

Next, move into the directory that was just created, e.g.

```bash
cd fpg0
```

Finally, create a new project in your editor (a.k.a. IDE, such as Visual Studio Code, Sublime, Atom, or IDEA) and make any configuration changes to your editor to make it easy for you to find this project quickly and work on it effectively, e.g. installing any needed plugins so your editor can properly highlight code.


## Development Preparation (Every Day)

When you first start work for the day, you'll want to sync up your local files with those in the cloud.  

In the Terminal:

```bash
cd path/to/your/project
git fetch origin
```

Fetching the origin will let your local repository know what new branches have been pushed up to the remote repository.  It's a way for you to keep an eye on the changes that your team-members have been pushing up.

Next, you should pull down the latest changes to the `master` branch so that your copy is up to date.  To do this, you should move to the `master` branch, then pull down any changes:

```
git checkout master
git pull origin master
```


## Doing Work

Once you have the latest changes synced to your local machine, you are ready to begin work.

### Create a new branch off of master

It's a much cleaner workflow if you do all of your work _out_ of the master branch. That way you will never be prevented from pulling down the latest changes that have been merged into the master branch.

> **Choosing a Branch Name** It's common to use naming conventions for your branches depending on what kind of work you're doing in them.  
> E.g., branch names often use prefixes like `feature` or `bugfix`.
> Also, your branch names are searchable and your team-members will see them, so it's good to provide a brief description of what changes they contain.

Create a new branch and change to it using `git checkout -b <new-branch-name>`, e.g. 

```bash
# Make sure you are splitting off your new branch from the master branch!
git checkout master
git checkout -b feature/adding-plotly-charts
```

### Adding Your Changes

As you work, you should take advantage of Git to be the ultimate power-tool in Undo technology.  Any time you do anything sigificant like finally getting some tricky new thing to work, COMMIT YOUR WORK.  Add a descriptive message (again, these are searchable and they help your team-members see what you've been up to)  

```
git add .
# Or, you can selective add files by name, e.g.
# git add path/to/file.py

git commit -m "Got that tricky bean_counter() function to work"

# Push your local changes up to the remote repository using push:
# git push origin <branch-name>

# Use `git branch` to see the name of your active branch (in case you forgot)
git branch

# Copy your branch name and use it to push your local changes up 
git push origin feature/adding-plotly-charts
```

Feel free to add as many commits as you want.  It can be 1, it can be hundreds.  Keep pushing them up and saving them to the cloud: your team-members, TAs, and instructors can then easily pull down your work and help you debug it.

### Merging Your Changes

Once you feel your feature or bugfix work is substantially complete, you are ready to begin the merge process.

**1. Make sure all of your work on your branch has been committed.**  

Running `git status` should come up clean, e.g.

```bash
git status
On branch feature/adding-plotly-charts
nothing to commit, working tree clean
```

If there are some files listed by `status`, you probably need to commit them (unless you are sure you don't).

**2. One last time, make sure your local copy of the `master` branch is up to date:**

```bash
git checkout master
git pull origin master
git fetch origin
```

Now your local `master` branch should be up to date.

**3. Change back to the branch you have been working on**

e.g.

```bash
git checkout feature/adding-plotly-charts
```

**4. Merge the `master` branch _into_ your branch.**

```bash
git merge master
```

This is where you may need to resolve conflicts!  Take note of any files that Git says has conflicts.  Open those files in your editor and look for the `<<<<<` and `>>>>>>` marks that denote which regions of code were in conflict between the 2 branches.  You will have to choose which sections to keep and which to abandon.  Ask me or a TA for help if needed!

**5. Push your branch to the remote repository**

```bash
git push origin feature/adding-plotly-charts
```


**6. Open a Merge Request**

In GitLab, open a Merge request (Github calls these "Pull Requests") that wants to merge your branch into the `master` branch.
Slack out the link to the merge request to your team-members.

One of your team-members should approve the merge in the Gitlab UI. Optionally, you may choose to "squash commits" and to delete the branch after the merge -- that's usually considered good house-keeping.

Your group members should now know that their local copies of `master` is now out of date because you have just added in your changes! 

> Note: In many companies, access to the `master` branch is often limited, so merge requests are often the only way to get your code into the `master` branch.