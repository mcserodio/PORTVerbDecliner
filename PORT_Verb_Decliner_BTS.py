'''
Classes and functions for Portuguese Verb Decliner project
'''

class Present: #indicative (default for verbs so far)
    def __init__(self,inf):
        self._infinitive=inf
        self._pst1s=''
        self._pst23s=''
        self._pst1p=''
        self._pst23p=''
        self.pst_forms={}
        
    def ar_pst1s(self,inf): #-ar infinitive: present 1st person singular
        #redefine _pst1s attribute: infinitive declined with -o ending
        self._pst1s=self._infinitive[:-2] #assign verb root to attribute
        self._pst1s+='o' #concatenate declension ending to attribute
        
    def ar_pst23s(self,inf): #present 2nd & 3rd person singular
        self._pst23s=self._infinitive[:-1] #can be formed by removing final 'r'

    def ar_pst1p(self,inf): #present 1st person plural
        self._pst1p=self._infinitive[:-1]
        self._pst1p+='mos'

    def ar_pst23p(self,inf): #present 2nd & 3rd person plural
        self._pst23p=self._infinitive[:-1]  
        self._pst23p+='m'

    def er_pst1s(self,inf): #present 1st person singular
        #redefine _pst1s attribute: infinitive declined with -o ending
        self._pst1s=self._infinitive[:-2] #assign verb root to attribute
        self._pst1s+='o' #concatenate declension ending to attribute
        
    def er_pst23s(self,inf): #present 2nd & 3rd person singular
        self._pst23s=self._infinitive[:-1]

    def er_pst1p(self,inf): #present 1st person plural
        self._pst1p=self._infinitive[:-1]
        self._pst1p+='mos'

    def er_pst23p(self,inf): #present 2nd & 3rd person plural
        self._pst23p=self._infinitive[:-1]  
        self._pst23p+='m'

    def ir_pst1s(self,inf): #present 1st person singular
        #redefine _pst1s attribute: infinitive declined with -o ending
        self._pst1s=self._infinitive[:-2] #assign verb root to attribute
        self._pst1s+='o' #concatenate declension ending to attribute
        
    def ir_pst23s(self,inf): #present 2nd & 3rd person singular
        self._pst23s=self._infinitive[:-2]
        self._pst23s+='e'

    def ir_pst1p(self,inf): #present 1st person plural
        self._pst1p=self._infinitive[:-1]
        self._pst1p+='mos'

    def ir_pst23p(self,inf): #present 2nd & 3rd person plural
        self._pst23p=self._infinitive[:-2]  
        self._pst23p+='em'
        
class ImperfectPreterit: 
    def __init__(self,inf):
        self._infinitive=inf
        self._imp123s=''
        self._imp1p=''
        self._imp23p=''
        self.pst_form={}
        
    def ar_imp123s(self,inf): #imperfect 1st, 2nd, & 3rd person singular
        self._imp123s=self._infinitive[:-1]  
        self._imp123s+='va' 
    #def dict_forms (key is the attribute, value is the declined str?) add all forms to dictionary, then use .items
    #to print the chart in one go
        #dict_forms['infinitive']=self._infinitive

    def ar_imp1p(self,inf): #imperfect 1st person plural
        self._imp1p=self._infinitive[:-2]   
        self._imp1p+='ávamos'

    def ar_imp23p(self,inf): #imperfect 1st person plural
        self._imp23p=self._infinitive[:-2] 
        self._imp23p+='avam'

    def er_imp123s(self,inf): #imperfect 1st, 2nd, & 3rd person singular
        self._imp123s=self._infinitive[:-1]  
        self._imp123s+='ia' 
    #def dict_forms (key is the attribute, value is the declined str?) add all forms to dictionary, then use .items
    #to print the chart in one go
        #dict_forms['infinitive']=self._infinitive

    def er_imp1p(self,inf): #imperfect 1st person plural
        self._imp1p=self._infinitive[:-2]   
        self._imp1p+='iamos'

    def er_imp23p(self,inf): #imperfect 1st person plural
        self._imp23p=self._infinitive[:-2] 
        self._imp23p+='iam'

    def ir_imp123s(self,inf): #imperfect 1st, 2nd, & 3rd person singular
        self._imp123s=self._infinitive[:-1]  
        self._imp123s+='ia' 
    #def dict_forms (key is the attribute, value is the declined str?) add all forms to dictionary, then use .items
    #to print the chart in one go
        #dict_forms['infinitive']=self._infinitive

    def ir_imp1p(self,inf): #imperfect 1st person plural
        self._imp1p=self._infinitive[:-2]   
        self._imp1p+='iamos'

    def ir_imp23p(self,inf): #imperfect 1st person plural
        self._imp23p=self._infinitive[:-2] 
        self._imp23p+='iam'

