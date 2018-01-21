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
![objective](screenshots/mayflower_dir.png?raw=true "dir")

__2__
- on VM copy the file name into a file called "unicode_raw.txt"
![unicode](screenshots/unicode_raw.png?raw=true "unicode")
- run get_utf_codes.py to save out the utf codes for OCR recognition 
- note this is done on vm, in this case we are doing OCR on output_ocr.txt
- this is a great place to make text as clear as possible by changing to large font in notepad
- a high quality image will give OCR algo best chance at accuracy
![unicode](screenshots/utf_codes.png?raw=true "utf codes")
__3__
-on local machine take a screenshot of the unicode representation for OCR analysis
![mp3](screenshots/mp3_chars.png?raw=true "ocr_this")
- run snip_to_text.py on local machine, -i flag is png image, -o is output file
```
(ocr) cas@ubuntu:~/working_dir/python_ocr$ python snip_to_text.py -i mp3_chars.png -o mp3_chars_out.txt
```
(ocr) cas@ubuntu:~/working_dir/python_ocr$ python print_utf.py
```

```
