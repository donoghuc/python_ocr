# Optical Character Recognition for "copy paste" from quarantine VM
We are examining malware on VM cut off from network and available drives. I would like to be able to copy paste some information (hashes/checksums) and some korean filenames for google translate

## Requirements/setup
I am using python3.6 on my local Ubuntu 16.04 machine
I set up a virtualenvironment and added the python packages described in requirements.txt
```
virtualenv -p /home/cas/miniconda/bin/python --no-site-packages ocr
source ocr/bin/activate
pip install -r requirements.txt
```
The main OCR engine used is tesseract-ocr, this is intalled with apt
```
sudo apt-get install tesseract-ocr
```
on virutual machine we have python2.7 on windows, I had nothing to do with that config, but i'm really happy we have python interpreter! 

## Example workflow
__1__
- On virtual machine I have mounted a USB image with OSFmount. 
- The filenames are in characters, want to investigate with google translate! 


__2__
- on VM copy the file name into a file called "unicode_raw.txt"
- run get_utf_codes.py to save out the utf codes for OCR recognition

__3__
-Use OCR to get a string from the character codes

