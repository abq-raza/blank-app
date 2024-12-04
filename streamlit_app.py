import streamlit as st
import random

# Title of the app
st.title("Student Comment Generator")

# Description
st.write("""
Enter the student's name and select their grade to generate a personalized comment.
""")

# Input fields
student_name = st.text_input("Student Name")
grade = st.selectbox("Grade", ("KG1", "KG2"))

# Define comments with {name} as placeholder
kg1_comments = [
    "{name} brightens each day with a positive attitude, showing genuine enthusiasm for learning and a sincere commitment to being honest. They are a great friend and are enthusiastic in helping others.",
    
    "{name} is a delightful learner who finds joy in school, approaching new challenges with a positive mindset. As they continue to grow, we are assisting them in mastering toilet training, providing the support needed to reach this important milestone.",
    
    "{name} consistently approaches classroom assignments, tasks, and group activities with impressive organization. While they display sensitivity, we are actively nurturing their strength and encouraging them to express themselves more confidently.",
    
    "{name} consistently faces issues and challenges with an admirable, can-do spirit. Their positive attitude is a powerful asset, and we believe that with such determination, there's no limit to what they can achieve.",
    
    "{name} proactively steers their own learning journey and seeks assistance whenever necessary, showcasing a strong sense of responsibility. Their enjoyment of conversations with friends during free periods not only reflects their social confidence but also their ability to effortlessly connect with and make new friends. {name}'s positive approach to both academics and social interactions is truly commendable.",
    
    "{name}'s vibrant energy and infectious smile bring positivity to the classroom environment. Not only is {name} consistently exuding good energy, but there has been noticeable improvement in their behavior. We are supporting and guiding {name} further in their ongoing development.",
    
    "{name}'s friendly and talkative nature, coupled with a curiosity to learn and assist others, contributes positively to the classroom. Notably, there has been commendable progress in their patience during activities and writing, showcasing their evolving development.",
    
    "{name} consistently demonstrates good preparation for class, showcasing genuine excitement for learning new things. Their attentive nature and ability to provide correct answers reflect not only their current knowledge but also a positive trajectory in their ongoing development.",
    
    "{name} is a focused and diligent learner, consistently striving to do their best in all tasks. Their notable emotional growth is evident and we are proud of them. We are committed to providing continued support to nurture their development further.",
    
    "{name} has made significant strides in their emotional well-being, now finding joy in attending school, which is truly uplifting. Their increased engagement is evident through improved communication as they actively seek assistance when needed. Witnessing {name}'s positive development is a source of great joy.",
    
    "{name} consistently demonstrates a proactive approach to their learning, showcasing a keen interest and a strong ability to maintain focus. Their conscious efforts to focus showcase notable growth in self-regulation, contributing positively to their ongoing development."
]

kg2_comments = [
    "{name} has been working on developing foundational skills. While there is progress in certain areas, they may need additional support and encouragement to enhance their participation in class activities and improve social interactions. With continued guidance, there is potential for growth and improvement in the next term.",
    
    "{name} has demonstrated great progress in various areas. Their enthusiasm for learning, excellent social skills, and consistent effort in both academics and creative activities showcase a wonderful achievement.",
    
    "{name} has shown good progress in key developmental areas. They have engaged well in classroom activities, demonstrated good social skills, and made satisfactory strides in academic tasks. With continued effort, they are expected to further excel in the upcoming terms.",
    
    "{name} is a well-behaved student, obedient to the teacher, respects classroom rules, and possesses a competitive spirit always striving for excellence. Excellent in completing both individual and group activities, we have every confidence that {name} will continue to excel in their educational journey, and we eagerly anticipate witnessing their continued growth and achievements. Best wishes and keep up the excellent work.",
    
    "{name} pays close attention to their teacher, follows classroom rules with respect, and possesses a competitive drive for excellence. Excelling in both individual and group tasks, it is evident that {name} has a natural aptitude for learning, and they possess the ability to quickly grasp new concepts and ideas. They are an excellent student. Best wishes and keep up the excellent work.",
    
    "{name} is a stellar student, excelling in both individual and group activities. Their potential is incredibly promising, and with continued encouragement and support, they're bound to shine even more. Providing gentle guidance and positive reinforcement will surely contribute to their continued success. Keep up the excellent work.",
    
    "{name} is a bright student, blessed with a spirit that obeys their teacher and embraces healthy competition. They shine in both individual and group activities, showcasing remarkable skills. We are excited to see {name} continue to blossom and achieve even greater heights in their educational journey. We wish them every success in meeting and exceeding expectations.",
    
    "{name} is a vibrant and eager learner, always ready to absorb new knowledge. They demonstrate excellent obedience and respect for classroom rules. Their positive energy uplifts the class atmosphere. We look forward to witnessing {name}'s ongoing success and growth, and we are excited about the bright future that lies ahead for them. Wishing them ongoing success and advancement!",
    
    "{name} is a dedicated learner who consistently demonstrates respect for classroom rules and shows great enthusiasm in both individual and group tasks. They excel in completing various activities. The future holds endless possibilities for {name}, and we are excited to see them thrive and flourish in all their endeavors. Wishing them continued success and growth!",
    
    "{name} is a delightful student who consistently follows classroom rules and embraces a strong sense of competition, constantly aiming for the best outcomes. They demonstrate exceptional skills in both individual and group tasks, and we are fortunate to have them as a part of our class. We have no doubt that {name} will continue to achieve great success in all their future endeavors. We wish them every success in meeting and exceeding expectations."
]

# Function to generate comment
def generate_comment(name, grade):
    if grade == "KG1":
        comment = random.choice(kg1_comments)
    else:
        comment = random.choice(kg2_comments)
    return comment.format(name=name)

# Button to generate comment
if st.button("Generate Comment"):
    if student_name.strip() == "":
        st.error("Please enter the student's name.")
    else:
        comment = generate_comment(student_name, grade)
        st.success("Generated Comment:")
        st.write(comment)
