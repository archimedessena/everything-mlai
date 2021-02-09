#list mutability
kofi = "His "
#kofi = "s" + kofi[1]

ans = [34, 5, 67, 48, 90]

#print(dir(kofi))(ans.sort())




#an = ans.index(48)
#if an == 3:
#    index(48) = va
#    print("That is what a want")
#else:
#    print("Not interested")


#print(kofi[-1])

# example of operator overloading
#dir(of a variabele or whatever print all the operator overloading)
#kofi = kofi. __add__("Customizing")
#print(kofi)


# Pattern matching
#import re
#match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
#match.group(1)
#print(match.group(1))


# sequence operation
L = [123, 'spam', 1.23]
#v =len(L) # number of items
#print(v ** 4)
L.append('NI') # growing a list
#print(L)
#print(L[:-1])
L.pop() # deleting the last item in the list

#print(L)
#L[1] = 34
#x, y, z = L 
#print(x, y, z)
#k = [1.., 99]
#print(k)

# Bounds checking
#print(L[99])


# Nesting in list, you can nest a tuple inside a list, which also be nested in a dictionary which can also be nested into a list and so on
k= [[1, 2, 3], # A 3 × 3 matrix, as nested lists
    [4, 5, 6],      # Code can span lines if bracketed
    [7, 8, 9]]

#print(M[2][2])
# List comprehension
#for i in M:
    #print(i[2])
    #for a in i:
        #print(a)


M = [[10, 12, 13], # A 3 × 3 matrix, as nested lists
    [14, 15, 16],      # Code can span lines if bracketed
    [17, 18, 19]]
## Collecting the diagonal of the matrix
#j = [M[i][i] for i in [0, 1, 2]]
#print(j)

#v = [ 3, 4, 5, 6, 7, 8]
#k = [i ** 2 for i in v]
#print(k)


#num = list(range(4))
#print(num)
#y = list(range(-6, 7, 2)) # list comprehension

#print(y)


#print(num)
#y = list(range(-6, 7, 2)) # list comprehension
#print(y)

#z = [[i * 2, i ** 3] for i in y if i > 4] # if filter
#print(z)


#t = [[b / 4, b + 5] for b in y if b <= 4]
#print(t)

#nums = (sum(b) for b in k) # summing row of a matrix
#print(next(nums))
#print(next(nums))
#print(next(nums))

#g = list(map(sum, k)) # Map sum over items in M
#print(g)

#numss = list(range(10))
#a = max(numss)
#print(a)
#n = sum(numss)
#print(n)

#h = list(map(sum, M))
#print(h)


#p = {i: sum(M[i]) for i in range(3)} # Creates key/value table of row sums
#print(p)



#h = [ord(x) for x in 'spaam'] # List of character ordinals
#print(h)

#n= {ord(x) for x in 'a'} # Sets remove duplicates
#print(n)

#s = {x: ord(x) for x in 'spaam'} # Dictionary keys are unique


#print(s)

#List summaring
#Operation Interpretation
#L * 3
#for x in L: print(x)
#3 in L
#Iteration, membership
#L.append(4)
#L.extend([5,6,7])
#L.insert(i, X)
#Methods: growing
#L.index(X)
#L.count(X)
#Methods: searching
#L.sort()
#L.reverse()
#L.copy()
#L.clear()
#Methods: sorting, reversing,
#copying (3.3+), clearing (3.3+)
#L.pop(i)
#L.remove(X)
#del L[i]
#del L[i:j]
#L[i:j] = []
#Methods, statements: shrinking
#L[i] = 3
#L[i:j] = [4,5,6]
#Index assignment, slice assignment
#L = [x**2 for x in range(5)]
#list(map(ord, 'spam'))
#List comprehensions and maps





        #DICTIONARIES
name_and_dob = {
    'Cee': 1992,
    'Eli': 1996,
     'Archimedes': 1988,
     'Godsway': 2002,
     'Bed': 1000 
}

#print(an['favorite_food'][0])
#print(an["location"][0].append('Lashibi'))

#for i in an:
#    for a in an[i]:
#        print(a)

#(name_and_dob['Eli']) = 2002
#print(name_and_dob)

#rec['jobs'].append('janitor')


#n = list(name_and_dob.keys())
#n.sort()
#print(n)
#for key in n:
#    print(key, '=>', n[key])
#for key in Ks: # Iterate though sorted keys
    #print(key, '=>', D[key])

