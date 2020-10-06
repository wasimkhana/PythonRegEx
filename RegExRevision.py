import re
#Task-1: to find phone number
#text = "my phone number is 0342-9897620 and 0333-3422334"
#obj=re.compile(r"\d\d\d\d-\d\d\d\d\d\d\d")
#print(obj.search(text).group())     #output: 0342-9897620
#print(obj.findall(text))	     #output: ['0342-9897620','0333-3422334']


#Task-2: to detect brakets along numbers
#text = "my phone number is 0342-9897620 and 0333-3422334"
#obj=re.compile(r"(\d\d\d\d)-(\d\d\d\d\d\d\d)")
#print(obj.search(text).group(2))  #output: 0342
#print(obj.search(text).group())   #output: (0342) 	if obj=re.compile(r"\((\d\d\d\d)\)-\d\d\d\d\d\d") and text="(0342)-9897620


#Task-3: to detect the matching string
text = "I met Batman"
obj=re.compile(r"Bat(ball|khan|jan|mann)")
if(obj.search(text)):
   print("Batman")
else:
   print("Not Found")


#Task-4: use of ? symbol(means 0 or 1 time)
#text = "I met Batwoman"
#obj=re.compile(r"Bat(wo)?man")
#print(obj.search(text).group())    #it only detects Batman and Batwoman


#Task-5: use of * symbol(means 0 or many times)
#text = "I met Batwoman"
#obj=re.compile(r"Bat(wo)*man")
#print(obj.search(text).group())	   #it detects Batman and Batwoman and also Batman with many 'wo' inside


#Task-6: use of + symbol(means 1 or many times)
#text = "I met Batwoman"
#obj=re.compile(r"Bat(wo)+man")
#print(obj.search(text).group())    #it detects Batwoman and so on... but not Batman here 'wo' is must 1 and optional many times


#Task-7: use of {min,max} to constrint the number of times any word or symbol
#text = "My numbers 330-9994-777,432-3442-444,3442-234"
#obj=re.compile(r"((\d\d\d-)?\d\d\d\d-\d\d\d(,)?){1,3}")
#print(obj.search(text).group())   # it matches according to the given regix here first 3 digits are option and ',' is optional after number
				  # minimum 1 number and maximum 3 number is returned. else error


#Task-8: greedy approach
#text = "I met 9999999"
#obj=re.compile(r"\d{2,7}")
#print(obj.search(text).group()) # it detects the maximum till max if max is not defined like {2,} it will match upto infinity


#Task-9: non greedy approach
#text = "I met 9999999"
#obj=re.compile(r"\d{2,7}?")
#print(obj.search(text).group()) # it detects the minimum as per min defined if min is not defined then it will return empty


# use os square bracket is that you can make own class as [aeiou] will find the vowels in given text
# use of carrot with in class[] '^' means not forexample [^aeiou] will obtain all the symbols except the vowels
# r"1|2|3|4|5|6|7|8|9" is what \d mean

# the carrot '^' in roast r"^" detect the following charater as begining of setence else empty
# the dolor '$' detect the followed by character as an end of sentence if not found then empty
# the dot '.' symbol detect character before the given word e.g '.at' in " cat is at home' output: ['cat',' at'] one can use {3} after dot 



