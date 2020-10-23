# Getting Started

These instructions provide information on usability and accessibility of the program, up and running on your local machine for development and testing purposes.

## System Requirements

The program is made using Python and other downloadable `pip` modules. We recommend installing the version listed below because the program was made on the same version. This increases the stability of the program on the system.

- [Python 3.8.6 (recommended)](https://www.python.org/downloads/release/python-386/)

## Installation & Usage

To download all the assets onto your local machine, follow the command on a bash terminal. This may require `git-scm` to be installed on your system.

```console
git clone https://github.com/harshcut/discord-bot.git
cd discord-bot
pip install discord.py
pip install python-decouple
```

To use this bot in a server, you need a Discord Account. Discord offers an open API to serve requests for both bots and OAuth2 integrations. Create an application on Discord Developer Portal to access your `TOKEN`.

```bat
cd discord-bot
ren .env_sample .env
```

Rename file `.env_sample` to `.env` and paste your `TOKEN`. Note that the `TOKEN` shown below is fake and is used just for demonstration.

```dotenv
SECRET_TOKEN=SrY2MjR0RET4NTEzMzY5ZTA5.54gQHQ.uxR5Av4peeidM2EXRg_vvTq_Z9I
```

For more information, visit [Discord Documentation](https://discord.com/developers/docs/intro#bots-and-apps).

## License

```text
MIT License

Copyright (c) 2020 Harsh Karande

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
