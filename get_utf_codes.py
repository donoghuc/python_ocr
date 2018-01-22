with open("unicode_raw.txt", "r") as fo:
	string_1 = unicode(fo.read(),'utf-8')

with open("output_ocr.txt", "w") as fo:
	fo.write(repr(string_1))