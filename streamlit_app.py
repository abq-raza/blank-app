import streamlit as st

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
st.title("Homeroom-Student Comment Generator")

# Description
st.write("""
Enter the student's name and select their grade and comment category to generate all sample comments for that category. **ALWAYS VERIFY AND DOUBLE CHECK**. **REPLACE 'THEIR'/'THEY' WITH 'HER/SHE' or 'HIS/HE' DEPENDING ON THEIR GENDER. 
""")

# Input fields
student_name = st.text_input("Student Name")
grade = st.selectbox("Grade", ("KG1", "KG2", "Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6"))

organized_comments = {
    "KG1": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} shows exceptional enthusiasm in all activities and consistently demonstrates a keen interest in learning new things. Their ability to grasp concepts quickly is impressive.",
            "{name} is a joy to have in class. They actively participate in discussions and help create a positive learning environment for everyone."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} is a reliable and hardworking student who consistently completes their tasks on time. They show a good understanding of the material and are always willing to help their classmates.",
            "{name} demonstrates a strong commitment to their learning. They follow instructions well and maintain a positive attitude in the classroom."
        ],
        "Rising, developing and Emerging students": [
            "{name} is making great progress in their learning journey. With continued support and encouragement, they will continue to develop their skills and confidence.",
            "{name} is eager to learn and shows improvement each day. Focusing on participation will help them further enhance their learning experience."
        ]
    },
    "KG2": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} consistently excels in all activities and displays a remarkable understanding of new concepts. Their leadership qualities are evident as they often assist and encourage their peers.",
            "{name} is highly motivated and shows great initiative in their learning. Their positive attitude and enthusiasm are contagious."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} is a dependable student who shows consistent effort in their studies. They have a solid grasp of the concepts taught and continue to improve steadily.",
            "{name} maintains a positive demeanor and demonstrates good behavior in class. Their dedication to learning is commendable."
        ],
        "Rising, developing and Emerging students": [
            "{name} is developing their skills well and shows a growing interest in classroom activities. With continued practice, they will continue to make significant strides.",
            "{name} is showing encouraging progress. Focusing on participation and engagement will further enhance their learning."
        ]
    },
    "Grade 1": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} is a gifted learner, consistently displaying a strong grasp of classroom topics. Their zest for learning is admirable and serves as a wonderful inspiration to their classmates. Additionally, embracing more consistent completion of homework assignments will further showcase their remarkable abilities.",
            "{name} is a bright and well-organized student, consistently showcasing a solid grasp of the concepts taught. They serve as a wonderful role model for their classmates through exceptional work habits and exhibit a commendable sense of pride in their achievements."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} consistently completes assignments and demonstrates a strong commitment to enhancing their abilities. They have great potential which can be further realized by channeling their enthusiasm for conversation into class discussions and maintaining a steady focus during lessons. Developing organizational skills will help them effectively manage tasks and continue their impressive progress.",
            "{name} is a bright and enthusiastic student, consistently displaying a keen interest in classroom activities. Their courteous demeanor is evident in interactions with classmates and teachers alike, contributing to a harmonious and respectful learning atmosphere.",
            "{name} has demonstrated consistent growth throughout the term. Their organizational skills are commendable, and they always complete homework assignments punctually. Exploring further opportunities in spelling will enhance their already impressive skill set."
        ],
        "Rising, developing and Emerging students": [
            "{name} shows an eagerness to embrace new knowledge. Consistent practice of their skills outside the classroom will further enhance their learning journey. Developing greater concentration during lessons and activities will wonderfully complement their growing skill set."
        ]
    },
    "Grade 2": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} is a fast learner and excels in understanding new concepts. They demonstrate a natural ability to grasp and apply new information. Their enthusiasm for learning is commendable. They have the potential to improve in the areas of organization and cleanliness. With guidance and practice, they can develop excellent organizational skills. In terms of spellings, they have the potential to improve their skills further!",
            "{name} is a remarkable student who consistently demonstrates a neat and well-organized approach to their work. They have shown great agility in class activities. Additionally, they have demonstrated intelligence in their academic work, consistently understanding concepts and applying them effectively. To further enhance their learning experience, they are encouraged to continue upgrading their knowledge beyond the curriculum. Keep up the spirit!"
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} is a quiet and well-behaved student who consistently follows instructions in class. They demonstrate a strong ability to grasp concepts quickly, which is commendable. To further enhance their learning experience, they are encouraged to actively volunteer and engage more in class activities. This will help them strengthen their communication and collaboration skills while also building confidence!"
        ],
        "Rising, developing and Emerging students": [
            "{name} is a quiet and obedient student who consistently follows instructions and classroom rules. In terms of handwriting, they have the potential to improve the neatness and legibility of their writing. With continued practice and focus, they can make their handwriting more visually pleasing and easier to read. Encouraging them to work on gaining fluency in counting both forward and backward and to practice spellings will contribute to their overall number sense and literacy skills!"
        ]
    },
    "Grade 3": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} consistently demonstrates high self-confidence and eagerness to engage in class activities. Their positive approach to learning reflects pride in showcasing their abilities. To elevate their communication skills, they can enhance clarity in expressing their thoughts."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} has a passion for learning and studies with enthusiasm, always keen to learn something new. They are very cooperative and constantly treat their peers with kindness and respect. There's always an opportunity for growth in both reading and speaking skills. Consistent practice in reading will undoubtedly lead to remarkable progress.",
            "{name} has self-confidence that constantly shows respect towards their peers. They consistently engage in class activities with enthusiasm and a positive mindset, demonstrating notable progress across various subjects. They have great potential for improvement in their reading skills and can achieve even greater success with continued effort.",
            "{name} has a passion for learning and studies with enthusiasm, always keen to learn something new. They are very cooperative and constantly treat their peers with kindness and respect. Opportunities for growth exist in both reading and speaking skills. Consistent practice in reading can lead to remarkable progress."
        ],
        "Rising, developing and Emerging students": [
            "{name} is showing promising growth in their academic and social skills. With continued encouragement and support, they will become more confident in their abilities and contribute positively to the classroom environment.",
            "{name} is developing a stronger understanding of the curriculum. Focusing on active participation during lessons will further enhance their learning experience."
        ]
    },
    "Grade 4": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} is consistently polite, kind, and helpful to both peers and teachers, creating a welcoming classroom environment. Their confidence shines through as they actively participate in all school activities, showcasing their willingness to try new things and embrace challenges. Keep up the good work!",
            "{name} consistently demonstrates politeness, kindness, and conscientiousness towards peers and teachers. Their ability to set targets and goals allows them to consistently aim higher and achieve great success. They exude confidence and take responsibility for their learning. Keep up the good work!",
            "{name} is consistently courteous, well-mannered, helpful, and responsible. Their positive attitude towards learning is inspiring, and they confidently and enthusiastically take part in all school activities. They always aim for excellence and show respect towards their peers. Keep up the good work!"
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name}'s positive attitude and efforts in their studies are commendable. They consistently display kindness and responsibility in both their actions and interactions with others. Additionally, they are always ready to lend a helping hand to classmates, creating a supportive learning environment.",
            "{name}'s courteous and well-mannered behavior is commendable. They consistently display politeness and respect towards peers, creating a positive environment in the classroom. Setting goals and targets will provide them with a clear direction and motivation to strive for academic excellence."
        ],
        "Rising, developing and Emerging students": [
            "{name} is gradually building their confidence in class discussions. With more encouragement, they will become more active participants and further develop their communication skills.",
            "{name} is showing improvement in their organizational skills. Continued focus on task management will help them excel even more in their studies."
        ]
    },
    "Grade 5": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} consistently demonstrates a strong understanding of the curriculum. Their analytical skills and ability to think critically are commendable. Encouraging {name} to participate more in class discussions will further enhance their learning experience.",
            "{name} is a proactive learner who takes initiative in both individual and group tasks. Their ability to collaborate effectively with peers is a significant asset to the classroom dynamic. Focusing on refining their presentation skills will benefit {name} in future projects.",
            "{name} exhibits a keen interest in all subjects, particularly excelling in mathematics and science. Their problem-solving abilities are outstanding. To further develop, {name} should focus on enhancing their writing skills to complement their analytical strengths.",
            "{name} has a strong grasp of the material covered this term and applies their knowledge effectively in assignments and exams. Encouraging {name} to engage more in extracurricular activities will help in their overall personal development.",
            "{name} is highly motivated and demonstrates excellent time management skills. Their ability to balance academic responsibilities with extracurricular commitments is impressive. Continuing to set personal goals will help {name} achieve even greater heights.",
            "{name} shows exceptional creativity and originality in their projects. Their ability to think outside the box is a valuable trait. Focusing on developing their research skills will further enhance {name}'s academic performance.",
            "{name} is an enthusiastic participant in class activities and shows great leadership potential. Their ability to guide and inspire peers is noteworthy. Encouraging {name} to take on more leadership roles will benefit both them and their classmates.",
            "{name} consistently produces high-quality work and demonstrates a thorough understanding of complex concepts. Their dedication to continuous improvement is admirable. Fostering {name}'s curiosity through advanced topics can further stimulate their intellectual growth."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} has shown remarkable improvement in their academic performance this term. Their dedication to completing assignments on time and actively seeking help when needed is impressive. Continuing this level of commitment will undoubtedly lead to further success.",
            "{name} is a responsible and dependable student who consistently meets deadlines and maintains high standards in their work. Their positive attitude and willingness to help others contribute to a supportive classroom environment."
        ],
        "Rising, developing and Emerging students": [
            "{name} is beginning to show more interest in class activities and discussions. With continued encouragement, they will develop greater confidence in their abilities.",
            "{name} is making steady progress in their studies. Focusing on building stronger study habits will help them achieve their full potential."
        ]
    },
    "Grade 6": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} has shown outstanding academic performance throughout the year. Their ability to grasp complex concepts quickly and apply them effectively is impressive. Encouraging {name} to take on more challenging projects will further enhance their learning.",
            "{name} is a diligent student who consistently produces excellent work. Their attention to detail and commitment to understanding the material deeply are commendable. {name} would benefit from participating in class debates to strengthen their public speaking skills.",
            "{name} demonstrates a high level of maturity and responsibility in all aspects of their schoolwork. Their ability to manage time effectively and prioritize tasks is exemplary. Continuing to set ambitious goals will help {name} achieve their full potential.",
            "{name} is a highly motivated learner who excels in both individual and group settings. Their leadership qualities and ability to collaborate with peers make them a valuable member of any team. Focusing on enhancing their analytical writing skills will benefit {name}'s academic journey.",
            "{name} exhibits a strong passion for learning, particularly in subjects such as history and literature. Their insightful contributions to class discussions enrich the learning environment for everyone. Encouraging {name} to engage in independent research projects will further develop their critical thinking skills.",
            "{name} consistently demonstrates exceptional problem-solving abilities and a keen analytical mind. Their proactive approach to seeking help when needed shows a commitment to continuous improvement. {name} should consider exploring advanced topics to further challenge their intellectual capabilities."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} is a respectful and cooperative student who consistently upholds classroom standards. Their ability to work harmoniously with others contributes to a positive learning atmosphere. Encouraging {name} to take on mentorship roles can help them develop leadership skills.",
            "{name} has shown significant growth in their academic performance this year. Their perseverance and dedication to overcoming challenges are admirable. Focusing on enhancing their presentation and communication skills will further support {name}'s academic success."
        ],
        "Rising, developing and Emerging students": [
            "{name} is gradually improving in their academic performance. With continued support and encouragement, they will build greater confidence in their abilities.",
            "{name} is beginning to engage more actively in class activities. Focusing on participation will help {name} enhance their learning experience."
        ]
    }
}

def get_categories(selected_grade):
    return list(organized_comments.get(selected_grade, {}).keys())

def generate_comments(name, selected_grade, selected_category):
    grade_comments = organized_comments.get(selected_grade, {})
    category_comments = grade_comments.get(selected_category, [])
    if not category_comments:
        return []
    
    # Format all comments with the student's name
    formatted_comments = [comment.format(name=name) for comment in category_comments]
    return formatted_comments

# Now, always attempt to display categories after grade is selected
categories = get_categories(grade)
if categories:
    category = st.selectbox("Comment Category", categories)
else:
    st.warning("No categories available for the selected grade.")
    category = None

if st.button("Generate Comments"):
    if student_name.strip() == "":
        st.error("Please enter the student's name.")
    elif category is None:
        st.error("Please select a valid comment category.")
    else:
        comments = generate_comments(student_name, grade, category)
        if not comments:
            st.warning("No comments available for the selected grade and category.")
        else:
            st.success("Generated Comments:")
            # Display all generated comments
            for i, comment_text in enumerate(comments, 1):
                st.markdown(f"**Option {i}:**")
                st.write(comment_text)
                st.markdown("---")


add_footer()
