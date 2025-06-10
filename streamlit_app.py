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

organized_comments_sem1 = {
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

organized_comments = {
    "KG1": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} has shown exceptional enthusiasm throughout the year, consistently demonstrating a keen interest in learning. Their ability to grasp new concepts quickly is impressive, and they are well-prepared for the challenges of KG2.",
            "{name} has been a joy to have in class this year. They actively participate in all activities, contribute positively to group discussions, and have developed strong social skills, making them a wonderful role model for their peers.",
            "It has been a pleasure to watch {name} grow this year. They have shown great leadership potential and a genuine love for learning. Their readiness for KG2 is evident in their academic and social maturity."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} has been a reliable and hardworking student all year long. They consistently completed tasks with care and have built a solid foundation for their learning. They are ready for a successful year in KG2.",
            "{name} has demonstrated a strong commitment to their learning and has shown wonderful growth in their independence. They follow instructions well, maintain a positive attitude, and interact kindly with classmates.",
            "{name} has made steady progress throughout the year, particularly in their ability to recognize letters and numbers. Their consistent effort is commendable, and with continued focus, they will thrive in KG2."
        ],
        "Rising, developing and Emerging students": [
            "{name} has made wonderful progress on their learning journey this year. With continued support and encouragement as they move into KG2, they will continue to build confidence and develop their skills.",
            "{name} has become more comfortable and participative in the classroom setting. To ensure a strong start in KG2, we encourage them to continue practicing their listening skills and engaging with peers during learning activities.",
            "It has been great to see {name}'s confidence grow this year. They have shown increasing interest in our learning themes and are beginning to share their ideas. Continued encouragement at home will greatly benefit their transition to KG2."
        ]
    },
    "KG2": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} has consistently excelled in all activities this year and displayed a remarkable understanding of new concepts. Their leadership qualities have blossomed, and they are thoroughly prepared for the academic demands of Grade 1.",
            "{name} has been a highly motivated and proactive learner throughout KG2. Their positive attitude and enthusiasm are contagious, and they have built a strong foundation in early literacy and numeracy for the coming year.",
            "{name} consistently produces work of a high standard and shows great initiative. They are a confident communicator and a kind friend to others, demonstrating a readiness for the more structured environment of Grade 1."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} is a dependable student who has shown consistent effort and progress this year. They have a solid grasp of the concepts taught and are well-prepared for a successful transition to Grade 1.",
            "{name} has maintained a positive demeanor and demonstrated good behavior all year. Their dedication to learning is commendable, and they have grown into a more confident and capable learner.",
            "{name} has worked hard this year and it shows. They have developed good work habits and a solid understanding of our curriculum. They should be very proud of their achievements as they get ready for Grade 1."
        ],
        "Rising, developing and Emerging students": [
            "{name} has developed their skills well and has shown a growing interest in classroom activities this year. With continued practice over the summer, they will make significant strides and be ready for Grade 1.",
            "{name} has shown encouraging progress, especially in their social interactions and willingness to try new things. Focusing on active listening and participation will be key to a successful start in Grade 1.",
            "This year, {name} has become more engaged in their learning and has made good progress in phonics and counting. Continued review of these foundational skills will ensure they feel confident and prepared for Grade 1."
        ]
    },
    "Grade 1": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} is a gifted learner who has consistently displayed a strong grasp of all classroom topics this year. Their zest for learning is admirable and has been a wonderful inspiration to their classmates. They are exceptionally well-prepared for Grade 2.",
            "{name} has been a bright and well-organized student throughout the year, consistently showcasing a solid grasp of the concepts taught. Their excellent work habits and pride in their achievements will serve them well in Grade 2 and beyond."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} has shown consistent growth and a strong commitment to enhancing their abilities throughout Grade 1. To continue this impressive progress in Grade 2, it will be important to channel their enthusiasm for conversation into class discussions and to further develop their organizational skills.",
            "{name} is a bright and enthusiastic student who has maintained a keen interest in classroom activities all year. Their courteous demeanor has made them a valued member of our class community. They have built a strong foundation for Grade 2.",
            "{name} has worked diligently all year and has demonstrated commendable growth, particularly in their reading fluency. Their punctuality with homework assignments is a testament to their responsibility. They are ready for the challenges of Grade 2."
        ],
        "Rising, developing and Emerging students": [
            "{name} has shown a growing eagerness to embrace new knowledge throughout this school year. Consistent practice of foundational reading and math skills over the summer will be vital for a confident start to Grade 2.",
            "This year, {name} has made notable progress in their ability to work independently and follow classroom routines. As they prepare for Grade 2, a continued focus on developing concentration during lessons will be highly beneficial.",
            "{name} has worked to overcome challenges this year and has shown improvement in their writing skills. Further encouragement to express their ideas verbally and on paper will greatly support their transition into Grade 2."
        ]
    },
    "Grade 2": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} has been a fast learner all year, excelling in understanding and applying new concepts. Their enthusiasm is commendable. As they prepare for Grade 3, developing stronger organizational habits will be a key area for growth.",
            "{name} is a remarkable student who has consistently demonstrated a neat and well-organized approach to their work this year. They are intelligent and agile in their thinking. To continue their growth in Grade 3, they are encouraged to read widely and explore topics of personal interest.",
            "With a strong grasp of the Grade 2 curriculum, {name} consistently demonstrates critical thinking and problem-solving skills. Their positive attitude and collaborative spirit have been an asset to our class. They are more than ready for Grade 3."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} is a quiet and well-behaved student who has demonstrated a strong ability to grasp concepts quickly throughout the year. As they prepare for Grade 3, continuing to actively volunteer and engage more in class activities will build their confidence and communication skills.",
            "{name} has been a responsible and hardworking member of our class this year. They have made steady academic gains, especially in mathematics. Their respectful nature makes them a pleasure to teach, and they are well-prepared for Grade 3."
        ],
        "Rising, developing and Emerging students": [
            "{name} has been a quiet and obedient student who follows instructions and classroom rules. To ensure a strong start in Grade 3, a continued focus on improving the neatness of their handwriting and practicing math facts for fluency is highly recommended.",
            "Throughout the year, {name} has put effort into their learning and has shown progress, especially in reading comprehension. Building confidence to ask for help and participate more actively in discussions will be an important goal for Grade 3.",
            "{name} has worked hard to improve their spelling and writing this year. They should be proud of the progress they have made. A consistent summer reading routine will be very beneficial for their transition to Grade 3."
        ]
    },
    "Grade 3": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} has consistently demonstrated high self-confidence and an eagerness to engage in class activities throughout the year. Their positive approach to learning is commendable. They are well-prepared for the intellectual challenges of Grade 4.",
            "{name} is a thoughtful and analytical student who has excelled across all subject areas this year. They consistently produce high-quality work and have a strong ability to articulate their thinking. They are poised for a fantastic year in Grade 4."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} has a passion for learning and studies with enthusiasm. Their cooperative nature and respectful treatment of peers have been a constant positive force in our classroom this year. Continuing to practice reading for stamina will be crucial for success in Grade 4.",
            "{name} has shown respect towards their peers and engaged in class activities with a positive mindset, leading to notable progress across various subjects this year. Their potential for success in Grade 4 is high, especially with a continued focus on strengthening reading comprehension skills.",
            "Throughout the year, {name} has been a conscientious and reliable student. They have a good understanding of mathematical concepts and have worked hard to improve their writing. This dedication will be a great asset in Grade 4."
        ],
        "Rising, developing and Emerging students": [
            "{name} has shown promising growth in their academic and social skills this year. With continued encouragement as they enter Grade 4, they will become more confident and contribute more actively in the classroom.",
            "{name} has developed a stronger understanding of the curriculum this year. Focusing on active participation and developing consistent homework habits will be key to their continued success in Grade 4.",
            "It has been rewarding to see {name}'s progress this year, particularly in their willingness to work with others. As they move to Grade 4, it will be important to build their academic independence and time management skills."
        ]
    },
    "Grade 4": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} has been consistently polite, kind, and helpful to both peers and teachers throughout the year. Their confidence shines through in all school activities, and they are thoroughly prepared for the challenges and increased independence of Grade 5.",
            "{name} is a conscientious student who has consistently set high goals for themself and achieved great success this year. They exude confidence and take responsibility for their learning, making them a model student ready for Grade 5.",
            "{name} has been courteous, responsible, and a positive leader in our classroom this year. Their inspiring attitude and enthusiasm for learning will undoubtedly lead to continued success in Grade 5."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name}'s positive attitude and consistent effort in their studies this year are commendable. They have been a kind and responsible member of our class community, always ready to lend a helping hand. They have a solid foundation for Grade 5.",
            "{name}'s courteous and well-mannered behavior has been a hallmark of their year in Grade 4. By continuing to set clear academic goals, they will be well-equipped to meet the challenges of Grade 5 with direction and motivation.",
            "{name} has shown significant improvement in their organizational skills and work habits this year. They are a responsible student who works well with others. This growth has prepared them well for the demands of Grade 5."
        ],
        "Rising, developing and Emerging students": [
            "{name} has gradually built their confidence in class discussions this year. Continued encouragement to share their ideas and ask questions will be highly beneficial for their transition into Grade 5.",
            "{name} has made encouraging progress in their organizational skills and task management this year. Maintaining these habits and applying them to long-term projects will be a key to their success in Grade 5.",
            "This year, {name} has worked to develop their writing skills and has shown progress in constructing paragraphs. Continued focus on reading and writing over the summer will provide a stronger foundation for the literacy demands of Grade 5."
        ]
    },
    "Grade 5": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} has consistently demonstrated a strong understanding of the curriculum this year. Their analytical skills are commendable. Their active participation and intellectual curiosity show a strong readiness for the challenges of Grade 6.",
            "{name} is a proactive learner who has taken great initiative in both individual and group tasks all year. Their ability to collaborate effectively is a significant asset that will serve them well as they move to Grade 6.",
            "{name} exhibits a keen interest in all subjects and has excelled this year. Their outstanding problem-solving abilities and creativity indicate a high potential for success in Grade 6 and beyond.",
            "{name} is a highly motivated learner with excellent time management skills. Their ability to balance academic responsibilities with extracurricular commitments has been impressive this year and shows a level of maturity that will be a great asset in Grade 6."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} has shown remarkable improvement in their academic performance this year. Their dedication to completing assignments on time and seeking help when needed has been impressive. This commitment will undoubtedly lead to success in Grade 6.",
            "{name} is a responsible and dependable student who has maintained high standards in their work all year. Their positive attitude and willingness to help others contribute to a supportive classroom environment. They are well-prepared for Grade 6.",
            "{name} has worked diligently throughout Grade 5, showing particular growth in their research and presentation skills. They are a cooperative student who can be counted on to do their part. They have built a solid foundation for the coming school year."
        ],
        "Rising, developing and Emerging students": [
            "{name} has developed a greater interest in class activities and discussions as the year has progressed. With continued encouragement in Grade 6, they will build greater confidence and academic independence.",
            "{name} has made steady progress in their studies this year. Focusing on building stronger and more independent study habits over the summer will help them achieve their full potential in the more demanding environment of Grade 6.",
            "This year, {name} has improved in their ability to manage multi-step assignments. They should be proud of this growth. For a successful transition to Grade 6, a continued focus on organization and planning for long-term projects is recommended."
        ]
    },
    "Grade 6": {
        "Exemplary, High Achievers Outstanding students": [
            "{name} has shown outstanding academic performance throughout the year. Their ability to grasp complex concepts and apply them effectively indicates a strong readiness for the academic challenges of Grade 7.",
            "{name} is a diligent student who has consistently produced excellent work all year. Their attention to detail and commitment to deep understanding are commendable. They are well-prepared for a successful transition to the next stage of their education.",
            "{name} has demonstrated a high level of maturity and responsibility in all aspects of their schoolwork this year. Their ability to manage time effectively is exemplary and shows they are ready for the increased independence of Grade 7.",
            "{name} is a highly motivated learner who excels in both individual and group settings. Their leadership qualities, insightful contributions, and passion for learning have been an asset to our class, and they are exceptionally well-prepared for Grade 7."
        ],
        "Steady and Competent and Accomplished Achievers": [
            "{name} is a respectful and cooperative student who has consistently upheld classroom standards all year. Their ability to work harmoniously with others and their steady effort have prepared them well for the collaborative demands of Grade 7.",
            "{name} has shown significant growth in their academic performance this year. Their perseverance and dedication to overcoming challenges are admirable. These qualities, combined with a continued focus on communication skills, will ensure their success in Grade 7.",
            "{name} has been a responsible and hardworking student throughout Grade 6. They consistently met deadlines and showed a genuine desire to learn. They have built a solid foundation of knowledge and skills to take with them to Grade 7."
        ],
        "Rising, developing and Emerging students": [
            "{name} has made gradual and steady improvement in their academic performance this year. With continued support and by focusing on proactive self-advocacy in Grade 7, they will continue to build greater confidence and success.",
            "{name} has begun to engage more actively in class activities this year, and this has positively impacted their learning. As they transition to Grade 7, making a concerted effort to stay organized and manage their time effectively will be crucial.",
            "Throughout Grade 6, {name} has worked to improve their study habits and take greater ownership of their learning. They should be proud of their progress. Continued development of these skills will be essential for navigating the increased workload of Grade 7."
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
                st.markdown(f"**EXAMPLE {i}:**")
                st.write(comment_text)
                st.markdown("---")


add_footer()
