# There were 8 students in pdxcodeguild.  The instructor's name is Grant.  The students were super excited to be there.  Sitting in front of their
# computers, they jumped for joy every time Grant showed them something new...until something went terribly wrong.  Who knew that entering the
# wrong code in Python would release an actual python snake? The python slithered out of the front monitor and headed straight for the 4 students in the
# 1st row.   Wrapping them all up at once the python was about to swallow them when suddenly Grant used the top secret code and a snake-eating
# dragon flew out of the monitor and grabbed the python in its talons and flew out the window taking the snake the the 4 students with him.

variable = {'student_no':8,'place':'pdxcodeguild','instructor_name':'Grant Holly', 'emotion':'excited', 'machine': 'computers', 'language':'Python',
'animal':'python','st_no':4, 'row':1}


story="""
There were  %(student_no)d students in %(place)s.  The instructor's name is %(instructor_name)s.  The students were super %(emotion)s to be there.  Sitting in front of their %(machine)s, they jumped for
joy every time %(instructor_name)s showed them something new...until something went terribly wrong.  Who knew that entering the wrong code in %(language)s would release an actual
%(animal)s snake?  The %(animal)s slithered out of the front monitor and headed straight for the %(st_no)d students in the %(row)dst row.  Wrapping them all up at once the %(animal)s was
about to swallow them when suddenly %(instructor_name)s used the top secret code and a snake-eating dragon flew out of the monitor and grabbed the %(animal)s in its
talons and flew out the window taking the %(animal)s and the %(st_no)d students with him."""

print(story % variable)
