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
using System.Windows.Media.Effects;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using WpfSuunnittelijaProjeti2022.ViewModel;

namespace WpfSuunnittelijaProjeti2022
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        Random rand;

        //List<string> mothsList = new List<string>();

        public MainWindow()
        {
            InitializeComponent();
            var tasks = new TaskListViewModel();
            tasks.Tasks.Add(new TaskViewModel() { Name = "Task 1", Complete = false });
            tasks.Tasks.Add(new TaskViewModel() { Name = "Task 2", Complete = true });
            this.DataContext = tasks;

            rand= new Random();

            //mothsList.Add("January");
            //mothsList.Add("February");
            //mothsList.Add("March");
            //mothsList.Add("April");
            //mothsList.Add("May");
            //mothsList.Add("June");
           // mothsList.Add("July");
            //mothsList.Add("August");
            //mothsList.Add("September");
            //mothsList.Add("October");
            //mothsList.Add("November");
            //mothsList.Add("December");

            //MonthsCombo.ItemsSource = mothsList;
        }

        private byte[] GetRandomBytes(int n)
        {
            var randomBytes = new byte[n];
            rand.NextBytes(randomBytes);
            return randomBytes;
        }

        private void Save_Click(object sender, RoutedEventArgs e)
        {
            Properties.Settings1.Default.textMon = MonTextBox.Text;
            Properties.Settings1.Default.Save();

            Properties.Settings1.Default.textTue = TueTextBox.Text;
            Properties.Settings1.Default.Save();

            Properties.Settings1.Default.textWed = WedTextBox.Text;
            Properties.Settings1.Default.Save();

            Properties.Settings1.Default.textThu = ThuTextBox.Text;
            Properties.Settings1.Default.Save();

            Properties.Settings1.Default.textFri = FriTextBox.Text;
            Properties.Settings1.Default.Save();

            Properties.Settings1.Default.textSat = SatTextBox.Text;
            Properties.Settings1.Default.Save();

            Properties.Settings1.Default.textSun = SatTextBox.Text;
            Properties.Settings1.Default.Save();
        }

        private void Exit_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }

        // Weekly Schedule where user can write something
        private void ResetButton_Click(object sender, RoutedEventArgs e)
        {
            MonTextBox.Background = Brushes.White;
            MonTextBox.Text = "Important today:";

            TueTextBox.Background = Brushes.White;
            TueTextBox.Text = "Important today:";

            WedTextBox.Background = Brushes.White;
            WedTextBox.Text = "Important today:";

            ThuTextBox.Background = Brushes.White;
            ThuTextBox.Text = "Important today:";

            FriTextBox.Background = Brushes.White;
            FriTextBox.Text = "Important today:";

            SatTextBox.Background = Brushes.White;
            SatTextBox.Text = "Important today:";

            SunTextBox.Background = Brushes.White;
            SunTextBox.Text = "Important today:";
        }

        // Open monday in detail
        private void OpenMonButton_Click(object sender, RoutedEventArgs e)
        {
            Monday mywindow= new Monday();

            mywindow.ImportantTextBlock.Text = MonTextBox.Text;

            mywindow.ShowDialog();
        }

        // Button Click me! changes the color of the title
        private void ChangeTitleButton_Click(object sender, RoutedEventArgs e)
        {
            byte[] rgb = GetRandomBytes(3);

            var randomColorBrush = new SolidColorBrush(Color.FromArgb(255, rgb[0], rgb[1], rgb[2]));

            //TitleText.Foreground = randomColorBrush;
            textBlockMon.Foreground= randomColorBrush;
            textBlockThu.Foreground= randomColorBrush;
            textBlockTue.Foreground= randomColorBrush;
            textBlockWed.Foreground= randomColorBrush;
            textBlockFri.Foreground= randomColorBrush;
            textBlockSat.Foreground= randomColorBrush;
            textBlockSun.Foreground= randomColorBrush;
        }

        // SAVE Button
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Properties.Settings1.Default.textMon = MonTextBox.Text;
            Properties.Settings1.Default.Save();

            Properties.Settings1.Default.textTue = TueTextBox.Text;
            Properties.Settings1.Default.Save();

            Properties.Settings1.Default.textWed = WedTextBox.Text;
            Properties.Settings1.Default.Save();

            Properties.Settings1.Default.textThu = ThuTextBox.Text;
            Properties.Settings1.Default.Save();

            Properties.Settings1.Default.textFri = FriTextBox.Text;
            Properties.Settings1.Default.Save();

            Properties.Settings1.Default.textSat = SatTextBox.Text;
            Properties.Settings1.Default.Save();

            Properties.Settings1.Default.textSun= SatTextBox.Text;
            Properties.Settings1.Default.Save();
        }

        
        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            MonTextBox.Text = Properties.Settings1.Default.textMon;

            TueTextBox.Text = Properties.Settings1.Default.textTue;

            WedTextBox.Text = Properties.Settings1.Default.textWed;

            ThuTextBox.Text = Properties.Settings1.Default.textThu;

            FriTextBox.Text = Properties.Settings1.Default.textFri;

            SatTextBox.Text = Properties.Settings1.Default.textSat;

            SunTextBox.Text = Properties.Settings1.Default.textSun;
        }

        private void Window_Closed(object sender, EventArgs e)
        {
            MessageBox.Show("See you soon!");
        }

        // Open Draw-application
        private void MenuItem_Click(object sender, RoutedEventArgs e)
        {
            Draw myDraw = new Draw();

            myDraw.ShowDialog();
        }

        // NOTEPAD project reference
        private void MenuItem_Click_1(object sender, RoutedEventArgs e)
        {
            WpfAppNotepad.MainWindow notepadWindow = new();
            notepadWindow.ShowDialog();
        }

        // OLYMPIC RINGS project reference
        private void olympicrings_Click(object sender, RoutedEventArgs e)
        {
            WpfAppOlympiaRenkaat.MainWindow olympicRingsWindow = new();
            olympicRingsWindow.ShowDialog();
        }

        // CALCULATOR project reference
        private void calculator_Click(object sender, RoutedEventArgs e)
        {
            WpfApp_Laskin.MainWindow olympicRingsWindow = new();
            olympicRingsWindow.ShowDialog();
        }

        // Dropdown Colors change Starst here!

        private void ComboBoxItem_Selected(object sender, RoutedEventArgs e)
        {
            TitleText.Foreground= new SolidColorBrush(Colors.Blue);
        }

        private void ComboBoxItem_Selected_1(object sender, RoutedEventArgs e)
        {
            TitleText.Foreground = new SolidColorBrush(Colors.LightBlue);
        }

        private void ComboBoxItem_Selected_2(object sender, RoutedEventArgs e)
        {
            TitleText.Foreground = new SolidColorBrush(Colors.Gold);
        }

        private void ComboBoxItem_Selected_3(object sender, RoutedEventArgs e)
        {
            TitleText.Foreground = new SolidColorBrush(Colors.GreenYellow);
        }

        private void ComboBoxItem_Selected_4(object sender, RoutedEventArgs e)
        {
            TitleText.Foreground = new SolidColorBrush(Colors.Aquamarine);
        }

        private void ComboBoxItem_Selected_5(object sender, RoutedEventArgs e)
        {
            TitleText.Foreground = new SolidColorBrush(Colors.SeaGreen);
        }

        private void ComboBoxItem_Selected_6(object sender, RoutedEventArgs e)
        {
            TitleText.Foreground = new SolidColorBrush(Colors.BurlyWood);
        }

        private void ComboBoxItem_Selected_7(object sender, RoutedEventArgs e)
        {
            TitleText.Foreground = new SolidColorBrush(Colors.LightSteelBlue);
        }

        private void ComboBoxItem_Selected_8(object sender, RoutedEventArgs e)
        {
            TitleText.Foreground = new SolidColorBrush(Colors.DeepPink);
        }

        private void ComboBoxItem_Selected_9(object sender, RoutedEventArgs e)
        {
            TitleText.Foreground = new SolidColorBrush(Colors.Thistle);
        }

        private void ComboBoxItem_Selected_10(object sender, RoutedEventArgs e)
        {
            TitleText.Foreground = new SolidColorBrush(Colors.DarkGoldenrod);
        }

        private void ComboBoxItem_Selected_11(object sender, RoutedEventArgs e)
        {
            TitleText.Foreground = new SolidColorBrush(Colors.Red);
        }

        // Dropdown Colors change ends here!
    }
}
