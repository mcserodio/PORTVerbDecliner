'''
24 Nov 2023 - present: Brazilian Portuguese imperative verb decliner
Make three different classes of verbs: -ar, -er, -ir
Tenses (each tense is a class function; declined forms stored as object attributes):
present, imperfect preterit, perfect preterit, -present participle (special case)
Start with just imperatives for now
-maybe later: separate this project into 2 files (1 for main program, 1 for classes/functions -->
import BTS file into main program file)
-also: the program itself should make files using I/O (do that later)
Main Program: create new chart (in old or existing txt file), view existing charts, modify existing charts, delete charts, irregular vrebs
'''
class ArVerb: #infinitives that end in -ar
    def __init__(self,inf):
        self._infinitive=inf

        #present imperative
        self._pst1s=''
        self._pst23s=''
        self._pst1p=''
        self._pst23p=''

        #imperfect preterit imperative
        self._imp123s=''
        self._imp1p=''
        self._imp23p=''

        #perfect preterit imperative
        self._prf1s=''
        self._prf23s=''
        self._prf1p=''
        self._prf23p=''
        
    def pst1s(self,inf): #present 1st person singular
        #redefine _pst1s attribute: infinitive declined with -o ending
        self._pst1s=self._infinitive[:-2] #assign verb root to attribute
        self._pst1s+='o' #concatenate declension ending to attribute
        
    def pst23s(self,inf): #present 2nd & 3rd person singular
        self._pst23s=self._infinitive[:-1] #can be formed by removing final 'r'

    def pst1p(self,inf): #present 1st person plural
        self._pst1p=self._infinitive[:-1]
        self._pst1p+='mos'

    def pst23p(self,inf): #present 2nd & 3rd person plural
        self._pst23p=self._infinitive[:-1]  
        self._pst23p+='m'
        
    def imp123s(self,inf): #imperfect 1st, 2nd, & 3rd person singular
        self._imp123s=self._infinitive[:-1]  
        self._imp123s+='va' 
    #def dict_forms (key is the attribute, value is the declined str?) add all forms to dictionary, then use .items
    #to print the chart in one go
        #dict_forms['infinitive']=self._infinitive

    def imp1p(self,inf): #imperfect 1st person plural
        self._imp1p=self._infinitive[:-2]   
        self._imp1p+='ávamos'

    def imp23p(self,inf): #imperfect 1st person plural
        self._imp23p=self._infinitive[:-2] 
        self._imp23p+='avam'

    def prf1s(self,inf): #perfect 1st person singular
        self._prf1s=self._infinitive[:-2] 
        self._prf1s+='ei'
        
    def prf23s(self,inf): #perfect 2nd & 3rd person singular
        self._prf23s=self._infinitive[:-2]
        self._prf23s+='ou'

    def prf1p(self,inf): #perfect 1st person plural
        self._prf1p=self._infinitive[:-1]
        self._prf1p+='mos'

    def prf23p(self,inf): #imperfect 1st person plural
        for i in self._infinitive[:-1]: 
            self._prf23p+=i
        self._prf23p+='ram'


class ErVerb:
    def __init__(self,inf):
        self._infinitive=inf

        #present imperative
        self._pst1s=''
        self._pst23s=''
        self._pst1p=''
        self._pst23p=''

        #imperfect preterit imperative
        self._imp123s=''
        self._imp1p=''
        self._imp23p=''

        #perfect preterit imperative
        self._prf1s=''
        self._prf23s=''
        self._prf1p=''
        self._prf23p=''
        
    def pst1s(self,inf): #present 1st person singular
        #redefine _pst1s attribute: infinitive declined with -o ending
        self._pst1s=self._infinitive[:-2] #assign verb root to attribute
        self._pst1s+='o' #concatenate declension ending to attribute
        
    def pst23s(self,inf): #present 2nd & 3rd person singular
        self._pst23s=self._infinitive[:-1]

    def pst1p(self,inf): #present 1st person plural
        self._pst1p=self._infinitive[:-1]
        self._pst1p+='mos'

    def pst23p(self,inf): #present 2nd & 3rd person plural
        self._pst23p=self._infinitive[:-1]  
        self._pst23p+='m'
        
    def imp123s(self,inf): #imperfect 1st, 2nd, & 3rd person singular
        self._imp123s=self._infinitive[:-1]  
        self._imp123s+='ia' 
    #def dict_forms (key is the attribute, value is the declined str?) add all forms to dictionary, then use .items
    #to print the chart in one go
        #dict_forms['infinitive']=self._infinitive

    def imp1p(self,inf): #imperfect 1st person plural
        self._imp1p=self._infinitive[:-2]   
        self._imp1p+='iamos'

    def imp23p(self,inf): #imperfect 1st person plural
        self._imp23p=self._infinitive[:-2] 
        self._imp23p+='iam'

    def prf1s(self,inf): #perfect 1st person singular
        self._prf1s=self._infinitive[:-2] 
        self._prf1s+='i'
        
    def prf23s(self,inf): #perfect 2nd & 3rd person singular
        self._prf23s=self._infinitive[:-2]
        self._prf23s+='eu'

    def prf1p(self,inf): #perfect 1st person plural
        self._prf1p=self._infinitive[:-1]
        self._prf1p+='mos'

    def prf23p(self,inf): #imperfect 1st person plural
        for i in self._infinitive[:-1]: 
            self._prf23p+=i
        self._prf23p+='ram'

