try:  # versucht den Code-Block auszufuehren
	print(x)
except:  # falls der try-Block einen Error verursacht wird der except-Block ausgefuehrt
	print("x nicht definiert")

x = 3
try:
	print('mit raise kann man selber einen Error verursachen')
	if x == 1:
		raise ValueError  # raise gibt uns die moeglichkeit selbst einen Fehler auszuloesen
	elif x == 2:
		raise ZeroDivisionError
	else:
		raise WindowsError
except ValueError:  # es koennen auch mehrere except blocke definiert werden dazu muss man der error type hinschreiben
	print("Value error")
except ZeroDivisionError:
	print('divison null')
except:  # wenn kein Error angegeben wird werden alle nicht zuvor abgefangenen errors abgefangen
	print('Alle anderen Fehler')

# try:
# 	#
# 	pass
# # print(x)
# except Exception as error:
# 	# Es konnen mehrere except statements geschreiben werden. Diese mussen einen error typ zugewiesen werden
# 	# https://docs.python.org/3/library/exceptions.html
# 	# https://www.tutorialsteacher.com/python/error-types-in-python
# 	print(type(error).__name__)
# else:  # der else block wird ausgefuehrt wenn kein Error verursacht wurde
# 	pass
# finally:  # der finally block wird immer ausgefuehrt
# 	pass
