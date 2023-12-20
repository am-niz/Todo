def edit_task(tasks, task_index, new_task):
    tasks[task_index - 1]['title'] = new_task
    print("Task edited successfully.")