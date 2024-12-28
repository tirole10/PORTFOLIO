import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Portfolio | Prachi Tirole",
    page_icon="✨",
    layout="wide",
)

# Inject Custom CSS
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(90deg, #ff7e5f, #feb47b);
        font-family: 'Arial', sans-serif;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #333333;
    }
    h1, h2, h3 {
        color: white;
    }
    .section {
        background-color: rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .button {
        background-color: #ff7e5f;
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
    }
    .button:hover {
        background-color: #feb47b;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("Portfolio Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Contact"])

# Home Page
if page == "Home":
    st.markdown("<h1 class='main-title'>✨ Welcome to My Portfolio ✨</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="section">
            <h2>Hello, I'm <strong>Prachi Tirole</strong> 👋</h2>
            <p>
                I'm a <strong>Software Developer</strong> passionate about <strong>web development and AI</strong>.
                Welcome to my portfolio, where you can explore my projects, skills, and contact me!
            </p>
            <p><strong>Quick Links:</strong></p>
            <ul>
                <li><a href="https://github.com/tirole10" target="_blank">GitHub</a></li>
                <li><a href="https://linkedin.com/in/prachi-tirole-84aa60256" target="_blank">LinkedIn</a></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Projects Page
elif page == "Projects":
    st.markdown("<h1 class='main-title'>📂 My Projects</h1>", unsafe_allow_html=True)
    
    # Resume Radar Project Section
    st.markdown(
        """
        <div class="section">
            <h2>Project 1: <a href="https://github.com/yourproject" target="_blank">Resume Radar</a></h2>
            <p>An ATS Resume Expert built with Python, Streamlit, Google Gemini API, PyPDF2, JSON, and dotenv. This web app helps job seekers optimize their resumes for Applicant Tracking Systems (ATS). By analyzing resume content, it provides personalized recommendations to enhance compatibility with ATS, increasing the chances of getting noticed by recruiters. It's a valuable tool for anyone looking to improve their resume for job applications.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Expander for "View More" Details
    if st.button('View More Details'):
        st.markdown(
            """
            <h3>Features:</h3>
            <ul>
                <li><strong>ATS Compatibility:</strong> Analyzes and optimizes resumes to ensure compatibility with Applicant Tracking Systems (ATS).</li>
                <li><strong>Real-time Feedback:</strong> Provides immediate suggestions for improving your resume’s ATS readability and keyword optimization.</li>
                <li><strong>PDF Resume Support:</strong> Supports PDF uploads, extracting text for analysis and feedback.</li>
                <li><strong>Custom Recommendations:</strong> Offers personalized recommendations based on the resume content to improve job application success.</li>
            </ul>
            
            <h3>Technologies Used:</h3>
            <ul>
                <li><strong>Python:</strong> Core programming language for developing the backend logic.</li>
                <li><strong>Streamlit:</strong> Web framework used to create the interactive and user-friendly frontend.</li>
                <li><strong>Google Gemini API:</strong> Integrated for smart resume analysis and intelligent feedback generation.</li>
                <li><strong>PyPDF2:</strong> Library used to extract text from uploaded PDF resumes.</li>
                <li><strong>JSON:</strong> Used for managing configurations and data exchange.</li>
                <li><strong>dotenv:</strong> Helps manage environment variables securely.</li>
            </ul>

            <h3>Future Work:</h3>
            <ul>
                <li><strong>AI Resume Scoring:</strong> Plan to integrate AI algorithms to score resumes based on ATS compatibility and industry standards.</li>
                <li><strong>User Interface Improvements:</strong> Enhancing the visual design and user experience for better interaction.</li>
                <li><strong>Multi-File Support:</strong> Enabling batch processing of multiple resumes for users who wish to upload and analyze more than one resume at once.</li>
            </ul>

            <h3>How to Use:</h3>
            <ul>
                <li><strong>Upload Your Resume:</strong> Upload your resume in PDF format to start the analysis.</li>
                <li><strong>Receive Feedback:</strong> Get instant feedback with suggestions on how to optimize your resume for ATS.</li>
                <li><strong>Download Optimized Resume:</strong> Download your improved resume, ready for submission to job portals and recruiters.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # Emotion Leverage Project Section
    st.markdown(
        """
        <div class="section">
            <h2>Project 2: <a href="https://github.com/yourproject" target="_blank">Emotion Leverage</a></h2>
            <p>An Emotion Detection system built with TensorFlow, Keras, OpenCV, scikit-learn, and TQDM. This web app analyzes facial expressions from images or video streams to detect emotions such as happiness, sadness, anger, fear, and more. By leveraging deep learning models and real-time image processing, it provides accurate emotion recognition for applications in psychological research, customer feedback systems, and human-computer interaction. A valuable tool for analyzing emotional responses and enhancing user experience in various domains.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Expander for "View More" Details
    # Emotion Leverage Project Section
    if st.button('View More Details', key='view_more_emotion_leverage'):
        st.markdown(
        """
        <h3>Features:</h3>
        <ul>
            <li><strong>Real-time Emotion Detection:</strong> Detects emotions in real-time from images or video streams.</li>
            <li><strong>Emotion Recognition:</strong> Identifies emotions like happiness, sadness, anger, fear, surprise, and disgust.</li>
            <li><strong>High Accuracy:</strong> Deep learning models trained on large datasets for accurate emotion classification.</li>
        </ul>
        
        <h3>Technologies Used:</h3>
        <ul>
            <li><strong>TensorFlow & Keras:</strong> For emotion detection via deep learning models.</li>
            <li><strong>OpenCV:</strong> For real-time image processing and face detection.</li>
            <li><strong>scikit-learn:</strong> For model evaluation and performance optimization.</li>
            <li><strong>NumPy & Pandas:</strong> For data preprocessing and manipulation.</li>
            <li><strong>TQDM:</strong> Helps in visualizing the training progress and making the model training more efficient.</li>
        </ul>

        <h3>Future Work:</h3>
        <ul>
            <li><strong>Multi-Facial Detection:</strong> Detect emotions from multiple faces in a single frame.</li>
            <li><strong>Emotion Analytics:</strong> Aggregate emotional data for market research or sentiment analysis.</li>
        </ul>

        <h3>How to Use:</h3>
        <ul>
            <li><strong>Upload Image/Start Webcam:</strong> Upload an image or enable webcam to detect emotions.</li>
            <li><strong>Receive Feedback:</strong> Get instant emotion recognition from facial expressions.</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # Other project sections
    st.markdown(
        """
        <div class="section">
            <h2>Project 3: <a href="https://github.com/yourproject" target="_blank">Lumen AI</a></h2>
            <p>A brief description of Project 3.</p>
            <button class="button">View More</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Skills Page
elif page == "Skills":
    st.markdown("<h1 class='main-title'>🛠️ My Skills</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="section">
            <ul>
                <li><strong>Programming:</strong> Python, C++</li>
                <li><strong>Frameworks:</strong> Streamlit, Numpy, Pandas, Tensorflow, Keras, API Integration</li>
                <li><strong>Tools:</strong> VS Code, Jupyter, Pycharm, Github</li>
                <li><strong>Databases:</strong> MySQL</li>
                <li><strong>Soft Skills:</strong> Problem-solving, Teamwork, Communication</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Contact Page
elif page == "Contact":
    st.markdown("<h1 class='main-title'>📬 Get in Touch</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="section">
             <h3>Feel free to reach out to me!</h3>
            <p><strong>Email:</strong> <a href="prachitirole10@gmail.com">prachitirole10@gmail.com</a></p>
            <p><strong>LinkedIn:</strong> <a href="https://linkedin.com/in/prachi-tirole-84aa60256" target="_blank">LinkedIn</a></p>
            <p><strong>GitHub:</strong> <a href="https://github.com/tirole10" target="_blank"> GitHub</a></p>
            <p><strong>GFG:</strong> <a href="https://www.geeksforgeeks.org/user/prachiti2os6/" target="_blank"> GeeksforGeeks</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.sidebar.write("✨ Thank you for visiting! ✨")
