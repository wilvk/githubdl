# Github Path Downloader

A tool for downloading individual files/directories from Github or Github Enterprise.

This circumvents the requirement to clone a complete repository.

# Requirements:

- Python 3.4+
- A Github or Github Enterprise Account

# Installation:

pip:

```bash
$ pip install githubdl
```

http:

```bash
$ pip install git+https://github.com/wilvk/githubdl.git
```

ssh:

```bash
$ pip install git+ssh://git@github.com:wilvk/githubdl.git
```

from clone:

```bash
$ git clone git@github.com:wilvk/githubdl.git
$ cd githubdl
$ pip install -e .
```

# Usage:

## Obtaining a Github token:

You will need a token from either Github Enterprise or Github as this package works with the Github v3 API.

To do this:

- Log into your Github account
- Click the Avatar Menu in the top-right corner, and select `Settings`
- On the Settings page, from the menu on the left-hand side, select `Developer Settings`
- From the Developer Settings page, from the menu, select `Personal access tokens`
- Click the `Generate new token` button
- Enter a name for the token. The token should only require the `read:org` permission specified.

There are also instructions on how to do this [here](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/).

# Usage (from the commandline):

With your new Github token, export it as the environment variable `GIT_TOKEN`.

```bash
$ export GIT_TOKEN=1234567890123456789012345678901234567890123
```

## Single file:

Then, for example, to download a file called `README.md` from the repository `http://github.com/wilvk/pbec`:

```bash
$ githubdl -u "http://github.com/wilvk/pbec" -f "README.md"
2018-05-12 07:19:16,934 - root         - INFO     - Requesting file: README.md at url: https://api.github.com/repos/wilvk/pbec/contents/README.md
2018-05-12 07:19:18,165 - root         - INFO     - Writing to file: README.md
```

## Entire directory:

```bash
$ githubdl -u "http://github.com/wilvk/pbec" -d "support"
2018-05-12 07:19:41,667 - root         - INFO     - Retrieving a list of files for directory: support
2018-05-12 07:19:41,668 - root         - INFO     - Requesting file: support at url: https://api.github.com/repos/wilvk/pbec/contents/support
2018-05-12 07:19:42,978 - root         - INFO     - Requesting file: support/Screen Shot 2017-12-10 at 9.27.56 pm.png at url: https://api.github.com/repos/wilvk/pbec/contents/support/Screen Shot 2017-12-10 at 9.27.56 pm.png
2018-05-12 07:19:46,274 - root         - INFO     - Writing to file: support/Screen Shot 2017-12-10 at 9.27.56 pm.png
2018-05-12 07:19:46,286 - root         - INFO     - Retrieving a list of files for directory: support/docker
...
```

# Entire repository:

```bash
$ githubdl -u "http://github.com/wilvk/pbec" -d "/" -t "."
```

Note: if `-t` is not set, output will go to your `/` directory.

# List all tags for a repository in JSON:

```bash
$ githubdl -u "http://github.com/wilvk/pbec" -a
```

# List all branches for a repository in JSON:

```bash
$ githubdl -u "http://github.com/wilvk/pbec" -b
```

## Options:

Current options are:

```bash
githubdl --help             or     -h
         --file                    -f
         --dir                     -d
         --url (required)          -u
         --target                  -t
         --git_token               -g
         --log_level               -l
         --reference               -r
         --tags                    -a
         --branches                -b
```

## Logging:

Valid log levels are: `DEBUG`, `INFO`, `WARN`, `ERROR`, `CRITICAL`

## References:

References can be applied to file and directory download only and consist of valid:

  - repository tags
  - commit SHAs
  - branch names.

# Usage (as a package):

## Loading the package (in a REPL):

```
python
Python 3.4.8 (default, Feb  7 2018, 02:31:08)
[GCC 5.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import githubdl
```

## Downloading a directory:

### Passing in a token:

```python3
>>> githubdl.dl_dir("https://github.com/wilvk/pbec", "support", github_token="1234567890123456789012345678901234567890123")
```

### Token as an environment variable:

In bash:

```bash
$ export GIT_TOKEN=1234567890123456789012345678901234567890123
```

In Python:

```python3
>>> githubdl.dl_dir("https://github.com/wilvk/pbec", "support")
```

### Saving to a different path:

```python3
>>> githubdl.dl_dir("https://github.com/wilvk/pbec", "support", "support_new")
```

## Downloading a file:

### Passing in a token:

```python3
>>> githubdl.dl_file("https://github.com/wilvk/pbec", "README.md", github_token="1234567890123456789012345678901234567890123")
```

### Token as an environment variable:

In bash:

```bash
$ export GIT_TOKEN=1234567890123456789012345678901234567890123
```

In Python:

```python3
>>> githubdl.dl_file("https://github.com/wilvk/pbec", "README.md")
```

### Saving with a different filename:

```python3
>>> githubdl.dl_file("https://github.com/wilvk/pbec", "README.md", "NEW_README.md")
```

# Extended options:

## File download options:

Only `repo_url` and `file_name` are required.

```python3
  def dl_file(repo_url, file_name, target_filename='', github_token='', log_level='', reference=''):
```

## Directory download options:

Only `repo_url` and `base_path` are required.

```python3
  def dl_dir(repo_url, base_path, target_path='', github_token='', log_level='', reference=''):
```

## Tags download options:

Only `repo_url` is required.

```python3
  def dl_tags(repo_url, github_token='', log_level=''):
```

## Branches download options:

Only `repo_url` is required.

```python3
  def dl_branches(repo_url, github_token='', log_level=''):
```

### A note on logging:

Log level is passed in as `logging` variable. e.g.

```python3
>>> import logging
>>> import githubdl
>>> githubdl.dl_file("http://github.com/wilvk/pbec", "README.md", log_level=logging.DEBUG)
```

# Tests:

```bash
$ auto/run-tests
```

Note: You will have to have a Github token exported as `GIT_TOKEN` to run the tests.
