# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:45:00 2026

@author: chandan
"""
import streamlit as st


def smoke_condition(smoke):
    

    if (smoke[0] == 0):
        return ("Join Smoker Group First")
    else:
        return ("Smoker नशेड़ी  ( NASHEDI ) BUDAAAAAAAAAAAAAAAA....... B$DK")
def main():
    
    # giving the title
    st.title('SMOKING PREDICTION for ASIF')

    # getting the input from user
    Smoke = st.number_input('Are you a Regular Smoker--(valid input-- 0-- NO, 1-- YES)',min_value=0, max_value=1)
    Age = st.number_input('Your Age(18 to 99)', min_value=18, max_value=99)
    # code for prediction
    condition = ''
    
    if st.button('SMOKING RESULT'):
        condition = smoke_condition([Smoke, Age])
        
    st.success(condition)
    
if __name__ == '__main__':
    main()
        
    
 