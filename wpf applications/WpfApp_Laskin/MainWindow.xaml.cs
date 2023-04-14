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
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApp_Laskin
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {

        int sum = 0;
        int number = 0;

        public MainWindow()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, RoutedEventArgs e)
        {
            number = 1;
            textBox.Text = number.ToString();

            sum = sum + number;
        }

        private void button2_Click(object sender, RoutedEventArgs e)
        {
            number = 2;
            textBox.Text = number.ToString();

            sum = sum + number;
        }

        private void button3_Click(object sender, RoutedEventArgs e)
        {
            number = 3;
            textBox.Text = number.ToString();

            sum = sum + number;
        }

        private void button4_Click(object sender, RoutedEventArgs e)
        {
            number = 4;
            textBox.Text = number.ToString();

            sum = sum + number;
        }

        private void button5_Click(object sender, RoutedEventArgs e)
        {
            number = 5;
            textBox.Text = number.ToString();

            sum = sum + number;
        }

        private void button6_Click(object sender, RoutedEventArgs e)
        {
            number = 6;
            textBox.Text = number.ToString();

            sum = sum + number;
        }

        private void button7_Click(object sender, RoutedEventArgs e)
        {
            number = 7;
            textBox.Text = number.ToString();

            sum = sum + number;
        }

        private void button8_Click(object sender, RoutedEventArgs e)
        {
            number = 8;
            textBox.Text = number.ToString();

            sum = sum + number;
        }

        private void button9_Click(object sender, RoutedEventArgs e)
        {
            number = 9;
            textBox.Text = number.ToString();

            sum = sum + number;
        }

        private void buttonEqual_Click(object sender, RoutedEventArgs e)
        {
            textBox.Text = sum.ToString();
            sum = 0;
        }
    }
}
