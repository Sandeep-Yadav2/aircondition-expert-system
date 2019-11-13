import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import skfuzzy as fuzz
import streamlit as st



st.title('AIR CONDITION CONTROLLER USING FUZZY LOGIC')
from PIL import Image
image = Image.open('ac.png')

st.image(image, caption=('Air Conditioner'),
         use_column_width=True,format='PNG')




#input
temp=ctrl.Antecedent(np.arange(10,31,1),'temp')
dew_point=ctrl.Antecedent(np.arange(10,21,1),'dew_point')

tdiff=ctrl.Antecedent(np.arange(-1,4,1),'tdiff')

#output
comp_speed=ctrl.Consequent(np.arange(0,101,1),'comp_speed')
fan_speed=ctrl.Consequent(np.arange(0,101,1),'fan_speed')


#temperture
t1=temp['low']=fuzz.trimf(temp.universe,[16,20,25])
t2=temp['optimal']=fuzz.trimf(temp.universe,[20,25,28])
t3=temp['high']=fuzz.trimf(temp.universe,[25,30,30])

#temp_diff
tdiff['negative']=fuzz.trimf(tdiff.universe,[-1,-0.5,1])
tdiff['zero']=fuzz.trimf(tdiff.universe,[-0.5,1,1.5])
tdiff['positive']=fuzz.trimf(tdiff.universe,[1,1.5,2])
tdiff['large']=fuzz.trimf(tdiff.universe,[1.5,3,3])

#dew point
dew_point['optimal']=fuzz.trimf(dew_point.universe,[10,12,15])
dew_point['humid']=fuzz.trimf(dew_point.universe,[12,18,18])

#compressor speed
comp_speed['low']=fuzz.trimf(comp_speed.universe,[0,25,50])
comp_speed['medium']=fuzz.trimf(comp_speed.universe,[25,50,80])
comp_speed['fast']=fuzz.trimf(comp_speed.universe,[50,100,100])

#fan speed
fan_speed['low']=fuzz.trimf(fan_speed.universe,[0,26,50])
fan_speed['medium']=fuzz.trimf(fan_speed.universe,[26,50,80])
fan_speed['fast']=fuzz.trimf(fan_speed.universe,[50,100,100])


#rules

rule1=ctrl.Rule(temp['low']|tdiff['negative']| dew_point['optimal'],fan_speed['low'])
rule2=ctrl.Rule(temp['optimal']|tdiff['negative']| dew_point['optimal'],fan_speed['low'])
rule3=ctrl.Rule(temp['high']|tdiff['negative']| dew_point['optimal'],fan_speed['low'])

rule4=ctrl.Rule(temp['low']|tdiff['zero']| dew_point['optimal'],fan_speed['fast'])
rule5=ctrl.Rule(temp['optimal']|tdiff['zero']| dew_point['optimal'],fan_speed['medium'])
rule6=ctrl.Rule(temp['high']|tdiff['zero']| dew_point['optimal'],fan_speed['low'])

rule7=ctrl.Rule(temp['low']|tdiff['positive']| dew_point['optimal'],fan_speed['fast'])
rule8=ctrl.Rule(temp['optimal']|tdiff['positive']| dew_point['optimal'],fan_speed['medium'])
rule9=ctrl.Rule(temp['high']|tdiff['positive']| dew_point['optimal'],fan_speed['medium'])

rule10=ctrl.Rule(temp['low']|tdiff['large']| dew_point['optimal'],fan_speed['fast'])
rule11=ctrl.Rule(temp['optimal']|tdiff['large']| dew_point['optimal'],fan_speed['fast'])
rule12=ctrl.Rule(temp['high']|tdiff['large']| dew_point['optimal'],fan_speed['fast'])



rule13=ctrl.Rule(temp['low']|tdiff['negative']| dew_point['humid'],fan_speed['fast'])
rule14=ctrl.Rule(temp['optimal']|tdiff['negative']| dew_point['humid'],fan_speed['low'])
rule15=ctrl.Rule(temp['high']|tdiff['negative']| dew_point['humid'],fan_speed['low'])

rule16=ctrl.Rule(temp['low']|tdiff['zero']| dew_point['humid'],fan_speed['fast'])
rule17=ctrl.Rule(temp['optimal']|tdiff['zero']| dew_point['humid'],fan_speed['fast'])
rule18=ctrl.Rule(temp['high']|tdiff['zero']| dew_point['humid'],fan_speed['medium'])

rule19=ctrl.Rule(temp['low']|tdiff['positive']| dew_point['humid'],fan_speed['fast'])
rule20=ctrl.Rule(temp['optimal']|tdiff['positive']| dew_point['humid'],fan_speed['fast'])
rule21=ctrl.Rule(temp['high']|tdiff['positive']| dew_point['humid'],fan_speed['fast'])