class PerfectPreterit:
    def __init__(self,inf):
        self._prf1s=''
        self._prf23s=''
        self._prf1p=''
        self._prf23p=''
        self.pst_forms={}
        
    def ar_prf1s(self,inf): #perfect 1st person singular
        self._prf1s=self._infinitive[:-2] 
        self._prf1s+='ei'
        
    def ar_prf23s(self,inf): #perfect 2nd & 3rd person singular
        self._prf23s=self._infinitive[:-2]
        self._prf23s+='ou'

    def ar_prf1p(self,inf): #perfect 1st person plural
        self._prf1p=self._infinitive[:-1]
        self._prf1p+='mos'

    def ar_prf23p(self,inf): #imperfect 1st person plural
        for i in self._infinitive[:-1]: 
            self._prf23p+=i
        self._prf23p+='ram'

    def er_prf1s(self,inf): #perfect 1st person singular
        self._prf1s=self._infinitive[:-2] 
        self._prf1s+='i'
        
    def er_prf23s(self,inf): #perfect 2nd & 3rd person singular
        self._prf23s=self._infinitive[:-2]
        self._prf23s+='eu'

    def er_prf1p(self,inf): #perfect 1st person plural
        self._prf1p=self._infinitive[:-1]
        self._prf1p+='mos'

    def er_prf23p(self,inf): #imperfect 1st person plural
        for i in self._infinitive[:-1]: 
            self._prf23p+=i
        self._prf23p+='ram'

    def ir_prf1s(self,inf): #perfect 1st person singular
        self._prf1s=self._infinitive[:-2] 
        self._prf1s+='i'
        
    def ir_prf23s(self,inf): #perfect 2nd & 3rd person singular
        self._prf23s=self._infinitive[:-2]
        self._prf23s+='iu'

    def ir_prf1p(self,inf): #perfect 1st person plural
        self._prf1p=self._infinitive[:-1]
        self._prf1p+='mos'

    def ir_prf23p(self,inf): #imperfect 1st person plural
        for i in self._infinitive[:-2]: 
            self._prf23p+=i
        self._prf23p+='ram'

#testing: initialize tense object, call methods to make forms, and save in dict, then print chart
''' use dictionary for user TEST action
forms_dict={}
inf='cantar'
g=Present(inf)
g.forms[pst1s]=g.ar_pst1s(inf)
g.forms[pst23s]=g.ar_pst23s(inf)
g.forms[pst1p]=g.ar_pst1p(inf)
g.forms[pst23p]=g.ar_pst23p(inf)
'''

inf='cantar'
g=Present(inf)
#make forms
g.ar_pst1s(inf)
g.ar_pst23s(inf)
g.ar_pst1p(inf)
g.ar_pst23p(inf)
#put forms in list; in program, would use .append() after creating each form
forms_list=[g._pst1s,g._pst23s,g._pst23s,g._pst1p,g._pst23p,g._pst23p]
#use list for charts; need to be able to index
for i in ['Person','Singular','Plural']: #header row
    print(format(i,'<20'))
    for n in range(6): #print s under singular column and p under plural column
        print(forms_list[n])
        print('\n')
