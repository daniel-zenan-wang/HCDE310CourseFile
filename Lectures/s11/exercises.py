#### Exercises ##############
## sample data for exercises
from posix import lstat
lst = [1, 2, 3, 4, 5]
movie_dicts = [{'title':'A Boy and His Dog', 'year':1975, 'rating':6.6},
               {'title':'Ran', 'year':1985, 'rating': 8.3},
               {'title':'True Grit', 'year':2010, 'rating':8.0},
               {'title':'Scanners', 'year':1981, 'rating': 6.7}]

### (1) List comprehensions
print '\nlist comprehensions\n------------'
## code and print out the following:

# (a) a list comprehension that adds 2 to each element of lst
#     so that you get [3,4,5,6,7] as the new list
lstPlus = [x + 2 for x in lst]
print lstPlus
# (b) a list comprehension that converts each element of lst to a string
#     so that you get ["1","2","3","4","5"] as the new list
lstStr = [str(x) for x in lst]
print lstStr


# (c) a list comprehension that generates the following from lst:
#    ['number 1', 'number 2', 'number 3', 'number 4', 'number 5']
lstNum = ['number ' + str(x) for x in lst]
print lstNum

# (d) a list comprehension that extracts a list of titles from movie_dict.
#    store the result in a variable called movie_titles and print it.
#    you should get something like (but order may vary!):
#    ['A Boy and His Dog', 'Ran', 'True Grit', 'Scanners']
# movie_titles = "["
# for item in movie_dicts:
#     movie_name = item['title']
#     
#     movie_titles = movie_titles + movie_name + ', '
# print movie_titles
movie_titles = [item['title'] for item in movie_dicts]
print movie_titles
# (e) a list comprehension that extracts makes a list of strings of movies
#     and years from the movie dicts. you should get.
#     store the result in a variable called movieyears and print it.
#     ['A Boy and His Dog (1975)', 'Ran (1985)', 'True Grit (2010)', 'Scanners (1981)']
#      (again, order may vary!)

movie_years = [item['title'] + '(' + str(item['year']) + ')' for item in movie_dicts]
print movie_years
### (2) Sorting
## use sorted() to code and print out the following:

print '\nsorting a list of strings in alphabetical order\n------------'
# (a.i) sort movie_titles in alphabetical order
new_movie_titles = sorted(movie_titles)
print new_movie_titles

# (a.ii) sort movie_titles in reverse alphabetical order
reverse_movie_titles = sorted(movie_titles, reverse = True)
print reverse_movie_titles

print '\nsorting a list of strings by number of characters\n------------'
# (b.i) sort movie_titles by number of characters in the title
#       so that the shortest titles appear at the front of the list
# len_movie_titles = sorted(movie_titles, key = len)
len_movie_titles = sorted(movie_titles, key = lambda x : len(x))
print len_movie_titles

# (b.ii) sort movie_titles by number of characters in the title
#        so that the longest titles appear at the front of the list
long_movie_titles = sorted(movie_titles, key = len, reverse = True)
print long_movie_titles

print '\nsorting a list of dictionaries by a key\n------------'
# (c.i) sort movie_dicts in alphabetical order


print '\nputting it all together\n------------'
# (d.i) sort movie_dicts by release date
#         print out the result as a list of strings, as in 1e
# ['A Boy and His Dog (1975)', 'Scanners (1981)', 'Ran (1985)', 'True Grit (2010)']
# this time order should not vary!


# (d.ii) sort movie_dicts by number of characters in the title
#         print out the titles as a list
#    ['Ran', 'Scanners', 'True Grit', 'A Boy and His Dog']
# this time order should not vary!


# (e) print out a list of titles of the three most recent movies