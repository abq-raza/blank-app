import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Student Comment Generator",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="auto",
)

def add_footer():
    footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: #555;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    <div class="footer">
        Made with ❤️ by Raza
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

# Display the logo at the top
logo_url = "https://assets.mograsys.com/Content/alimtiaz/Images/SchoolLogo/mograsys.jpg"
st.image(logo_url, width=150)
st.title("Homeroom - Student Comment Generator")

# Description
st.write("""
Enter the student's name and select their grade to generate a personalized comment.
""")

# Input fields
student_name = st.text_input("Student Name")
grade = st.selectbox("Grade", ("KG1", "KG2", "Grade 1", "Grade 2", "Grade 3", "Grade 4"))

# Define comments with {name} as placeholder

# KG1 Comments
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

# KG2 Comments
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

# Grade 1 Comments
grade1_comments = [
    "{name} is a gifted learner, consistently displaying a strong grasp of classroom topics. Their zest for learning is admirable and serves as a wonderful inspiration to their classmates. Additionally, embracing more consistent completion of homework assignments will further showcase their remarkable abilities.",
    "{name} consistently completes assignments and demonstrates a strong commitment to enhancing their abilities. They have great potential which can be further realized by channeling their enthusiasm for conversation into class discussions and maintaining a steady focus during lessons. Developing organizational skills will help them effectively manage tasks and continue their impressive progress.",
    "{name} shows an eagerness to embrace new knowledge. Consistent practice of their skills outside the classroom will further enhance their learning journey. Developing greater concentration during lessons and activities will wonderfully complement their growing skill set.",
    "{name} is a bright and enthusiastic student, consistently displaying a keen interest in classroom activities. Their courteous demeanor is evident in interactions with classmates and teachers alike, contributing to a harmonious and respectful learning atmosphere.",
    "{name} has demonstrated consistent growth throughout the term. Their organizational skills are commendable, and they always complete homework assignments punctually. Exploring further opportunities in spelling will enhance their already impressive skill set.",
    "{name} is a bright and well-organized student, consistently showcasing a solid grasp of the concepts taught. They serve as a wonderful role model for their classmates through exceptional work habits and exhibit a commendable sense of pride in their achievements."
]

# Grade 2 Comments
grade2_comments = [
    "{name} is a fast learner and excels in understanding new concepts. They demonstrate a natural ability to grasp and apply new information. Their enthusiasm for learning is commendable. They have the potential to improve in the areas of organization and cleanliness. With guidance and practice, they can develop excellent organizational skills. In terms of spellings, they have the potential to improve their skills further!",
    "{name} is a remarkable student who consistently demonstrates a neat and well-organized approach to their work. They have shown great agility in class activities. Additionally, they have demonstrated intelligence in their academic work, consistently understanding concepts and applying them effectively. To further enhance their learning experience, they are encouraged to continue upgrading their knowledge beyond the curriculum. Keep up the spirit!",
    "{name} is a quiet and obedient student who consistently follows instructions and classroom rules. In terms of handwriting, they have the potential to improve the neatness and legibility of their writing. With continued practice and focus, they can make their handwriting more visually pleasing and easier to read. Encouraging them to work on gaining fluency in counting both forward and backward and to practice spellings will contribute to their overall number sense and literacy skills!",
    "{name} is a remarkable student who consistently demonstrates a neat and well-organized approach to their work. They have shown great agility in class activities. Additionally, they have demonstrated intelligence in their academic work, consistently understanding concepts and applying them effectively. To further enhance their learning experience, they are encouraged to continue upgrading their knowledge beyond the curriculum. Keep up the spirit!",
    "{name} is a quiet and well-behaved student who consistently follows instructions in class. They demonstrate a strong ability to grasp concepts quickly, which is commendable. To further enhance their learning experience, they are encouraged to actively volunteer and engage more in class activities. This will help them strengthen their communication and collaboration skills while also building confidence!"
]

# Grade 3 Comments
grade3_comments = [
    "{name} has a passion for learning and studies with enthusiasm, always keen to learn something new. They are very cooperative and constantly treat their peers with kindness and respect. There's always an opportunity for growth in both reading and speaking skills. Consistent practice in reading will undoubtedly lead to remarkable progress.",
    "{name} has self-confidence that constantly shows respect towards their peers. They consistently engage in class activities with enthusiasm and a positive mindset, demonstrating notable progress across various subjects. They have great potential for improvement in their reading skills and can achieve even greater success with continued effort.",
    "{name} has a passion for learning and studies with enthusiasm, always keen to learn something new. They are very cooperative and constantly treat their peers with kindness and respect. Opportunities for growth exist in both reading and speaking skills. Consistent practice in reading can lead to remarkable progress.",
    "{name} consistently demonstrates high self-confidence and eagerness to engage in class activities. Their positive approach to learning reflects pride in showcasing their abilities. To elevate their communication skills, they can enhance clarity in expressing their thoughts."
]

# Grade 4 Comments
grade4_comments = [
    "{name} is consistently polite, kind, and helpful to both peers and teachers, creating a welcoming classroom environment. Their confidence shines through as they actively participate in all school activities, showcasing their willingness to try new things and embrace challenges. Keep up the good work!",
    "{name} consistently demonstrates politeness, kindness, and conscientiousness towards peers and teachers. Their ability to set targets and goals allows them to consistently aim higher and achieve great success. They exude confidence and take responsibility for their learning. Keep up the good work!",
    "{name} is consistently courteous, well-mannered, helpful, and responsible. Their positive attitude towards learning is inspiring, and they confidently and enthusiastically take part in all school activities. They always aim for excellence and show respect towards their peers. Keep up the good work!",
    "{name}'s positive attitude and efforts in their studies are commendable. They consistently display kindness and responsibility in both their actions and interactions with others. Additionally, they are always ready to lend a helping hand to classmates, creating a supportive learning environment.",
    "{name}'s courteous and well-mannered behavior is commendable. They consistently display politeness and respect towards peers, creating a positive environment in the classroom. Setting goals and targets will provide them with a clear direction and motivation to strive for academic excellence."
]

# Function to generate comment
def generate_comment(name, grade):
    if grade == "KG1":
        comment = random.choice(kg1_comments)
    elif grade == "KG2":
        comment = random.choice(kg2_comments)
    elif grade == "Grade 1":
        comment = random.choice(grade1_comments)
    elif grade == "Grade 2":
        comment = random.choice(grade2_comments)
    elif grade == "Grade 3":
        comment = random.choice(grade3_comments)
    elif grade == "Grade 4":
        comment = random.choice(grade4_comments)
    else:
        comment = "No comments available for the selected grade."
    return comment.format(name=name)

# Button to generate comment
if st.button("Generate Comment"):
    if student_name.strip() == "":
        st.error("Please enter the student's name.")
    else:
        comment = generate_comment(student_name, grade)
        st.success("Generated Comment:")
        st.write(comment)

# Add footer
add_footer()
