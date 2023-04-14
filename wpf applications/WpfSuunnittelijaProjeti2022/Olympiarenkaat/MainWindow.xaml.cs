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

namespace WpfAppOlympiaRenkaat
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Canvas.SetLeft(blue, 0);
            Canvas.SetTop(yellow, 310);
            Canvas.SetTop(black, 0);
            Canvas.SetTop(green, 310);
            Canvas.SetLeft(red, 500);
        }

        private void fix_Click(object sender, RoutedEventArgs e)
        {
            Canvas.SetLeft(blue, 160);
            Canvas.SetTop(blue, 107);
            Canvas.SetLeft(yellow, 222);
            Canvas.SetTop(yellow, 157);
            Canvas.SetLeft(black, 289);
            Canvas.SetTop(black, 107);
            Canvas.SetLeft(green, 351);
            Canvas.SetTop(green, 157);
            Canvas.SetLeft(red, 416);
            Canvas.SetTop(red, 107);
        }

        private void _new_Click(object sender, RoutedEventArgs e)
        {
            Window1 mywindow = new Window1();

            mywindow.ShowDialog();
        }
    }
}
