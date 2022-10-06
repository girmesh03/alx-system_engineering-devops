#description of what each script is doing

0. switches the current user.
1. prints the effective username of the current user.
2. prints all the groups the current user is part of.
3. changes the owner of the file hello to the user betty.
4. creates an empty file called hello.
5. adds execute permission to the owner of the file hello.
6. adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
7. adds execution permission to the owner, the group owner and the other users, to the file hello.
8. sets the permission to the file hello as follows:
		Owner: no permission at all
		Group: no permission at all
		Other users: all the permissions
9. sets the mode of the file hello to this:
		-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
10. sets the mode of the file hello the same as olleh’s mode.
		The file hello will be in the working directory
		The file olleh will be in the working directory
11. adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
12. creates a directory called my_dir with permissions 751 in the working directory.
13. changes the group owner to school for the file hello
		The file hello will be in the working directory
