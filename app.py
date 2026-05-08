from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        tasks.append({"task": task, "done": False})
        return redirect('/')

    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect('/')

@app.route('/complete/<int:index>')
def complete(index):
    tasks[index]['done'] = True
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
