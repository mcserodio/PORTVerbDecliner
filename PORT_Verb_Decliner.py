'''
Marilia C Serodio -- Portuguese Verb Decliner -- started 24 Nov 2023


word=some string
for word in range (-2,-1):
	if word[-2] + word[-1] == ‘ar’ or ‘er’ or ‘ir’:
		return word.replace(‘r’,’ndo’) #need to ensure it’ll only replace suffix part, not any ‘r’ in word
#see below: maybe use range and (len(word),len(word)-3,-1)? For examining last two chars of word
#or word[len(word)-3:]
#or Boolean operator ‘in’:
#if ‘ar’ or ‘er’ or ‘ir’ in word[len(word)-3:]

Verb decliner: use custom function WITHIN A CLASS to create dictionary entry w/ one key (verb infinitive form) and multiple values
(declensions of the verb from first to third person, both singular and plurals). Have different class for each tense (this preliminary
verb decliner will only have present/past (imperfect + perf) and participles). Make the program interactive (while loop); users can store,
view, and change their verb study guide. Also make it so that function can recognize irregular verbs (and will then store those irregular forms
— different class for irregular/regular verbs of each tense, maybe?)
'''
#assume only regular verbs are entered for this program; later, ensure that the program recognizes irregular verbs and can print out
#those exceptional declined forms to the users

#each verb tense has its own class; each instance created of the class is an object (dictionary) holding the different declined forms of that tense
class ImperfectPreterit:
    def __init__(self,infinitive): #when I define functions below, am I working w/ the object self or infinitive (user input)? need to review Classes
        #and object-oriented programming
        self.inf = infinitive
        #make empty dictionary to hold different declined forms
        self.declined = {}
    def print_inf(self):
        print(self.inf)
    def p1s_p2s_ar(self): #1st and 2nd person singular of -ar verb have same form
        #replace the last occurence of 'ar' or 'r' w/ 'ava' or 'va', e.g. nadar --> nadava
        for letter in self.inf[-2:-1]:
            self.inf.replace('ar','ava')
        print(self.inf)
        '''
        form_p1s_ar=infinitive.replace('ar','ava')
        declined['1st Person Singular']=infinitive.replace('r','va')
        print("First person singular of the imperfect preterit is",declined['1st Person Singular'])
        '''
        
    #def p1p_ar(self): #1st person plural of -ar V
        #return self.replace('r','ávamos')
    
n=ImperfectPreterit("nadar")
n.print_inf()
declined_form=n.p1s_p2s_ar()
print(declined_form)
'''this returns nadar \n nadar \n None'''
#forms needed: 'FirstPersonSing':'','SecondPersonSing':'','ThirdPersonSing':'','FirstPersonPl':'','SecondPersonPl':'','ThirdPersonPl':''

''' 
end=False
while end==False:
    inf=input("Enter a Portuguese regular verb infinitive or 'e' to end the program: ")
    if inf='e':
        break
    else:
        #decline verb
'''
