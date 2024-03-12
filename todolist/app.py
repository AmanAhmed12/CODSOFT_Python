from flask import Flask, render_template, request, redirect, url_for, flash
from mysql.connector.errors import IntegrityError
import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="", database="todolist")

if connection.is_connected():
    print("connected successfully..")
else:
    print("Failed to connect...")

app = Flask(__name__)
app.secret_key = 'AmaanAhmed'





@app.route('/')
def index():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT taskid, taskname, status FROM tasks")
        tasks_data = cursor.fetchall()
        cursor.close()
        return render_template('index.html', task=tasks_data)

    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for('index'))
    

@app.route('/updateInfo', methods=['POST'])
def updateInfo():
     s_oldid=request.form.get('taskidold')
     s_newid=request.form.get('taskid')
     s_newname=request.form.get('task')
     cursor = connection.cursor()
     sql = "UPDATE tasks SET taskid = %s ,taskname=%s WHERE taskid = %s"
     cursor.execute(sql, (s_newid,s_newname, s_oldid))
     connection.commit()
     cursor.close()
     flash("Task updated Successfully !!!", "success")
     return redirect(url_for('update'))
  
    

@app.route('/updated', methods=['GET'])
def updated():
    taskid = request.args.get('taskid')
    taskname = request.args.get('taskname')
    return render_template('update.html', taskid=taskid, taskname=taskname)
    

@app.route('/update')
def update():
   return render_template('update.html')


@app.route('/add', methods=['POST'])
def add_task():
    try:
        s_taskid = request.form.get('taskid')
        s_task = request.form.get('task')

        # Perform validation
        if not s_taskid or not s_task:
            flash("All fields are required", "error")
            return redirect(url_for('index'))

        cursor = connection.cursor()
        sql = "INSERT INTO tasks(taskid, taskname, status) VALUES (%s, %s, %s)"
        val = (s_taskid, s_task, "In-progress")
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        flash("Task Added Successfully !!!", "success")
        return redirect(url_for('index'))

    except IntegrityError as e:
        flash("ID Already Exists!", "error")
        return redirect(url_for('index'))

    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for('index'))
    


    
@app.route('/update_task_status/<string:taskid>/<string:action>', methods=['POST'])
def update_task_status(taskid, action):
    try:
        cursor = connection.cursor()
        if action == 'complete':
            sql = "UPDATE tasks SET status = %s WHERE taskid = %s"
            cursor.execute(sql, ("complete", taskid))
            connection.commit()
            cursor.close()
            return redirect(url_for('index'))
        elif action == 'delete':
            sql = "DELETE FROM tasks WHERE taskid = %s"
            cursor.execute(sql, (taskid,))
            connection.commit()
            cursor.close()
            return redirect(url_for('index'))
        elif action == 'incomplete':
            sql = "UPDATE tasks SET status = %s WHERE taskid = %s"
            cursor.execute(sql, ("In-progress", taskid))
            connection.commit()
            cursor.close()
            return redirect(url_for('index'))
        elif action == 'update':
            return redirect(url_for('update'))
        else:
            # Handle invalid action
            flash("Invalid action", "error")
            return redirect(url_for('index'))
    except Exception as e:
        flash("An error occurred: " + str(e), "error")
        return redirect(url_for('index'))



   
if __name__ == '__main__':
    app.run(debug=True)
