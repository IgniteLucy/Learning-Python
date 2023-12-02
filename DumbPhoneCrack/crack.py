from string import digits,ascii_letters,punctuation 
# importing numbers, a-z A-Z and !@#$%^&*()_-= .  ... and so on 

for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                print(i,j,k,l)


# will go through a loop of numbers
# 0 0 0 0
# 0 0 0 1
# 0 0 0 2
# ...

# way longer but very fast to get
#for i in ascii_letters:
 #   for j in ascii_letters:
  #      for k in ascii_letters:
   #         for l in ascii_letters:
    #            print(i,j,k,l)
#Same but letters a-z A-Z

# way longer but very fast to get
#for i in ascii_letters + digits + punctuation:
 # for j in ascii_letters + digits + punctuation:
  #      for k in ascii_letters + digits + punctuation:
   #         for l in ascii_letters + digits + punctuation:
    #            print(i,j,k,l)
#All 4 combination with NUMBER,a-zA-Z[]

#giving something a value 
book = 'my book'
pages = 200


 
print(book + "has about " + str(pages) + " pages")
print(7 + 3)
print(10 - 5)
print(5 * 3)
print(10 / 2)

