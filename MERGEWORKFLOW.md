# Merge GitWorkFlow

## Getting Started (Do Only Once)

1. clone the repository
```git clone https://usc.bootcampcontent.com/fireproofsocks/fpg1.git```

2. then create a branch
```git checkout -b {name of your branch}```
^ this creates a local branch on your desktop
when creating this branch, make sure that this is a feature/{function name} this will help me figure out what kind of functions are being merged to the dev_master branch

3. then create a remote branch that is connected to your local branch
 ```git push -u origin {name of your branch}```

## After you have created a branch
4. ```git pull origin dev_master```

5. merge the dev_master branch to your own branch  
```git merge dev_master```

6. edit your file you want to edit

7. 
```git add .```
```git commit -m "message"```
```git push origin {your branch name}```

## NOTES
You should never have to access the dev_master branch. If you want to create a merge request, just do so online, and I'll make sure to check. 

Make sure we are always communicating with our teammates. We need to know which files we are working on and what we need to do!