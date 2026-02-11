import streamlit as st

st.title("Nested Button Example")
if 'show_second_button' not in st.session_state:
    st.session_state.show_second_button = False

if st.button("First Button"):
    st.session_state.show_second_button = True   
    # this prevents the second button to be false which would have made it go back to the beginning of the app and hide the second button again. 
    # This way, the second button will stay revealed until the user clicks it or refreshes the page.
    
if st.session_state.show_second_button:
    st.write("Revealed")
    if st.button("Second Button"):
        st.write("Second Button Clicked!")