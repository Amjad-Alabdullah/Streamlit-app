
import streamlit as st
from PIL import Image
st.markdown(""" <style> .font {
    font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    font-size:35px;
    color: white;
} 
</style> """, unsafe_allow_html=True)
st.markdown(""" <style> .fon {
    font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    font-size:60px;
    color: white;
} 
</style> """, unsafe_allow_html=True)
st.markdown(""" <style> .demo{
    font-family:Copperplate, Papyrus, fantasy;
    font-size:25px;
    color: white;
} 
</style> """, unsafe_allow_html=True)
st.markdown(""" <style> .box {
    border: 2px solid black;
    outline: white solid 5px;
    margin: auto;  
    padding: 20px;
    text-align: center;
} 
</style> """, unsafe_allow_html=True)

st.sidebar.markdown('<p class="font">My First Streamlit Application !!!</p>', unsafe_allow_html=True)
with st.sidebar:
    st.write(""" About the app:""")
    st.write("""=> Flames Game is a relationship calculating algorithm which is famous between the youngsters.""")
    st.header("FLAMES stands for:")
    st.write("F - Friends")
    st.write("L - Lover")
    st.write("A - Affection")
    st.write("M - Marriage")
    st.write("E - Enemy")
    st.write("S - Sibling")
st.markdown('<p style="text-align: center;" class="fon">F L A M E S</p>', unsafe_allow_html=True)
st.markdown('<h5 style="text-align: center;">✨✨The  most  fascinating  and  nostalgic  app  is  back ✨✨</h5>', unsafe_allow_html=True)
st.write("Knock🧐! Knock🧐 !...Hey😀!!!...It's time⏰...Let's start to Check your relationship status😉 by appending the identities...")

n1=st.text_input("Enter first name:")
n2=st.text_input("Enter second name:")
st.markdown("Next...press the button to know your magic number!!!😀😀")
n1=n1.replace(" ","").lower()
n2=n2.replace(" ","").lower()
n4=str(n2)
for i in n1.lower():
    n2=n2.replace(i,"",1)
for j in n4.lower():
    n1=n1.replace(j,"",1)
N=len(n1)+len(n2)

res=st.button("Get the magic number")
if res:
    if not(n1.isnumeric() and n2.isnumeric()):
        st.balloons()
        st.write(" Your Magic Number is: ",N)
        st.write("Hey...Awesome😍...You are not far off...")
        st.write("Just enter the magic number and click done to know your affiliation❤...")
    else:
        st.write("only characters are allowed")

num=st.number_input("Enter your magic number:")
if num:
    if int(num) is N:
        flames = 'FLAMES'
        length  = 6
        while(True):
            position = N%length
            flames=flames.replace(flames[position-1],'')
            if(position==0):
                flames=flames[position:]
            else:
                flames=flames[position-1:]+flames[:position-1]
            length-=1
            if length == 1:
                break
    else:
        st.warning("enter crt num")
        
le=st.button("Done")
if le and int(num) is N and num:
    relationship=flames
    if relationship[0] == 'F':
        image=Image.open('frd2.jpg')
        new=image.resize((250,150))
        col1, col2, col3 = st.columns([0.2,1, 0.2])
        col2.image(new, use_column_width=True)
        st.markdown('<div class="box"><p class="demo">Friend - A person who will be your shadow if you are alone , will be your shoulder if you want to cry,will be your smile if you need to be happy and walks in when rest of the world walks out</p></div>', unsafe_allow_html=True)
        st.snow()
    elif relationship[0] == 'L':
        image=Image.open('love1.jpg')
        new=image.resize((350,250))
        col1, col2, col3 = st.columns([0.2,1, 0.2])
        col2.image(new, use_column_width=True)
        st.markdown('<div class="box"><p class="demo">Love - Person who feels that your happines is essential as their own and all want is you to be happy even if he/she is not part of your happiness</p></div>', unsafe_allow_html=True)
        st.snow()
    elif relationship[0] == 'A':
        image=Image.open('aff2.webp')
        new=image.resize((380,260))
        col1, col2, col3 = st.columns([0.2,1, 0.2])
        col2.image(new, use_column_width=True)
        st.markdown('<div class="box"><p class="demo">Affection - Person who shows a gentle feeling of fondness,caring and makes you feel safe and always cared for</p></div>', unsafe_allow_html=True)
        st.snow()
    elif relationship[0] == 'M':
        image=Image.open('mar2.jpg')
        new=image.resize((500,350))
        col1, col2, col3 = st.columns([0.2,1, 0.2])
        col2.image(new, use_column_width=True)
        st.markdown('<div class="box"><p class="demo">Marriage - Special person who loves more than your mom,cares more than your father,supports and annoy you in rest of the life</p></div>', unsafe_allow_html=True)
        st.snow()
    elif relationship[0] == 'E':
        image=Image.open('ene4.jpg')
        new=image.resize((350,280))
        col1, col2, col3 = st.columns([0.2,1, 0.2])
        col2.image(new, use_column_width=True)
        st.markdown('<div class="box"><p class="demo">Enemy - Person who triggers your potential and makes you to stand up for somethimg , sometime in life</p></div>', unsafe_allow_html=True)
        st.snow()
    elif relationship[0] == 'S':
        image=Image.open('sib2.webp')
        new=image.resize((300,250))
        col1, col2, col3 = st.columns([0.2,1, 0.2])
        col2.image(new, use_column_width=True)
        st.markdown('<div class="box"><p class="demo">Sibling - Person who is the second parent and the most arrogant best friend in the world</p></div>', unsafe_allow_html=True)
        st.snow()
    else:
        st.write('enter valid name or try again...')


