# CustomPATH
Mini PATH wrapper for cmd

## Basic Usage

1 . Add a program to list (a csv file) by dragging an `.exe` file onto `cpatha.exe` or type the full path from cli:
 
```shell
$ cpatha "C:\full\path\to\executable\hello.exe"
```
2 . Execute a listed program from cli using:

```shell
$ cpath hello
# or
$ cpath hello arg1 arg2 ...
```
3 . Add the program folder (`path\to\custom-path\`) to System PATH Environment Variable.

## Executables

### `cpath`

* Executes a listed program from first argv 
* Lists all saved programs if no arg is passed

### `cpathp`

* Shows full path of a listed program from first argv
* Lists all saved programs if no arg is passed
* Can be executed with command redirection operators:
```shell
$ cpathp hello | cmd
$ cpathp hello > hello-path.txt
```

### `cpatha`

* Adds a new program to list from argv or dragging program onto executable. 
* Lists all saved programs if no arg is passed

## Path list

A simple csv (`custom_path.csv`) that saves the programs paths.

This will be generated in first execution.

Can be edited manually.