# The above code involve three steps but with the newer version is just one step
#for i in sorted(name_and_dob):
#    print(i, name_and_dob[i])


# iteration and optimization
#squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
#print(squares)


#squares = []
#for x in [1, 2, 3, 4, 5]:   # This is what a list comprehension does
#    squares.append(x ** 2)      # Both run the iteration protocol internally
#print(squares)


# Time and timeit modules help in determining the speed of your code




                        # TUPLES are immutable
#T = (1, 2, 3, 4)         # A 4-item tuple
#len(T)               # Length
#v = T + (5, 6)       # Concatenation
#print(v)
#(1, 2, 3, 4, 5, 6)
#print(T[0])             # Indexing, slicing, and more
#
## count and index
#print(T.index(4))
#print(T.count(3))
#
#T = (2,) + T[1:] # Make a new tuple for a new value


#T = (5,) + T[2:] #concatenation
#print(T)

# Tuples support mixed types but can never grow or shrink



                # FILES
 #f = open('data.txt', 'w')   # Make a new file in output mode ('w' is write)
 #f.write('Hello\n')          # Write strings of characters to i
 #f.write('world\n')          # Return number of items written in Python 3.
 #f.close()                   # Close to flush output buffers to disk

#with open('arc.txt', 'w') as t:
#    t.write("Hello World")
#print(t)
#t.close() 

# read(read lines), seek(a particular position), for loop can also be used to read each line in the written text

#for line in open('arc.txt'): print(line)

#dir(t)
#help(t.seek)

# Revisit binary bytes files


##SET
#q = set("Archimedes") # making a set out of a sequence
#for i in sorted(q):
#    print(i)
#r = {'cat'} #'goat', 'fish', 'cat'} # making set using set literals
#v = q, r
#print(v)
#print(v[0])

#print(q, r)


# intersection
#X = {1, 3, 5} # Make a set out of a sequence in 2.X and 3.X
#Y = {2, 3, 4, 5, }
#
#print(X & Y)

# UNION
#print(X | Y)
## Difference
#print(X - Y)
#print(Y-X)
# superset
#print(Y > X)


# Set comprehension
#{k ** 2 for k in [1, 2, 4, 6]}
#print(k)
#
#b = {n ** 2 for n in [1, 2, 3, 4]}
#print(b)



#list(set([1, 2, 1, 3, 1])) # Filtering out duplicates (possibly reordered)

# Other core types

#import decimal # Decimals: fixed precision
#d = decimal.Decimal('3.141')
#print(d + 3)
#
#decimal.getcontext().prec = 2
#decimal.Decimal('1.00') / decimal.Decimal('3.00')


#from fractions import Fraction # Fractions: numerator+denominator
#f, v, r = Fraction(2, 3), Fraction(5, 3), Fraction(7, 9)
#t, b = v * r - f + v, v * r
#print(b)
#print(t)
#
#print(type(f))
#
#print(isinstance(f, Fraction)) # Object-oriented tests




#           NUMERIC TYPES
#Expression operators
#+, -, *, /, >>, **, &, etc.
#Built-in mathematical functions
#pow, abs, round, int, hex, bin, etc.
#Utility modules
#random, math, etc.


#Operators Description page 189
#yield x Generator function send protocol
#lambda args: expression Anonymous function generation
#x if y else z Ternary selection (x is evaluated only if y is true)
#x or y Logical OR (y is evaluated only if x is false)
#x and y Logical AND (y is evaluated only if x is true)
#not x Logical negation
#x in y, x not in y Membership (iterables, sets)
#x is y, x is not y Object identity tests
#x < y, x <= y, x > y, x >= y
#x == y, x != y
#Magnitude comparison, set subset and superset;
#Value equality operators
#x | y Bitwise OR, set union
#x ^ y Bitwise XOR, set symmetric difference
#x & y Bitwise AND, set intersection
#x << y, x >> y Shift x left or right by y bits
#x + y
#x – y
#Addition, concatenation;
#Subtraction, set difference
#x * y
#x % y
#x / y, x // y
#Multiplication, repetition;
#Remainder, format;
#Division: true and floor
#−x, +x Negation, identity
#˜x Bitwise NOT (inversion)
#x ** y Power (exponentiation)
#x[i] Indexing (sequence, mapping, others)
#x[i:j:k] Slicing
#x(...) Call (function, method, class, other callable)
#x.attr Attribute reference
#(...) Tuple, expression, generator expression
#[...] List, list comprehension
#{...} Dictionary, set, set and dictionary comprehensions


