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

namespace WpfAppNotepad
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class Window1 : Window
    {
        public Window1()
        {

            System.Threading.Thread.CurrentThread.CurrentUICulture =
            new System.Globalization.CultureInfo("sv-SE");

            InitializeComponent();
        }


        private void Increase_button_Click(object sender, RoutedEventArgs e)
        {
            textBlock1.FontSize++; 
        }

        private void Decrease_button_Click(object sender, RoutedEventArgs e)
        {
            textBlock1.FontSize--;
        }

        private void OK_button_Click(object sender, RoutedEventArgs e)
        {
            DialogResult = true;

            Close();

        }
    }
}
