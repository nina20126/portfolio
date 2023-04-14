using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace WpfSuunnittelijaProjeti2022
{
    /// <summary>
    /// Interaction logic for Monday.xaml
    /// </summary>
    public partial class Monday : Window
    {
        public Monday()
        {
            InitializeComponent();
        }

        // SAVE
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Properties.Settings1.Default.noteMon = monNote.Text;
            Properties.Settings1.Default.Save();
        }

        // CLEAR
        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            monNote.Text = "Plan your day!";


            Properties.Settings1.Default.noteMon = monNote.Text;
            Properties.Settings1.Default.Save();
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            monNote.Text = Properties.Settings1.Default.noteMon;

        }
    }
}