# Numeric types
#a + 1, a − 1 # Addition (3 + 1), subtraction (3 − 1)
#(4, 2)
#b * 3, b / 2 # Multiplication (4 * 3), division (4 / 2)
#(12, 2.0)a % 2, b ** 2 # Modulus (remainder), power (4 ** 2)
#(1, 16)
#2 + 4.0, 2.0 ** b # Mixed-type conversions
#(6.0, 16.0)





# floor vs truncation
#import math
#math.floor(2.5) # Closest number below value
##2
#math.floor(-2.5)
##-3
#math.trunc(2.5) # Truncate fractional part (toward zero)
###2
#math.trunc(-2.5) # -3

#import math
#5 / float(−2) # Remainder in 2.X
#−2.5
#5 / −2, 5 // −2 # Floor in 2.X
#(−3, −3)
#math.trunc(5 / float(−2)) # Truncate in 2.X
#−2

# Complex numbers
#v = 8 + 5j
#print(v* 3)


# hexadecimal, octal, binary  page 200


# OTHER BUILT IN NUMBERIC TOOLS
import math
math.pi, math.e # Common constants
#(3.141592653589793, 2.718281828459045)
math.sin(2 * math.pi / 180) # Sine, tangent, cosine
#0.03489949670250097
math.sqrt(144), math.sqrt(2) # Square root
#(12.0, 1.4142135623730951)
pow(2, 4), 2 ** 4, 2.0 ** 4.0 # Exponentiation (power)
#(16, 16, 16.0)
abs(-42.0), sum((1, 2, 3, 4)) # Absolute value, summation
#(42.0, 10)
min(3, 1, 2, 4), max(3, 1, 2, 4) # Minimum, maximum
#(1, 4)

a, b, c = 2, 3, 4
#d = math.sqrt((a**2) - (4*b*c))/(2*b)
#print(d)
#print(math.sin(60))



##print(math.sqrt(3456789)) # module
#print(pow(12, .5))


# RANDOM MODULE = random integers, floats, choices, shuffles
import random
v = (random.random()) # displaying numbers btn 0 and 1
c = v * 100
#print(c)

#print(random.randint(1, 90)) # select integers at random

# this selects from a list at random not integers
#print(random.choice(["Mango", "Apple", "Orange"]))

d = ["Mango", "Apple", "Orange"] 
random.shuffle(d) # Rearrange the items according to alphabet
#print(d)


from decimal import Decimal
#q = Decimal(30.9) + Decimal(45.990)
#print(q)

#decimal.getcontext().prec = 2
 #print(pay)


#import decimal
#decimal.Decimal('1.00') / decimal.Decimal('3.00')
#Decimal('0.3333333333333333333333333333')
#
#with decimal.localcontext() as ctx:
#    ctx.prec = 2
#decimal.Decimal('1.00') / decimal.Decimal('3.00')
#
#Decimal('0.33')
#
#decimal.Decimal('1.00') / decimal.Decimal('3.00')
#Decimal('0.3333333333333333333333333333')



from fractions import Fraction
#def adds():
#    g = Fraction(2, 3) + Fraction(9, 11)
#    return g
#
#c = Fraction(2, 5) / Fraction(3,  6) 
#def div(adds=None):
#    if adds == Fraction(49, 33):
#       d = c + adds
#    return d
#
#
#print(adds())
#print(div())


# Fractions can be created using floating point
from decimal import Decimal
#p = Fraction(0.34) + Fraction(5.88)


p = 21.5 .as_integer_ratio() # float object
#print(p)

y = 6.9
h = Fraction(*y.as_integer_ratio())  #Convert float -> fraction: two args, same as fraction
#print(h)

# convert fraction to decimal
#g = Fraction(5, 2)
#i = (float(g))
#print(i)
#k = i.as_integer_ratio()
#print(k)

# SET
u = set([4, 6, 7, 8, 9, 4])
#u.add(5)
#print(u)
#
#y = set([11, 45, 5, 4, 7])
## intersection
#k = u & y
#print(k)

# union
#c = u | y
#print(c)
#
## difference
#t = u - y
#print(t)
#p = y - u
#print(p)

# initializing an empty set
#q = set()

# some other ways of writing it
#c = u.union(y)
#print(c)
#g = u.intersection(y)
#print(g)
#print(u.difference(y))
#print(u.issubset(y))



