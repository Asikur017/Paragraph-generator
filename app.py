import streamlit as st

# 1. This sets up the title on the web browser screen
st.title("✨ My Interactive Paragraph Generator")
st.write("Change the details below, and your custom paragraph will update automatically!")

st.divider()

# 2. Creating the input sections for the user
st.subheader("👤 Personal Details")
std_name = st.text_input("Your Name", value="Rakesh")
std_age = st.text_input("Your Age", value="15")
cls = st.text_input("Class/Grade", value="4")
scl_name = st.text_input("School Name", value="PTI Institution")
location = st.text_input("Location/Address", value="Kurlipara, Musarbang, Bindia")
dishes = st.text_input("Famous Dishes", value="Biriyani, Kabab, Tikka, Polao")

st.divider()

st.subheader("👨‍👩‍👧‍👦 Family Details")
father_name = st.text_input("Father's Name", value="Gurli")
father_age = st.text_input("Father's Age", value="39")
father_occupation = st.text_input("Father's Occupation", value="Doctor")

mother_name = st.text_input("Mother's Name", value="Murli")
mother_age = st.text_input("Mother's Age", value="35")
mother_occupation = st.text_input("Mother's Occupation", value="Housewife")

st.divider()

st.subheader("🎨 Hobbies & Routine")
hobby = st.text_input("Hobbies", value="Gardening, Watching Movies, Playing Soccer")
fv_hobby = st.selectbox("Favorite Hobby", ["Gardening", "Watching Movies", "Playing Soccer"])

# Keeping the rest of your original variables clean
number_of_siblings = '4'
b1, b1_age = 'Ruhil', '2'
b2, b2_age = 'Kurman', '5'
b3, b3_age = 'Karka', '6'
scl_start, scl_finish = '9.00 a.m.', '4.00 p.m.'
wake_up, went = '6.00 a.m.', '7.30 a.m.'
sty_start, sty_finish = '7 p.m.', '9.30 p.m.'
bed_time = '10.30 p.m.'

st.divider()

# 3. This displays the paragraph live on the website using st.write instead of print
st.subheader("📝 Your Generated Story")

st.write(f'''
My name is **{std_name}**. I am {std_age} years old. I read in class {cls}. My school name is {scl_name}.
It is famous in our locality for its class leading education quality and its environment. I am living in {location} which is known for its heritage and culture. It has its own dishes for which it is famous for such as {dishes}.

My father's name is {father_name}, he is {father_age} years old. He is a {father_occupation}. My mother's name is {mother_name} and she is {mother_age} years old. She is a {mother_occupation}.
We are {number_of_siblings} brothers and sisters. I am the eldest one, 2nd one is my sister her name is {b1}, she is {b1_age}, 3rd one is brother his name is {b2}, he is {b2_age} years old. Last one name is {b3}, she is {b3_age} years old.

In weekdays, I go to the school. It starts from {scl_start} to {scl_finish}. Usually, I wake up at {wake_up}, brush my teeth and wash my face, and pray my morning prayer. While I am doing my essentials, my mother is preparing my breakfast. Afterward, I take breakfast and at {went} I headed out for my school. After finishing the school I came back and take shower and take lunch with my mother. 

In the afternoon, I play with my siblings in the garden. After playing with my siblings, I put water on plants in my garden. In the evening, I start study from {sty_start} to {sty_finish}. At the end of study, take dinner with my parents. And go to the bed at {bed_time}.    

I have a few hobbies such as {hobby}, but from them one of my favorite hobby is **{fv_hobby}**. It is a great hobby I think, because it helps me to connect with nature and play with them. Also, it gives me refreshment while I am doing. My mother helps me in the gardening.

It is such a blessing to have lovely family and spend time with them.
''')
