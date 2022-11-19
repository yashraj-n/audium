
<h1 align="center">
  <a href="https://github.com/yashraj-n/audium">
    <img src="images/banner.png" alt="audium-banner">
  </a>
</h1>

<p align="center">
<img src="https://img.shields.io/github/repo-size/yashraj-n/audium?style=for-the-badge"/>
<img src="https://img.shields.io/github/languages/count/yashraj-n/audium?style=for-the-badge" />
<img src="https://img.shields.io/github/license/yashraj-n/audium?style=for-the-badge" />
 <a target="_blank" href="https://twitter.com/NarkeYashraj/"><img height="20" src="https://img.shields.io/twitter/follow/NarkeYashraj?style=for-the-badge" /></a>
</p>
<p align="center">
🎤 Encode Audio with custom message 
</p>

<p align="center">
<a href="#introduction">Introduction</a> &nbsp;&bull;&nbsp;
<a href="#installation">Installation</a> &nbsp;&bull;&nbsp;
<a href="#usage">Usage</a> &nbsp;&bull;&nbsp;
<a href="#documentation">Documentation</a> &nbsp;&bull;&nbsp;
<a href="#issue">Issue?</a>
</p>

# Introduction
Audium is tool to encode custom data to a `.wav` file.
You can: 
- Encode and Decode data with key
- Read/Save Data to file
- Much more...


## Installation
##### Clone the Repository
```bash
git clone https://github.com/yashraj-n/audium
```
##### Change Directory
```bash
cd audium
```
##### Install Dependencies
```bash
pip install -r requirements.txt
```


## Usage
To Encode:<br/>
```
audium encode -f green -k 'An Apple A day keeps doctor away' -d  "I like apples"
```
To Decode: <br>
```
audium decode -f green -k 'An Apple A day keeps doctor away'
```

## Documentation
##### Help Command
Use audium --help to get all the commands
```bash
$ audium --help
usage: Audium [-h] -f AUDIOFILE [-d [DATA]] [-df DATAFILE] [-k [KEY]] [-v [VERBOSE]] [-of [OUTPUTFILE]] {encode,decode}

Encode and decode audio files

positional arguments:
  {encode,decode}       Method to use

options:
  -h, --help            show this help message and exit
  -f AUDIOFILE, --audiofile AUDIOFILE
                        Name of the audio file to encode/decode
  -d [DATA], --data [DATA]
                        Data to encode
  -df DATAFILE, --datafile DATAFILE
                        File containing data to encode
  -k [KEY], --key [KEY]
                        Key to use for encryption/decryption
  -v [VERBOSE], --verbose [VERBOSE]
                        Verbose output
  -of [OUTPUTFILE], --outputfile [OUTPUTFILE]
                        Name of the output file

By @yashraj-n
```
You only need to provide filename and method in CLI
Options in `[]` are Optional and are not required

## Issue
This repository is maintained actively, so if you face any issue please <a href="https://github.com/yashraj-n/audium/issues/new">raise an issue</a>.

<h4>Liked the work ?</h4>
Give the repository a star :-)