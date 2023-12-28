from unittest import *
from PORT_Verb_Decliner_BTS import *

inf='bantar'
v=Present(inf)
v.ar_pst1s(inf)
v.ar_pst23s(inf)
v.ar_pst1p(inf)
v.ar_pst23p(inf)

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