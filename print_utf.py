### NOTE: quick easy way of dealing with back slashes in text repr of unicode :)

import codecs


with codecs.open("unicode_out.txt", "w", "utf-8") as file:
    #### add your unicode repr between double quotes, careful for the back slash hell! 
	text = "(\uc870\uc120\ubbfc\uc8fc\uc8fc\uc758\uc778\ubbfc\uacf5\ud654\uad6d)_-_\uc560\uad6d\uac00"
	print(text)
	file.write(text)