y = set([11, 45, 5, 4, 7])
#y.add((2, 4, 5, 6, 6))
#print(y)
#
#if 450 in y:
#    print("Available")
#else:
#    print("Not Available")


# set comprehension
#h = {x**2 for x in y }
#print(h)

# Removal of duplicates
# first create the list and give it to a set
#r = [1, 2, 3, 5, 6, 6, 7, 5, 2, 2, 2, 4, 5]
#t = set(r)
#print(t)
#k = list(t)
#print(k)

# list of set of strings
#j = list(set(("a", "g", "b")))
#print(j)


#engineers = {'bob', 'sue', 'ann', 'vic'}
#managers = {'tom', 'sue'}
#v = 'bob' in engineers
#print(v)

# all set properties can be used on normal daily life questions as well




#n = 27
#print(pow(n, 3))
#import math
#from fractions import Fraction
#print(math.sqrt(64))
#print(125 ** .334)
#print(pow(n, Fraction(2, 3)))


#math.trunc()
#math.round()
#math.floor()
#math.ceil()
#math.factorial()
#math.cos()
#math.sin()
#math.log()
#math.radians()
#math.exp()
#math.fabs
#math.hypot()



#A = ["spam"]
#B = A[:]
#print(B)
#B[0] = "shrubbery"
#print(A)

# STRINGS

#Operation Interpretation
#S = '' Empty string
#S = "spam's" Double quotes, same as single
#S = 's\np\ta\x00m' Escape sequences
#S = """...multiline...""" Triple-quoted block strings
#S = r'\temp\spam' Raw strings (no escapes)
#B = b'sp\xc4m' Byte strings in 2.6, 2.7, and 3.X (Chapter 4, Chapter 37)
#U = u'sp\u00c4m' Unicode strings in 2.X and 3.3+ (Chapter 4, Chapter 37)
#S1 + S2
#S * 3
#Concatenate, repeat
#S[i]
#S[i:j]
#len(S)
#Index, slice, length
#"a %s parrot" % kind String formatting expression
#"a {0} parrot".format(kind) String formatting method in 2.6, 2.7, and 3.X
#S.find('pa')
#S.rstrip()
#S.replace('pa', 'xx')
#S.split(',')
#String methods (see ahead for all 43): search,
#remove whitespace,
#replacement,
#split on delimiter,


#Operation Interpretation
#S.isdigit()
#S.lower()
#S.endswith('spam')
#'spam'.join(strlist)
#S.encode('latin-1')
#B.decode('utf8')
#content test,
#case conversion,
#end test,
#delimiter join,
#Unicode encoding,
#Unicode decoding, etc. (see Table 7-3)
#for x in S: print(x)
#'spam' in S
#[c * 2 for c in S]
#map(ord, S)
#Iteration, membership
#re.match('sp(.*)am', line) Pattern matching: library module





#Escape Meaning
#\newline Ignored (continuation line)
#\\ Backslash (stores one \)
#\' Single quote (stores ')
#\" Double quote (stores ")
#\a Bell
#\b Backspace
#\f Formfeed
#\n Newline (linefeed)
#\r Carriage return
#\t Horizontal tab
#\v Vertical tab
#\xhh Character with hex value hh (exactly 2 digits)
#\ooo Character with octal value ooo (up to 3 digits)
#\0 Null: binary 0 character (doesn’t end string)
#\N{ id } Unicode database ID
#\uhhhh Unicode character with 16-bit hex value
#\Uhhhhhhhh Unicode character with 32-bit hex valuea
#\other Not an escape (keeps both \ and other)





# STRINGS IN ACTION
#v = 'neat ' + 'work' # concentenation
#print(v)
#
#football = 'Mathematics'
#vo = ([b for b in football if len(football)>=2])
#print(vo, end=' ')


# slicing
slice_ = [19, 2, 5, 40, 5, 'Machined Learning', 6, 7, 'Goals']
sli = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#print(slice_[2: 4])
#print(slice_[2:])
#print(slice_[:])
#print(slice_[-2])
#print(slice_[-4])
#print(slice_[:-4])
#print(sli[3:19:2])
#print(sli[::2])
#print(sli[::-3]) # reversed
#print(sli[3:1:-3]) # reversed
#[slice(1, 3)]

#for i in range(len(slice_)):
#    print(slice_[i], end=' ')
#    print(i)




