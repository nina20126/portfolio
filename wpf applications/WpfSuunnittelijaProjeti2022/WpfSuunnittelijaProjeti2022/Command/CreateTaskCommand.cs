﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using WpfSuunnittelijaProjeti2022.ViewModel;

namespace WpfSuunnittelijaProjeti2022.Command
{
    public class CreateTaskCommand : ICommand
    {
        public event EventHandler? CanExecuteChanged;

        public bool CanExecute(object? parameter)
        {
            return true;
        }

        public void Execute(object? parameter)
        {
            if (parameter is  TaskListViewModel taskList)
            {
                taskList.Tasks.Add(new TaskViewModel() { Name = taskList.TaskName, Complete= false });
            }
        }
    }
}
