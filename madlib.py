# There were 8 students in pdxcodeguild.  The instructor's name is Grant.  The students were super excited to be there.  Sitting in front of their
# computers, they jumped for joy every time Grant showed them something new...until something went terribly wrong.  Who knew that entering the
# wrong code in Python would release an actual python snake? The python slithered out of the front monitor and headed straight for the 4 students in the
# 1st row.   Wrapping them all up at once the python was about to swallow them when suddenly Grant used the top secret code and a snake-eating
# dragon flew out of the monitor and grabbed the python in its talons and flew out the window taking the snake the the 4 students with him.

student_no = input('Give a number')
place = raw_input('Name a place.')	
instructor_name = raw_input('Provide a name.')
emotion = raw_input('Provide an emotion.')
machine = raw_input('Name a technological object.')
language = raw_input('Name a computer language.')
animal = raw_input('Name an animal.')
st_no = raw_input('Give a number.')
ro = raw_input('Pick a positive integer less than 2.')

variable = {'student_no': student_no, 'place': place, 'instructor_name': instructor_name, 'emotion': emotion, 'machine': machine, 'language': language,
'animal': animal, 'st_no': st_no, 'ro': ro + 'st'}



story="""
There were %(student_no)d students in %(place)s.  The instructor's name is %(instructor_name)s.The students were super %(emotion)s to be there.  Sitting in front of their %(machine)s, they jumped for joy every time %(instructor_name)s showed them something new...until something went terribly wrong.  Who knew that entering the wrong code in %(language)s would release an actual
%(animal)s snake?  The %(animal)s slithered out of the front monitor and headed straight for the %(st_no)r students in the %(ro)r row.  Wrapping them all up at once the %(animal)s was
about to swallow them when suddenly %(instructor_name)s used the top secret code and a snake-eating dragon flew out of the monitor and grabbed the %(animal)s in its
talons and flew out the window taking the %(animal)s and the %(st_no)r students with him."""

print(story % variable)
