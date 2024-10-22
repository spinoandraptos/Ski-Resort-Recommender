from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for ski resorts
resorts_data = {
    'beginner': ['Resort A', 'Resort B'],
    'intermediate': ['Resort C', 'Resort D'],
    'advanced': ['Resort E', 'Resort F']
}

@app.route('/', methods=['GET', 'POST'])
def index():
    resorts = []
    if request.method == 'POST':
        skill_level = request.form.get('skill_level')
        location = request.form.get('location')  # You can use this for filtering in a real application
        resorts = resorts_data.get(skill_level, [])
    return render_template('index.html', resorts=resorts)

if __name__ == '__main__':
    app.run(debug=True)