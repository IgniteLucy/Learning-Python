from string import digits,ascii_letters,punctuation

for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                print(i,j,k,l)

# way longer but very fast to get
#for i in ascii_letters:
 #   for j in ascii_letters:
  #      for k in ascii_letters:
   #         for l in ascii_letters:
    #            print(i,j,k,l)


# way longer but very fast to get
#for i in ascii_letters + digits + punctuation:
 # for j in ascii_letters + digits + punctuation:
  #      for k in ascii_letters + digits + punctuation:
   #         for l in ascii_letters + digits + punctuation:
    #            print(i,j,k,l)

book = 'my book'
pages = 200
print(7 + 3)
print(10 - 5)
print(5 * 3)
print(10 / 2)