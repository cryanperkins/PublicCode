__author__ = 'student'
#Create a program to find all prime numbers up to a given number n.
#first find if divisible by 2, then 3, then 5, then 7, and continuing on to n.  The numbers not divisible by any number but itself are prime.
#to do - make it so that the numbers 2, 3, 5, and 7 are inserted properly.

n = input("Choose a number greater than 1.")

#print ("2\n3\n5\n7\n")

primes = [2, 3, 5, 7, 11, 13, 17, 19]

for i in range(8, n + 1):

    if i % 2 != 0:
        if i % 3 != 0:
            if i % 5 != 0:
                if i % 7 != 0:
                    if i % 11 != 0:
                        if i % 13 != 0:
                            if i % 17 != 0:
                                if i % 19 != 0:
                                    primes.append(i)

print(primes)

#create program so that it inserts prime numbers into the spot after % so that it would run up to any number
"""
we should have:
 2  |  3  |  5  |  7  |  11  |  13  |  17  |  19
|  23  |  29  |  31  |  37  |  41  |  43  |  47  |  53  |  59  |  61  |  67  |
 71  |  73  |  79  |  83  |  89  |  97  |  101  |  103  |  107  |  109  |  113  |
   127  |  131  |  137  |  139  |  149  |  151  |  157  |  163  |  167  |  173
 179  |  181  |  191  |  193  |  197  |  199  |  211  |  223  |  227  |  229
 233  |  239  |  241  |  251  |  257  |  263  |  269  |  271  |  277  |  281  |
283  |  293  |  307  |  311  |  313  |  317  |  331  |  337  |  347  |  349  |
353  |  359  |  367  |  373  |  379  |  383  |  389  |  397  |  401  |  409  |
419  |  421  |  431  |  433  |  439  |  443  |  449  |  457  |  461  |  463
467  |  479  |  487  |  491  |  499  |  503  |  509  |  521  |  523  |
 541  |  547  |  557  |  563  |  569  |  571  |  577  |  587  |  593  |
599  |  601  |  607  |  613  |  617  |  619  |  631  |  641  |  643
 |  647  |  653  |  659  |  661  |  673  |  677  |  683  |  691  |
 701  |  709  |  719  |  727  |  733  |  739  |  743  |  751  |  757
 |  761  |  769  |  773  |  787  |  797  |  809  |  811  |  821  |
                    823  |  827  |  829  |  839  |  853  |  857  |
  859  |  863  |  877  |  881  |  883  |  887  |  907  |  911  |  919  |  929  |  937  |  941  |  ...   (168  primes)(25  primes)
"""

"""
primes = [2, 3, 5, 7, 11, 13, 17, 19, ]

    for j in primes:
        if i % j == 0:
            break
        else:
            primes.append(i)
            break
"""