import unittest
from PORT_Verb_Decliner_BTS import *
#from PORT_Verb_Decliner import __

inf='bantar' 
v=Present(inf)
v.ar_pst1s(inf)
v.ar_pst23s(inf)
v.ar_pst1p(inf)
v.ar_pst23p(inf)

v2=ImperfectPreterit(inf)
v2.ar_imp123s(inf)
v2.ar_imp1p(inf)
v2.ar_imp23p(inf)
                    
v3=PerfectPreterit(inf)
v3.ar_prf1s(inf)
v3.ar_prf23s(inf)
v3.ar_prf1p(inf)
v3.ar_prf23p(inf)

class TestArForms(unittest.TestCase):
    #present
    def test_ar_pst1s(self): #naming convention note: tests must start w/ 'test'
        declined=v._pst1s
        self.assertEqual(declined,'banto')
    def test_ar_pst23s(self):
        declined=v._pst23s
        self.assertEqual(declined,'banta')
    def test_ar_pst1p(self):
        declined=v._pst1p
        self.assertEqual(declined,'bantamos')
    def test_ar_pst23p(self):
        declined=v._pst23p
        self.assertEqual(declined,'bantam')
    #imperfect
    def test_ar_imp123s(self): #naming convention note: tests must start w/ 'test'
        declined=v2._imp123s
        self.assertEqual(declined,'bantava')
    def test_ar_imp1p(self):
        declined=v2._imp1p
        self.assertEqual(declined,'bantávamos')
    def test_ar_imp23p(self):
        declined=v2._imp23p
        self.assertEqual(declined,'bantavam')
    #perfect
    def test_ar_prf1s(self): #naming convention note: tests must start w/ 'test'
        declined=v3._prf1s
        self.assertEqual(declined,'bantei')
    def test_ar_prf23s(self):
        declined=v3._prf23s
        self.assertEqual(declined,'bantou')
    def test_ar_prf1p(self):
        declined=v3._prf1p
        self.assertEqual(declined,'bantamos')
    def test_ar_pst23p(self):
        declined=v3._prf23p
        self.assertEqual(declined,'bantaram')
        
class TestChartFile(unittest.TestCase):
    def test_file_data_not_null(self):
        with open("Portuguese_Verb_Charts.txt",'r+') as charts:
            charts_txt=charts.read() #test that file contains data/is being read from beginning
            self.assertIsNotNone(charts_txt)
            self.assertNotEqual(charts_txt,'')
            self.assertNotEqual(charts_txt,'\n')
            self.assertNotEqual(charts_txt,' ')
    def test_chart_does_not_exist(self):
        #test that an exception is raised if chart_start index is -1 (chart cannot be found in file)
        with self.assertRaises(Exception): #use context manager so you can call function normally
            chart_not_found(-1)
            
#new test idea: user permissions (check for pre-existing permissions?)    

if __name__== '__main__': #to run tests directly from this module
    unittest.main()


#testing: initialize tense object, call methods to make forms, and save in dict, then print chart
''' use dictionary for user TEST action
forms_dict={}
inf='cantar'
g=Present(inf)
g.forms[pst1s]=g.ar_pst1s(inf)
g.forms[pst23s]=g.ar_pst23s(inf)
g.forms[pst1p]=g.ar_pst1p(inf)
g.forms[pst23p]=g.ar_pst23p(inf)

#below are tests for option 2 (view a verb chart)
inf='cantar'
tense='present'
g=Present(inf)
#make forms
g.ar_pst1s(inf)
g.ar_pst23s(inf)
g.ar_pst1p(inf)
g.ar_pst23p(inf)


#put forms in list; in actual program, would use .append() after creating each form
forms_list=[g._pst1s,g._pst23s,g._pst23s,g._pst1p,g._pst23p,g._pst23p]
'''



'''
with open("Portuguese_Verb_Charts.txt",'r+') as charts:
    charts_txt=charts.read()
    #print(charts_txt)
    chart_start=charts_txt.find(v._tense.capitalize()+' tense forms of '+inf.lower())
    #print(chart_start)
    chart_end=charts_txt.find('*', chart_start) #finds first occurrence of '*' substring after chart_start
    #print(chart_end)
    chart_end+=59 #line of 60 '*'s marks end of the chart; add 59 to find final index of chart
    charts.truncate(0) #change file handle position from end to beginning of charts
    revised_txt=charts_txt[:chart_start]+charts_txt[chart_end+1:]
    #print(charts_txt[:chart_start])
    charts.write(revised_txt)
    print(v._tense.capitalize(),'chart of',inf.lower(),'has been deleted from your charts.')
    charts.close()
#this version works!^

#old version:
with open("Portuguese_Verb_Charts.txt",'a+') as charts:
    #a+ mode won't let me rewrite the file, only append to it
    #need to be able to read the file before I rewrite it; use r+ mode
    charts_txt=charts.read()
    #this reads nothing because the file handle starts at end of file for a+ mode
    chart_start=charts_txt.find(v._tense.capitalize()+' tense forms of '+inf.lower())
    chart_end=charts_txt.find('*', chart_start) #finds first occurrence of '*' substring after chart_start
    chart_end+=59 #line of 60 '*'s marks end of the chart; add 59 to find final index of chart
    revised_txt=charts_txt[:chart_start]+charts_txt[chart_end+1:]
    #revised_txt is an empty str; see comment above regarding file handle
    print(revised_txt)
    charts_txt.write(revised_txt)
    print(v._tense.capitalize(),'chart of',inf.lower(),'has been deleted from your charts.')
    charts.close()
'''

