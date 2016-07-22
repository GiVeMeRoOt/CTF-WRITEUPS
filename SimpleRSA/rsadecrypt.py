#!/usr/bin/env python

p = 238324208831434331628131715304428889871

q = 296805874594538235115008173244022912163

c = 29846947519214575162497413725060412546119233216851184246267357770082463030225

e = 3

N = 70736025239265239976315088690174594021646654881626421461009089480870633400973

assert p * q == N
print "P: %s" % p
print "Q: %s" % q

# ./rsatool -p <value for p> -q <value for q>   And also dont forget to change the value of DEFAULT_EXP to the value of e given in the question
d = 0x68421d449e2537580b2b44e56233fdf7dc35facafb5c928e9eb427213439b493

print "D: %s" % d

decrypted = pow(c, d, N)
flag = hex(decrypted)[2:-1].decode("hex")
print flag
																																																																																						
