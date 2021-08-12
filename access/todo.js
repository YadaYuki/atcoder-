// Step1: dumpTaskの実装
function dumpTask(task) {
  const taskStateStr = task.checked ? "[x]" : "[ ]";
  return `${taskStateStr} ${task.title}`;
}

// Step2: dumpTasksの実装
function dumpTasks(tasks, excludeChecked) {
  const taskList = [];
  tasks.map((task) => {
    if (excludeChecked == true) {
      if (task.checked == false) {
        taskList.push(dumpTask(task));
      }
    }
    if (excludeChecked === false) {
      taskList.push(dumpTask(task));
    }
  });
  return taskList;
}

// Step3: addTaskの実装
function addTask(newTask, tasks) {
  tasks.push(newTask);
}

// Step4: checkTaskの実装
function checkTask(title, tasks) {
  for (let task of tasks) {
    if (task.title === title) {
      task.checked = true;
    }
  }
}

// Step5: uncheckTaskの実装
function uncheckTask(title, tasks) {
  for (let task of tasks) {
    if (task.title === title) {
      task.checked = false;
    }
  }
}

// Step6: deleteTaskの実装
function deleteTask(title, tasks) {
  for (let i in tasks) {
    if (tasks[i].title === title) {
      tasks.splice(i, 1);
    }
  }
}

// Step7: sortedTaskの実装
function sortedTasks(tasks, excludeChecked) {
  const sorter = (a, b) => {
    if(a.priority === b.priority){
      const aTitle = a.title.toString().toLowerCase();
      const bTitle = b.title.toString().toLowerCase();
      if(aTitle < bTitle){
          return -1;
      }else if(aTitle > bTitle){
          return 1;
      }
      return 0;
    }
    return a.priority - b.priority;
  };
  if (excludeChecked == true) {
    tasks = tasks.filter((task) => {
      return !task.checked;
    });
  }
  tasks.sort(sorter);
  return dumpTasks(tasks,excludeChecked)
}


exports.dumpTask = dumpTask;
exports.dumpTasks = dumpTasks;
exports.addTask = addTask;
exports.checkTask = checkTask;
exports.uncheckTask = uncheckTask;
exports.deleteTask = deleteTask;
exports.sortedTasks = sortedTasks;


var tasks = [{
  title: "Atring",
  checked: true,
  priority: 12
},{
  title: "Atring",
  checked: true,
  priority:12
},{
  title: "String",
  checked: true,
  priority: 12
}];

console.log(sortedTasks(tasks,false))

