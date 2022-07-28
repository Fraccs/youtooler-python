![](https://img.shields.io/badge/platform-Ubuntu-orange)
![](https://img.shields.io/badge/python-3.10.x-yellow)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Fraccs/youtooler-python)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Fraccs/youtooler-python/test)
![GitHub](https://img.shields.io/github/license/Fraccs/youtooler-python)
![GitHub issues](https://img.shields.io/github/issues/Fraccs/youtooler-python)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Fraccs/youtooler-python)

# Youtooler

> Multithreaded YouTube viewer BOT based on TOR.

## Disclaimer

***Developers assume no liability and are NOT RESPONSIBLE for any misuse or damage caused by this program.***

***This is just an experiment, the usage of this program is NOT RECCOMENDED.***

## Requirements

- **Linux** High end machine

- **Python** 3.10.x

- **Firefox ESR**

- **Geckodriver**

- **TOR**

- **High speed** internet connection.

## Firefox Installation (Debian / Ubuntu)

```bash
sudo add-apt-repository ppa:mozillateam/ppa
```

```bash
sudo apt update
```

```bash
sudo apt install firefox-esr
```

## Geckodriver Installation (Debian / Ubuntu)

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

## TOR Installation (Debian / Ubuntu)

```bash
sudo apt install tor
```

## Youtooler Installation (Linux)

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

## Usage

```bash
cd src
```

```bash
python3 youtooler.py <url_of_video> [--level <level>]
```

> Make sure that the URL is in the correct format: ```https://www.youtube.com/watch?v=<video_id>```
