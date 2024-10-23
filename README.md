<h1>Resume Screening App With Python and SQL</h1>

<p>This is a simple web-based application for resume screening, built using <strong>Streamlit</strong>, <strong>Scikit-learn</strong>, and <strong>NLTK</strong>. It takes a resume file (either in <code>.txt</code> or <code>.pdf</code> format), cleans the text, and classifies the resume into one of several predefined job categories such as "Data Science," "Java Developer," and others. The app uses a pre-trained machine learning model based on <code>TfidfVectorizer</code> and <code>KNeighborsClassifier</code> for classification.</p>

<h2>Features</h2>
<ul>
    <li><strong>File Upload</strong>: Supports both <code>.txt</code> and <code>.pdf</code> resume files.</li>
    <li><strong>Text Cleaning</strong>: Automatically cleans and preprocesses the resume text (removes URLs, special characters, and redundant spaces).</li>
    <li><strong>Resume Classification</strong>: Predicts the job category based on the resume content.</li>
    <li><strong>Interactive Interface</strong>: Built with Streamlit for easy interaction.</li>
</ul>

<h2>Installation</h2>

<p>To run this application on your local machine, follow the steps below:</p>

<h3>1. Clone the repository:</h3>

<pre><code>git clone https://github.com/your-username/resume-screening-app.git
cd resume-screening-app
</code></pre>

<h3>2. Install dependencies:</h3>

<p>Create a virtual environment (optional but recommended):</p>

<pre><code>python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
</code></pre>

<p>Install the required packages:</p>

<pre><code>pip install -r requirements.txt
</code></pre>

<h3>3. Download NLTK data:</h3>

<p>The app requires some NLTK data for text processing. Run the following Python script to download the necessary packages:</p>

<pre><code>import nltk
nltk.download('punkt')
nltk.download('stopwords')
</code></pre>

<h3>4. Run the app:</h3>

<pre><code>streamlit run app.py
</code></pre>

<p>The app will open in your browser at <a href="http://localhost:8501">http://localhost:8501</a>.</p>

<h2>Usage</h2>

<ol>
    <li>Upload a resume in either <code>.txt</code> or <code>.pdf</code> format using the file uploader.</li>
    <li>The app will preprocess the resume and classify it into one of the predefined categories.</li>
    <li>The predicted category will be displayed on the screen.</li>
</ol>

<h2>Models</h2>

<p>The app uses the following models:</p>

<ul>
    <li><strong>TfidfVectorizer</strong>: For transforming resume text into numerical features.</li>
    <li><strong>KNeighborsClassifier</strong>: For classifying the resume into predefined categories.</li>
</ul>

<h2>Category Mapping</h2>

<p>The app supports the following job categories:</p>

<table>
    <tr>
        <th>ID</th>
        <th>Job Category</th>
    </tr>
    <tr><td>0</td><td>Advocate</td></tr>
    <tr><td>1</td><td>Arts</td></tr>
    <tr><td>2</td><td>Automation Testing</td></tr>
    <tr><td>3</td><td>Blockchain</td></tr>
    <tr><td>4</td><td>Business Analyst</td></tr>
    <tr><td>5</td><td>Civil Engineer</td></tr>
    <tr><td>6</td><td>Data Science</td></tr>
    <tr><td>7</td><td>Database</td></tr>
    <tr><td>8</td><td>DevOps Engineer</td></tr>
    <tr><td>9</td><td>DotNet Developer</td></tr>
    <tr><td>10</td><td>ETL Developer</td></tr>
    <tr><td>11</td><td>Electrical Engineering</td></tr>
    <tr><td>12</td><td>HR</td></tr>
    <tr><td>13</td><td>Hadoop</td></tr>
    <tr><td>14</td><td>Health and Fitness</td></tr>
    <tr><td>15</td><td>Java Developer</td></tr>
    <tr><td>16</td><td>Mechanical Engineer</td></tr>
    <tr><td>17</td><td>Network Security Engineer</td></tr>
    <tr><td>18</td><td>Operations Manager</td></tr>
    <tr><td>19</td><td>PMO</td></tr>
    <tr><td>20</td><td>Python Developer</td></tr>
    <tr><td>21</td><td>SAP Developer</td></tr>
    <tr><td>22</td><td>Sales</td></tr>
    <tr><td>23</td><td>Testing</td></tr>
    <tr><td>24</td><td>Web Designing</td></tr>
</table>

<h2>Files</h2>

<ul>
    <li><code>app.py</code>: The main file that runs the Streamlit app.</li>
    <li><code>tfidf.pkl</code>: Pre-trained TF-IDF vectorizer.</li>
    <li><code>clf.pkl</code>: Pre-trained KNeighborsClassifier model.</li>
    <li><code>requirements.txt</code>: List of required packages.</li>
</ul>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Contributing</h2>

<p>Feel free to submit issues or pull requests if you have any suggestions for improvements or new features!</p>

<h2>Contact</h2>

<p>For any questions or issues, please contact:</p>

<ul>
    <li><strong>Imaad Sharieff</strong> - imaadsharieff266@gmail.com</li>
</ul>