# STRING CONVERSION TOOLS
# int, str, repr
#v = str('45')
#print(v)


#B = '1101' # Convert binary digits to integer with ord
#I = 0
#while B != '':
#    I = I * 2 + (ord(B[0]) - ord('0')) # not clear
#    B = B[1:]
   

 


#print(int('5467', 9)) # Convert binary to integer: built-in
#
#print(bin(2871)) # convert integer to binary 

S = 'spam'
#S = S + 'SPAM!' # To change a string, make a new one
#S = S[-1] + 'Burger' 
#print(S)

# you can call replace on strings
#v = S.replace('sp', 'y')
#print(v)

# Call methods on objects
#f = 'I love  {}'.format('Archimedes') # format method
#print(f.upper())


#j = f.find('Arch')
#print(j)


# STRING METHODS
#S.capitalize()
#S.casefold() 
#S.lower()
#S.center(width [, fill])
#S.count(sub [, start [, end]])
#S.encode([encoding [,errors]])
#S.endswith(suffix [, start [, end]])
#S.expandtabs([tabsize])
#S.find(sub [, start [, end]])
#S.format(fmtstr, *args, **kwargs)
#S.index(sub [, start [, end]])
#S.isalnum()
#S.isalpha()
#S.isdecimal()
#S.lstrip([chars])
#S.maketrans(x[, y[, z]])
#S.partition(sep)
#S.replace(old, new [, count])
#S.rfind(sub [,start [,end]])
#S.rindex(sub [, start [, end]])
#S.rjust(width [, fill])
#S.rpartition(sep)
#S.rsplit([sep[, maxsplit]])
#S.rstrip([chars])
#S.split([sep [,maxsplit]])


#S.isdigit()
# S.splitlines([keepends])
#S.isidentifier() 
#S.startswith(prefix [, start [, end]])
#S.islower() 
#S.strip([chars])
#S.isnumeric() 
#S.swapcase()
#S.isprintable() 
#S.title()
#S.isspace() 
#S.translate(map)
#S.istitle() 
#S.upper()
#S.isupper() 
#S.zfill(width)
#S.join(iterable)

# slicing with method
#q = 'painful'
#q = 'painful'
#t = q[:1] + 'eace' + q[4:]
#print(t)

#S = 'xxxxSPAMxxxxSPAMxxxx'
#where = S.find('SPAM') # Search for position
#where # Occurs at offset 4
#S = S[:where] + 'EGGS' + S[(where+4):]
#print(S)

#h = list(t) # changing a string to list
#print(h)
## After that you can mutate it and change it back to string
## using join
#h[4] = 'ee'
#print(h)
#g = ''.join(h)
#print(g)



# split method
ko = "manager has enough time"
#p = ko.split(' ') 
#c = ''.join(ko)
#print(c)
#print(p)

# other string method
#print(ko.rstrip())

#print(ko.isalpha()) # Is this alpha
#print(ko.endswith('time')) # does it end with time? which is true
#print(ko.startswith('man')) # does it start with man? which is true the answers are always boolean value
#h = ko.find('time') !=1 # check if the time is at the end of the statement
#print(h)

g = ko[-len(ko):] == ko
print(g)


# string substitution page 270 to be looked at again


#Code Meaning
#s String (or any object’s str(X) string)
#r Same as s, but uses repr, not str
#c Character (int or str)
#d Decimal (base-10 integer)
#i Integer
#u Same as d (obsolete: no longer unsigned)
#o Octal integer (base 8)
#x Hex integer (base 16)
#X Same as x, but with uppercase letters
#e Floating point with exponent, lowercase
#E Same as e, but uses uppercase letters
#f Floating-point decimal
#F Same as f, but uses uppercase letters
#g Floating-point e or f
#G Floating-point E or F
#% Literal % (coded as %%)




somelist = list('SPAM')
r = '{0[2]}'.format(somelist)
print(r)


#somelist = list('SPAM')
#somelist
#['S', 'P', 'A', 'M']
#'first={0[0]}, third={0[2]}'.format(somelist)
#'first=S, third=A'
#'first={0}, last={1}'.format(somelist[0], somelist[-1]) # [-1] fails in fmt
#'first=S, last=M'
#parts = somelist[0], somelist[-1], somelist[1:3] # [1:3] fails in fmt
#'first={0}, last={1}, middle={2}'.format(*parts) # Or '{}' in 2.7/3.1+
#"first=S, last=M, middle=['P', 'A']"


