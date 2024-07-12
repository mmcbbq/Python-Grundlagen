# Schreibe ein Programm das die folgende Tabelle ausgibt

# Name    Alter    Ort
# --------------------
# Alice   25       New York
# Bob     30       London
# Tim     22       Paris

print("Name", "\tAlter", "\tOrt")
print("----------------------")
print("Alice", "\t25", "\t\tNew York")
print("Bob", "\t30", "\t\tLondon")
print("Tim", "\t22", "\t\tParis")

# Schreibe ein Programm das den folgenden Text ausgibt
# Twinkle, Twinkle, little star,
#		  How I wonder what you are!
#				Up above the world so high
#				Like a diamond in the sky
# Twinkle, Twinkle, little star,
#		  How I wonder what you are

print(""" Twinkle, Twinkle, little star,
		  How I wonder what you are!
				Up above the world so high
				Like a diamond in the sky
 Twinkle, Twinkle, little star,
		  How I wonder what you are""")

# Ändere folgenden Code das als ausgabe
# Hallo***Welt***ich---bin+++Bob
print("Hallo", "Welt", "ich", sep="***", end="---")
print("bin", "Bob", sep="+++")

# Printe den folgenden Pfeil mit so wenig Funktionts aufrufen wie möglich
#
print("""     *
    * *
   *   *
  *     *
 ***   ***
   *   *
   *   *
   *****""")
# Printe 2 Pfeile nebeneinander
# Tipp probiere mal "text" * 2
print("        *        " * 2)
print("       * *       " * 2)
print("      *   *      " * 2)
print("     *     *     " * 2)
print("    *       *    " * 2)
print("   ***     ***   " * 2)
print("      *   *      " * 2)
print("      *   *      " * 2)
print("      *   *      " * 2)
print("      *****      " * 2)

print("        *        " * 2, "       * *       " * 2, "      *   *      " * 2, "     *     *     " * 2,
	  "    *       *    " * 2, "   ***     ***   " * 2, "      *   *      " * 2, "      *   *      " * 2,
	  "      *   *      " * 2, "      *****      " * 2, sep="\n")

print('Hallo'*1000)