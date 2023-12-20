def delete_task(tasks, task_index):        
    deleted_task = tasks.pop(task_index - 1)
    print(f"Task '{deleted_task['title']}' deleted successfully.")
