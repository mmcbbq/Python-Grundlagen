
x = 2  #-> 0000 0010   -> 1111 1101 -> -0b11

y = -3 # 3 = 0000 0011  -> 1111 1100 +1 -> 1111 1101
# The complement operator (~) JUST FLIPS BITS. It is up to the machine to interpret these bits.
# https://stackoverflow.com/questions/791328/how-does-pythons-bitwise-complement-operator-tilde-work
print(~x)
print(y)