import streamlit as st

def app():      
    st.title('Style transfer')
    st.subheader('Lets have little bit of fun')
    st.image('https://analyticsindiamag.com/wp-content/uploads/2020/06/1_kOQOZxBDNw4lI757soTEyQ.png')
    st.subheader('What is style transfer?')
    st.write('Neural Style Transfer refers to a class of software algorithms that manipulate digital images, or videos, in order to adopt the appearance or visual style of another image. ')
    st.write('You want to try it ,click on below given link')
    st.subheader('https://neural-style-transfer-kkp.herokuapp.com/')
    st.write('You have to upload two Images ')
    st.write('Content image of a person, animal or any place')
    st.write('Style image ,In which style you want to convert your content image .')