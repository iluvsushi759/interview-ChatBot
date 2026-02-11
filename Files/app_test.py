import streamlit as st

st.title('_This_ is :blue[a title] :speech_balloon:')

st.title('$E = mc^2$')

st.header('This is a header')
st.subheader('This is a subheader')

st.text('This is plain text without any formatting.')

st.markdown('This is **bold** text, this is *italic* text, and this is `inline code`.\n- This is a list item')

st.write('Hello *world* using st.write :smile:')

data = {"Name": "Alice", "Age": 30, "Occupation": "Engineer"}
