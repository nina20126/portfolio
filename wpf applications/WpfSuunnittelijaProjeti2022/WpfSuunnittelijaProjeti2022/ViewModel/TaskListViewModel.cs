﻿using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Collections.Specialized;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using WpfSuunnittelijaProjeti2022.Command;

namespace WpfSuunnittelijaProjeti2022.ViewModel
{
    public class TaskListViewModel : INotifyPropertyChanged
    {
        private ObservableCollection<TaskViewModel> tasks = new ObservableCollection<TaskViewModel>();
        public ObservableCollection<TaskViewModel> Tasks {
            get { return tasks; }
            set { 
                if (tasks != value)
                {
                    tasks = value;
                    NotifyPropertyChanged(nameof(Tasks));
                }
                
            }
        }
        public string TaskName { get; set; }
        public ICommand CreateTaskCommand { get { return new CreateTaskCommand(); } }

        public event PropertyChangedEventHandler? PropertyChanged;

        private void NotifyPropertyChanged(String name)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
        }
    }
}