rule22=ctrl.Rule(temp['low']|tdiff['large']| dew_point['humid'],fan_speed['fast'])
rule23=ctrl.Rule(temp['optimal']|tdiff['large']| dew_point['humid'],fan_speed['fast'])
rule24=ctrl.Rule(temp['high']|tdiff['large']| dew_point['humid'],fan_speed['fast'])

rule25=ctrl.Rule(temp['low']|tdiff['negative']| dew_point['optimal'],comp_speed['low'])
rule26=ctrl.Rule(temp['optimal']|tdiff['negative']| dew_point['optimal'],comp_speed['low'])
rule27=ctrl.Rule(temp['high']|tdiff['negative']| dew_point['optimal'],comp_speed['low'])

rule28=ctrl.Rule(temp['low']|tdiff['zero']| dew_point['optimal'],comp_speed['low'])
rule29=ctrl.Rule(temp['optimal']|tdiff['zero']| dew_point['optimal'],comp_speed['low'])
rule30=ctrl.Rule(temp['high']|tdiff['zero']| dew_point['optimal'],comp_speed['low'])
rule31=ctrl.Rule(temp['low']|tdiff['positive']| dew_point['optimal'],comp_speed['fast'])
rule32=ctrl.Rule(temp['optimal']|tdiff['positive']| dew_point['optimal'],comp_speed['medium'])
rule33=ctrl.Rule(temp['high']|tdiff['positive']| dew_point['optimal'],comp_speed['medium'])
rule34=ctrl.Rule(temp['low']|tdiff['large']| dew_point['optimal'],comp_speed['fast'])
rule35=ctrl.Rule(temp['optimal']|tdiff['large']| dew_point['optimal'],comp_speed['fast'])
rule36=ctrl.Rule(temp['high']|tdiff['large']| dew_point['optimal'],comp_speed['fast'])

rule37=ctrl.Rule(temp['low']|tdiff['negative']| dew_point['humid'],comp_speed['fast'])
rule38=ctrl.Rule(temp['optimal']|tdiff['negative']| dew_point['humid'],comp_speed['low'])
rule39=ctrl.Rule(temp['high']|tdiff['negative']| dew_point['humid'],comp_speed['low'])
rule40=ctrl.Rule(temp['low']|tdiff['zero']| dew_point['humid'],comp_speed['fast'])
rule41=ctrl.Rule(temp['low']|tdiff['zero']| dew_point['humid'],comp_speed['medium'])
rule42=ctrl.Rule(temp['high']|tdiff['zero']| dew_point['humid'],comp_speed['medium'])
rule43=ctrl.Rule(temp['low']|tdiff['positive']| dew_point['humid'],comp_speed['fast'])
rule44=ctrl.Rule(temp['optimal']|tdiff['positive']| dew_point['humid'],comp_speed['fast'])
rule45=ctrl.Rule(temp['high']|tdiff['positive']| dew_point['humid'],comp_speed['medium'])

rule46=ctrl.Rule(temp['low']|tdiff['large']| dew_point['humid'],comp_speed['fast'])
rule47=ctrl.Rule(temp['optimal']|tdiff['large']| dew_point['humid'],comp_speed['fast'])
rule48=ctrl.Rule(temp['high']|tdiff['large']| dew_point['humid'],comp_speed['fast'])


fan_ctrl1=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,
                              rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24])
fan_ctrl=ctrl.ControlSystemSimulation(fan_ctrl1)
AC_ctrl=ctrl.ControlSystem([rule13,rule14,rule15,
                           rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule37,rule38,rule39,rule40,rule41,rule42,rule43,
                           rule44,rule45,rule46,rule47,rule48])
Ac=ctrl.ControlSystemSimulation(AC_ctrl)
utemp= st.number_input('Enter user Temperature',min_value=16,max_value=30)
Ac.input['temp']=(utemp)

dpoint = st.number_input('ENTER DEW POINT',min_value=11,max_value=20)
Ac.input['dew_point']=(dpoint)

tdiff = st.number_input('ENTER Temperature Diff',min_value=0,max_value=3)
Ac.input['tdiff']=(tdiff)

Ac.compute()
if st.checkbox("comp speed"):
        
        st.write(Ac.output['comp_speed'])

fan_ctrl.input['temp']=(utemp)
fan_ctrl.input['dew_point']=(dpoint)
fan_ctrl.input['tdiff']=(tdiff)

fan_ctrl.compute()
if st.button("fan speed"):
        
        st.write(fan_ctrl.output['fan_speed'])

image=Image.open('remote.jpg')
st.image(image, caption='remote',
         use_column_width=True,format='PNG')


