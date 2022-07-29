![](https://img.shields.io/badge/platform-Ubuntu-orange)
![](https://img.shields.io/badge/python-3.10.x-yellow)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Fraccs/youtooler-python)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Fraccs/youtooler-python/test)
![GitHub](https://img.shields.io/github/license/Fraccs/youtooler-python)
![GitHub issues](https://img.shields.io/github/issues/Fraccs/youtooler-python)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Fraccs/youtooler-python)

# YouTooler

> Multithreaded YouTube viewer BOT based on TOR.

## Table of contents

1. [ Disclaimer ](#disclaimer)
2. [ Requirements ](#requirements)
3. [ Installation ](#installation)
4. [ Usage ](#usage)
5. [ Contribute ](#usage)

---

## Disclaimer

***Developers assume no liability and are NOT RESPONSIBLE for any misuse or damage caused by this program.***

***This is just an experiment, the usage of this program is NOT RECCOMENDED.***

---

## Requirements

- **Linux** High end machine

- **Python** 3.10.x

- **Firefox ESR**

- **Geckodriver**

- **TOR**

- **High speed** internet connection.

---

## Installation

### Firefox Installation (Debian / Ubuntu)

```bash
sudo add-apt-repository ppa:mozillateam/ppa
```

```bash
sudo apt update
```

```bash
sudo apt install firefox-esr
```

### Geckodriver Installation (Debian / Ubuntu)

```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz
```

```bash
tar -xvzf geckodriver*
```

```bash
chmod +x geckodriver
```

```bash
sudo mv geckodriver /usr/local/bin/
```

### TOR Installation (Debian / Ubuntu)

```bash
sudo apt install tor
```

### Youtooler Installation (Linux)

```bash
git clone https://github.com/Fraccs/youtooler-python.git
```

```bash
cd youtooler-python
```

```bash
pip install -r requirements.txt
```

```bash
pip install .
```

---

## Usage

```bash
cd src
```

```bash
python3 youtooler.py <url> [--level <level>]
```

### Arguments

- Positionals
  - url: str (The url of the video)

- Optionals
  - --level: int (The number of threads to start)

---

## Contribute

> If you wish to contribute to the project, start by <a href="https://github.com/Fraccs/youtooler-python/fork">forking the repo</a>.

### Branching convention

> This project uses <u>gitflow</u> and pull requests.

Before creating a new feature/bugfix a <a href="https://github.com/Fraccs/youtooler-python/issues">related issue should be opened</a>.

The branch name should follow the pattern: ```<issue_id>-<branch_type>-<branch_name>``` where ***issue_id*** is the number that identifies the previously opened issue (i.e. 29), ***branch_type*** is a short descriptor of what kind of feature/bugfix the branch is about and should be either ```feat|fix|docs|refactor|test``` and ***branch_name*** is a short descriptive name of the branch.

***An example feature workflow would look like this:***

1. <a href="https://github.com/Fraccs/youtooler-python/issues">Create issue on the main repo</a>.

2. Start a new feature: ```git flow feature start <issue_id>-<branch_type>-<feature_name>```.

3. Commit your code following the <a href="#commit-convention">commit convention</a> to build the commit message.

4. Push the feature to your remote: ```git flow feature publish <issue_id>-<branch_type>-<feature_name>```

5. Open the pull request and wait for it to be tested, reviewed and merged.

### Commit convention

This project follows the <a href="https://github.com/angular/angular/blob/main/CONTRIBUTING.md#-commit-message-format">Angular.js commit convention</a> where each commit should have the following structure:

```
<HEADER>
<blank_line>
<BODY>
<blank_line>
<FOOTER>
```

```
HEADER:

<type>(<scope>): <short summary>
  │       │             │
  │       │             └─ Summary in present tense. All lowercase. No period at the end.
  │       │
  │       └─ Commit Scope: *|main|parser|app|thread|webdriver|tor|utils|logs|
  |                           exceptions|workflows|readme|requirements|setup|test_<module_name>
  │
  └─ Commit Type: feat|fix|refactor|docs|test|chore|style
```

```
BODY:

Just as in the summary, use the imperative, present tense: "fix" not "fixed" nor "fixes".

Explain the motivation for the change in the commit message body. This commit message should explain why you are making the change. You can include a comparison of the previous behavior with the new behavior in order to illustrate the impact of the change.
```

```
FOOTER:

The footer can contain information about GitHub issues and other PRs that this commit closes or is related to.
```

> If the type of commit is test, the scope should only be the name of the module that is being tested and not test_<module_name>.
