# 0x02. Shell, I/O Redirections and filters

In this project, we will explore a powerful feature used by command line programs called input/output redirection. As we have seen, many commands such as ls print their output on the display. This does not have to be the case, however. By using some special notations we can redirect the output of many commands to files, devices, and even to the input of other commands.

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* All your scripts will be tested on `Ubuntu 20.04 LTS`
* All your scripts should be exactly two lines long `($ wc -l file should print 2)`
* The first line of all your files should be exactly `#!/bin/bash`
* A `README.md` file, at the root of the folder of the project, describing what each script is doing
* You are not allowed to use backticks, `&&`, `||` or `;`
* All your files must be executable
* You are not allowed to use `sed` or `awk`

## Project files and Description

| Filename                        | Description |
| ------------------------------- | -------------------- |
| `0-hello_world`                 | Prints "Hello, World", followed by a new line to the standard output |
| `1-confused_smiley`             | Displays a confused smiley `"(Ôo)'` |
| `2-hellofile`                   | Displays the content of the `/etc/passwd` file |
| `3-twofiles`                    | Displays the content of `/etc/passwd` and `/etc/hosts` |
| `4-lastlines`                   | Displays the last 10 lines of `/etc/passwd` |
| `5-firstlines`                  | Displays the first 10 lines of `/etc/passwd` |
| `6-third_line`                  | Displays the third line of the file `iacta` |
| `7-file`                        | creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ending by a new line |
| `8-cwd_state`                   | Writes into the file `ls_cwd_content` the result of the command `ls -la`. If the file `ls_cwd_content` already exists, it should be overwritten |

| `10-no_more_js`                 | Deletes all the regular files with a `.js` extension that are present in the current directory and all its subfolders |
| `11-directories`                | Counts the number of directories and sub-directories in the current directory |
| `12-newest_files`               | Displays the 10 newest files in the current directory |
| `13-unique`                     | Takes a list of words as input and prints only words that appear exactly once |
| `14-findthatword`               | Displayes lines containing the pattern "root" from the file `/etc/passwd` |
| `15-countthatword`              | Displays the number of lines that contain the pattern "bin" in the file `/etc/passwd` |
| `16-whatsnext`                  | Displays lines containing the patter "root" and 3 lines after them in the file `/etc/passwd` |
| `17-hidethisword`               | Displays all the lines in the file `/etc/passwd` that do not contain the pattern "bin" |
| `18-letteronly`                 | Displays all lines of the file `/etc/ssh/sshd_config` starting with a letter |
| `19-AZ`                         | Replaces all characters `A` and `c` from input to `Z` and `e` respectively |
| `20-hiago`                      | Removes all letters `c` and `C` from input |
| `21-reverse`                    | Reverses its input |
| `22-users_and_homes`            | Displays all users and their home directories, sorted by users |
| `100-empty_casks`               | Finds all empty files and directories in the current directory and all sub-directories |
| `101-gifs`                      | Lists all the files with a `.gif` extension in the current directory and all its sub-directories |
| `102-acrostic`                  | Decodes acrostics that use the first letter of each line |
| `103-the_biggest_fan`           | Parses web servers in TSV format as input and displays the 11 hosts or IP addresses which did the most requests |