class IrVerb:
    def __init__(self,inf):
        self._infinitive=inf

        #present imperative
        self._pst1s=''
        self._pst23s=''
        self._pst1p=''
        self._pst23p=''

        #imperfect preterit imperative
        self._imp123s=''
        self._imp1p=''
        self._imp23p=''

        #perfect preterit imperative
        self._prf1s=''
        self._prf23s=''
        self._prf1p=''
        self._prf23p=''
        
    def pst1s(self,inf): #present 1st person singular
        #redefine _pst1s attribute: infinitive declined with -o ending
        self._pst1s=self._infinitive[:-2] #assign verb root to attribute
        self._pst1s+='o' #concatenate declension ending to attribute
        
    def pst23s(self,inf): #present 2nd & 3rd person singular
        self._pst23s=self._infinitive[:-2]
        self._pst23s+='e'

    def pst1p(self,inf): #present 1st person plural
        self._pst1p=self._infinitive[:-1]
        self._pst1p+='mos'

    def pst23p(self,inf): #present 2nd & 3rd person plural
        self._pst23p=self._infinitive[:-2]  
        self._pst23p+='em'
        
    def imp123s(self,inf): #imperfect 1st, 2nd, & 3rd person singular
        self._imp123s=self._infinitive[:-1]  
        self._imp123s+='ia' 
    #def dict_forms (key is the attribute, value is the declined str?) add all forms to dictionary, then use .items
    #to print the chart in one go
        #dict_forms['infinitive']=self._infinitive

    def imp1p(self,inf): #imperfect 1st person plural
        self._imp1p=self._infinitive[:-2]   
        self._imp1p+='iamos'

    def imp23p(self,inf): #imperfect 1st person plural
        self._imp23p=self._infinitive[:-2] 
        self._imp23p+='iam'

    def prf1s(self,inf): #perfect 1st person singular
        self._prf1s=self._infinitive[:-2] 
        self._prf1s+='i'
        
    def prf23s(self,inf): #perfect 2nd & 3rd person singular
        self._prf23s=self._infinitive[:-2]
        self._prf23s+='iu'

    def prf1p(self,inf): #perfect 1st person plural
        self._prf1p=self._infinitive[:-1]
        self._prf1p+='mos'

    def prf23p(self,inf): #imperfect 1st person plural
        for i in self._infinitive[:-2]: 
            self._prf23p+=i
        self._prf23p+='ram'

'''
inf=input('infinitive? ')
g=Ar_Verb(inf)
g.pst1s(inf)
g.pst23s(inf)
print(g._pst1s,g._pst23s)


        if self._infinitivo[-2]=='e' or self._infinitivo[-2]=='i':
            new_form=''
            for i in self._infinitivo[:-2]:
                new_form+=i
            new_form+='ia'
            return new_form

print('starting with "estar"')
word1=Verb('estar')
print('imperfect 1st person singular form is', word1.imp_123ps())
    
#word2=Verb('beber')
#print(word2.imp_123ps())

#word3=Verb('dizer')
#print(word3.imp_123ps())

#actual program
print("Welcome to the Brazilian Portuguese Verb Recliner! Obrigada por vir.")
#while loop to keep running decliner until user wants to stop
end=False
while end==False:
    #make a menu for user to choose which tense they want to conjugate inf to
    try:
        infinitivo=input("Please enter an infinitive verb form. To return to the main menu, enter (menu): ")
        if infinitivo=='menu':
            end=True
        word=Verb(infinitivo)
        #testing if the basic structure still works; later, should be input-driven for tense:
        print('the imperfect 1st/2nd/3rd person form of your infinitive is',\
              word.imp_123ps())
    except:
        print("Invalid input, please try again.")

CHART FORMAT: infinitive header (title); columns singular/plural; rows Person
'''
