from flask import Flask, render_template, json
from datetime import datetime
import os

app = Flask(__name__)

# 加载项目数据
def load_projects():
    try:
        with open(os.path.join(app.root_path, 'content', 'projects.json')) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

@app.context_processor
def inject_common_variables():
    return {
        'projects': load_projects(),
        'now': datetime.now(),
        'config': app.config
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)