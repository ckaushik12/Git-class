# How to pull any file from git hub
1.Login with your github user name
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT (main)
$ git config --global user.name ckaushik12

2.Login with your email id
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT (main)
$ git config --global user.email ck.kaushik.2911@gmail.com

3.To check login credentials use below command 
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT (main)
$ git config --global --list
core.autocrlf=true
user.name=ckaushik12
user.emal=ck.kaushik.2911@gmail.com
user.email=ck.kaushik.2911@gmail.com

4.To make the code compatible for windows use below command
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT (main)
$ git config --global core.autocrlf true

5.To make the code compatible for linux use below command
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT (main)
$ git config --global core.autocrlf input


6.To check current working directory use below command
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT (main)
$ pwd
/c/Users/Steve/Data Science/GIT

7.To create a new folder use below command
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT (main)
$ mkdir git class

Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT (main)
$ mkdir python

8.To check all available directories/ folders in current working directories
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT (main)
$ ls
class/  git/  python/

9.To get inside any folder
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT (main)
$ cd git

10.To pull any file from the git hub, use HTTPS code link copied from the git hub
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git (main)
$ git clone https://github.com/ckaushik12/Git-class.git
Cloning into 'Git-class'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

11.To create a new file
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/python (main)
$ vim f1.py

12.To check data inside any file
	- to go in edit mode press ‘I’
	- to exist edit mode press ‘ESC’
	- to save press ‘:wq’ then press ‘Enter’
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/python (main)
$ cat f1.py
a=23
b=15
c=a+b
print(c)

Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/python (main)
$ cat f1.py
a=23
b=15
c=a+b
print(c)

13.To get out of any directory
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/python (main)
$ cd ..

14.To check hidden files availabel in the current working directories
	-if git file available here, that means it is in staging area
	- if no git file, that means it is in local computer only
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ ls -al
total 5
drwxr-xr-x 1 Steve 197612  0 Jun 15 14:50 ./
drwxr-xr-x 1 Steve 197612  0 Jun 15 14:50 ../
drwxr-xr-x 1 Steve 197612  0 Jun 15 14:50 .git/
-rw-r--r-- 1 Steve 197612 11 Jun 15 14:50 README.md

15.Use below command to put any file in staging area

Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/python (main)
$ git init
Initialized empty Git repository in C:/Users/Steve/Data Science/GIT/git/pgit/

Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/python (master)
$ ls -al
total 5
drwxr-xr-x 1 Steve 197612  0 Jun 15 15:08 ./
drwxr-xr-x 1 Steve 197612  0 Jun 15 14:50 ../
drwxr-xr-x 1 Steve 197612  0 Jun 15 15:08 .git/
-rw-r--r-- 1 Steve 197612 25 Jun 15 14:53 f1.py

16.Use below command to add files in staging area

Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/python (master)
$ git add .
warning: in the working copy of 'f1.py', LF will be replaced by CRLF the me Git touches it

17.To check the status of changes done
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/python (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   f1.py


18.To check past commits log

Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/python (master)
$ git log
fatal: your current branch 'master' does not have any commits yet

19.Name the commit version
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/python (master)
$ git commit -m "First commit"
[master (root-commit) cdd84c8] First commit
 1 file changed, 5 insertions(+)
 create mode 100644 f1.py

# How to push any file in git hub
Step 1.
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT (main)
$ cd git

Step 2.
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git (main)
$ ls
Git-class/  python/  stats/

Step 3.
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git (main)
$ cd Git-class

Step 4.
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ ls -al
total 5
drwxr-xr-x 1 Steve 197612  0 Jun 15 14:50 ./
drwxr-xr-x 1 Steve 197612  0 Jun 15 14:50 ../
drwxr-xr-x 1 Steve 197612  0 Jun 15 14:59 .git/
-rw-r--r-- 1 Steve 197612 11 Jun 15 14:50 README.md

Step 5.
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ vim f1.py

Step 6.
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ cat f1.py
a=2
b=34
c=a*b
print(c)

Step 7.
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ git add .
warning: in the working copy of 'f1.py', LF will be replaced by CRLF the it

Step 8.
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ git config --global autocrlf true
error: key does not contain a section: autocrlf

Step 9.
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   f1.py


Step 10.
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ git commit -m "First commit"
[main 3798a1b] First commit
 1 file changed, 4 insertions(+)
 create mode 100644 f1.py

Step 11.
Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 297 bytes | 148.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/ckaushik12/Git-class.git
   e980184..3798a1b  main -> main

Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ vim f1.py

Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ git commit -m "second commit"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   f1.py

no changes added to commit (use "git add" and/or "git commit -a")

Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ git add f1.py
warning: in the working copy of 'f1.py', LF will be replaced by CRLF the it

Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ git commit -m "second commit"
[main d52b2f9] second commit
 1 file changed, 1 insertion(+)

Steve@ALI-SOLAR-LIT2022 MINGW64 ~/Data Science/GIT/git/Git-class (main)
$ git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 303 bytes | 151.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/ckaushik12/Git-class.git
   3798a1b..d52b2f9  main -> main


