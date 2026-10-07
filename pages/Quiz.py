import streamlit as st

if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "score" not in st.session_state:
    st.session_state.score = 0
#This is so that the score doesn't reset with each click and it will calculate the score at the end and prompt the user to try again if they don't get a perfect score.   
#Title
st.title("Chiikawa Trivia")
st.write("Test your knowledge on Chiikawa with these questions!")
st.header("Questions")

#Question 1 #NEW
q1_answer = st.radio(
    "1. What does Chiikawa stand for?",
    options = ["Small and Cute Creature", "Fat and ugly", "Hamster", "Biggest Beefsteak"],
    index = None,
)
   
st.image("Images/chiikawa.png.")
#Question 2 #NEW
q2_answer = st.multiselect(
    "2. Which of the following characters are in the trio? (SELECT ALL THAT APPLY)",
    options = ["Hachiware", "Chiikawa", "Usagi", "Momonga"]
        )
st.image("Images/friends.png")
#Question 3 #NEW
q3_answer = st.slider(
    label = "How many members are inside the group Pajama Parties?",
    min_value = 0,
    max_value = 10,
    value = 0,
    key = "q3"
)
    
st.image("Images/pajamas.png")

#Question 4
q4_answer = st.radio(
    "4. Who is the richest character in Chiikawa's world?",
    options = ["Rakko", "Momonga", "Kurimanju", "Shisa"],
    index = None,
)
st.image("Images/Rakko.png")
#Question 5
q5_answer = st.multiselect(
    "5. What is Chiikawa's personality like?",
    options = ["Bold", "Shy", "Energetic", "Prone to Tears", "Silent"]
)
st.image("Images/cryingchiikawa.png")
#Question 6
q6_answer = st.number_input(
    "6. How many members are in the Chiikawa trio?",
    min_value=0,
    max_value=20,
    value=0,
    step=1
)
st.image("Images/thetrio.png")
if st.button("Submit Quiz"):

    score = 0

    if q1_answer == "Small and Cute Creature":
        score += 1

    if set(q2_answer) == {"Hachiware", "Chiikawa", "Usagi"}:
        score += 1

    if q3_answer == 4:
        score += 1

    if q4_answer == "Rakko":
        score += 1

    if set(q5_answer) == {"Shy", "Prone to Tears", "Silent"}:
        score += 1

    if q6_answer == 3:
        score += 1

    st.header("🎉 Results")
    st.write(f"You scored **{score}/6**!")

    if score == 6:
        st.success("You did it Chiikawa! 🎉")
    elif score >= 3:
        st.success("You're almost there Chiikawa! 👍")
    else:
        st.error("Study Harder Chiikawa! 💪")




    