# Advanced formatting string method to be looked at later page 276 - 290



#Operation Interpretation


# List and dictionary
#L * 3
#for x in L: print(x)
#3 in L
#Iteration, membership
#L.append(4)
#L.extend([5,6,7])
#L.insert(i, X)
#Methods: growing
#L.index(X)
#L.count(X)
#Methods: searching
#L.sort()
#L.reverse()
#L.copy()
#L.clear()
#Methods: sorting, reversing,
#copying (3.3+), clearing (3.3+)
#L.pop(i)
#L.remove(X)
#del L[i]
#del L[i:j]
#L[i:j] = []
#Methods, statements: shrinking
#L[i] = 3
#L[i:j] = [4,5,6]
#Index assignment, slice assignment
#L = [x**2 for x in range(5)]
#list(map(ord, 'spam'))



# List in action
# str([1, 2]) + "34" # Same as "[1, 2]" + "34"
#'[1, 2]34'
#[1, 2] + list("34") # Same as [1, 2] + ["3", "4"]
#[1, 2, '3', '4']

l = [2, 4, 6, 8]
print(8 in l)


# list comprehension
res = [c * 4 for c in 'SPAM']
print(res)
f = [i * 2 for i in l]
print(f)

#print(list(map(abs, [−1, −2, 0, 1, 2])))

h = [1, 23]
h[:0] = [2, 4, 7]
h.append(list(set('Archimedes')))
print(h)


#L = ['abc', 'ABD', 'aBe']
#sorted(L, key=str.lower, reverse=True) # Sorting built-in
#['aBe', 'ABD', 'abc']
#L = ['abc', 'ABD', 'aBe']
#sorted([x.lower() for x in L], reverse=True) # Pretransform items: differs!
#['abe', 'abd', 'abc']

# other functions reverse, reversed, append, extend, 
#L = [1, 2]
#L.extend([3, 4, 5]) # Add many items at end (like in-place +)
#L
#[1, 2, 3, 4, 5]
#L.pop() # Delete and return last item (by default: −1)
#5
#L
#[1, 2, 3, 4]
#L.reverse() # In-place reversal method
#L
#[4, 3, 2, 1]
#list(reversed(L)) # Reversal built-in with a result (iterator)
#[1, 2, 3, 4]


#L = ['spam', 'eggs', 'ham']
#L.index('eggs') # Index of an object (search/find)
#1
#L.insert(1, 'toast') # Insert at position
#L
#['spam', 'toast', 'eggs', 'ham']
#L.remove('eggs') # Delete by value
#L
#['spam', 'toast', 'ham']
#L.pop(1) # Delete by position
#'toast'
#L
#['spam', 'ham']
#L.count('spam') # Number of occurrences
#1

#L = ['spam', 'eggs', 'ham', 'toast']
#del L[0] # Delete one item
#L
#['eggs', 'ham', 'toast']
#del L[1:] # Delete an entire section
#L # Same as L[1:] = []
#['eggs']


#L[i:j]=[] # A form of emptying a list
#L = ['Already', 'got', 'one']
#L[1:] = []
#L
#['Already']
#L[0] = []
#L
#[[]]


# dictionaries
#Operation Interpretation
#D = {} #Empty dictionary
#D = {'name': 'Bob', 'age': 40} #Two-item dictionary
#E = {'cto': {'name': 'Bob', 'age': 40}} #Nesting
#D = dict(name='Bob', age=40)
#D = dict([('name', 'Bob'), ('age', 40)])
#D = dict(zip(keyslist, valueslist))
#D = dict.fromkeys(['name', 'age'])
##Alternative construction techniques:
##keywords, key/value pairs, zipped key/value pairs, key lists
#D['name']
#E['cto']['age']
#Indexing by key
#'age' in D Membership: key present test
#D.keys()
#D.values()
#D.items()
#D.copy()
#D.clear()
#D.update(D2)
#D.get(key, default?)
#D.pop(key, default?)
#D.setdefault(key, default?)
#D.popitem()
#Methods: all keys,
#all values,
#all key+value tuples,
#copy (top-level),
#clear (remove all items),
#merge by keys,
#fetch by key, if absent default (or None),
#remove by key, if absent default (or error)
#fetch by key, if absent set default (or None),
#remove/return any (key, value) pair; etc.
#len(D) Length: number of stored entries
#D[key] = 42 Adding/changing keys
#del D[key] Deleting entries by key
#list(D.keys())
#D1.keys() & D2.keys()

