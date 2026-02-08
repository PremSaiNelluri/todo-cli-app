def delete_task(tasks, index):
    tasks.pop(index)  # Bug: index should be index-1

