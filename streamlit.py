import streamlit as st


st.title('Simple Calculator')
a=st.number_input('enter your first number:')
b=st.number_input('enter your second number:')
operator=st.text_input('enter the operator:(+,-,*,/,//,%,**)')


button=st.button('Run')
st.text('The result is:')
if button== 1:
    if operator=='+':
        st.write(a+b)
    elif operator=='-':
        st.write(a-b)
    elif operator=='*':
        st.write(a*b)
    elif operator=='/':
        st.write(a/b)
    elif operator=='//':
        st.write(a//b)
    elif operator=='%':
        st.write(a%b)
    elif operator=='**':
        st.write(a**b)
    else:
        st.write('Unavailable operator')