#D.viewkeys(), D.viewvalues() Dictionary views (Python 2.7)
#D = {x: x*2 for x in range(10)} Dictionary comprehensions (Python 3.X, 2.7)

#D.get('spam') # A key that is there

#D
#{'eggs': 3, 'spam': 2, 'ham': 1}
#D2 = {'toast':4, 'muffin':5} # Lots of delicious scrambled order here
#D.update(D2)
#D
#{'eggs': 3, 'muffin': 5, 'toast': 4, 'spam': 2, 'ham': 1}


#table = {'Holy Grail': '1975', # Key=>Value (title=>year)
#'Life of Brian': '1979',
#'The Meaning of Life': '1983'}
##year = '1983'
##movie = table[year]
#
#list(table.items()) # Value=>Key (year=>title)
##[('The Meaning of Life', '1983'), ('Holy Grail', '1975'), ('Life of Brian', '1979')]
##print(list(table.items())
##[title for (title, year) in table.items() if year == '1975']
##print(title)
#
#
#v = '1975'
#[key for (key, value) in table.items() if value == V] # Value=>Key
#
#[key for key in table.keys() if table[key] == V]

#print(key, value)
# Left off at page 310
# Dictionary usage notes




# an interesting way of creating a dictionary
#Matrix = {}
#Matrix[(2, 3, 4)] = 88
#Matrix[(7, 8, 9)] = 99
#X = 2; Y = 3; Z = 4 # ; separates statements: see Chapter 10
#Matrix[(X, Y, Z)]
#
#if (2, 3, 6) in Matrix: # Check for key before fetch
#    print(Matrix[(2, 3, 6)]) # See Chapters 10 and 12 for if/else
#else:
#    print(0)
#try:
#    print(Matrix[(2, 3, 6)]) # Try to index
#except KeyError: # Catch and recover
#    print(0) # See Chapters 10 and 34 for try/except
#
#Matrix.get((2, 3, 4), 0) # Exists: fetch and return
#
#Matrix.get((2, 3, 6), 0) # Doesn't exist: use default arg

#print(Matrix)

v = {}
v[(4, 5, 6)] = 4
v[(4, 5, 8)] = 45
print(v)
p = v.keys()
print(p)

# other forms of creating dictionary
#{'name': 'Bob', 'age': 40} # Traditional literal expression
#D = {} # Assign by keys dynamically
#D['name'] = 'Bob'
#D['age'] = 40
#dict(name='Bob', age=40) # dict keyword argument form
#dict([('name', 'Bob'), ('age', 40)]) # dict key/value tuples form


#dict(zip(keyslist, valueslist)) # Zipped key/value tuples form (ahead)


#dict.fromkeys(['a', 'b'], 0)
#{'a': 0, 'b': 0}

r = dict.fromkeys([b, c], 12)
print(r)



#>>> D = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
#>>> D['name']
#'Bob'
#>>> D['jobs'].remove('mgr')
#>>> D
#{'jobs': ['dev'], 'age': 40.5, 'name': 'Bob'}



# sets working same like dictionary
#>>> D = {}
#>>> D['state1'] = True # A visited-state dictionary
#>>> 'state1' in D
#True
#>>> S = set()
#>>> S.add('state1') # Same, but with sets
#>>> 'state1'


#Dictionary comprehension
#v = list(zip(['a', 'b', 'c'], [2, 4, 6])) # zip together keys and values
#print(v)
#
## creating a dictionary out of a list
#c = dict(zip(['b', 'c', 'h'], [34, 56, 78]))
#d = [x for x in c]
#print(d)
#print(c)

# the above code can also be written as 
#c = {k: v for (k, v) in zip(['x', 'r', 'y'], [1, 2, 3])}
#print(c)
#




#l = list(zip([ 2, 4, 5], ['a', 'b', 'c']))
#print(l)
#g = dict(zip([ 2, 4, 5], ['a', 'b', 'c']))
#print(g)

#t = {v: y for (v,  y) in zip([4, 7, 9], ['u', 'm', 'p'])}
#print(t)


# more interesting examples
#r = {h: h**3 for h in range(1, 5)}
#print(r)

#g = {n*3: m*2  for (n, m) in zip([3, 4, 5], [10, 20, 30])}
#print(g)

D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)



left off page 318







