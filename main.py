import random
names= ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
#new_dict= {new_key:new_value for (key,value) in dict.items() if test}
students_scores= {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student,score) in students_scores.items() if score>=70}


