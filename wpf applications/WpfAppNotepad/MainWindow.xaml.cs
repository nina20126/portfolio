using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.IO;
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

namespace WpfAppNotepad
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private string _filename;
        private string _opened_file_path;

        public string Filename
        {
            get { return _filename; }
            set { }
        }

        public string Opened_file_path
        {
            get { return _opened_file_path; }
            set { }
        }

        public MainWindow()
        {

            System.Threading.Thread.CurrentThread.CurrentUICulture =
            new System.Globalization.CultureInfo("sv-SE");

            InitializeComponent();

            // Title = WpfAppNotepad.Properties.Resources.WPFNotepad;
            // Open = WpfAppNotepad.Properties.Resources.Open;
        }

        public MainWindow(string filename)
        {
            try
            {
                _filename = filename;
                this.Title = _filename;
            }

            catch(Exception ext)
            {
                MessageBox.Show("No File Name\n" + "Error code : " + ext.Message, "Missing File name", MessageBoxButton.OK, MessageBoxImage.Warning);
            }
        }

        // Function for open file
        private void MenuItem_Click(object sender, RoutedEventArgs e)
        {
            text_area.Document.Blocks.Clear();

            OpenFileDialog file_dialog = new OpenFileDialog();

            file_dialog.ShowDialog();

            text_area.AppendText(File.ReadAllText(file_dialog.FileName).ToString());

            _opened_file_path = System.IO.Path.GetFullPath(file_dialog.FileName);

            this.Title = System.IO.Path.GetFileNameWithoutExtension(file_dialog.FileName);
        }

        // function for printing
        private void MenuItem_Click_1(object sender, RoutedEventArgs e)
        {
            var printDialog = new PrintDialog();
            if (printDialog.ShowDialog() == true)
            {
                printDialog.PrintVisual(text_area as Visual, "printing as visual");
            }
        }

        // Fonttimääritysten avaaminen uuteen ikkunaan
        private void MenuItem_Click_2(object sender, RoutedEventArgs e)
        {
            Window1 mywindow = new Window1();

            mywindow.textBlock1.Text = GetContent(text_area); 
            if (mywindow.ShowDialog() == true)
            {
                FontSize = mywindow.textBlock1.FontSize;
            }
            //mywindow.ShowDialog(); 
        }
        private string GetContent(RichTextBox rtb)
        {
            TextRange textRange = new TextRange(
                rtb.Document.ContentStart,
                rtb.Document.ContentEnd
            );

            return textRange.Text;
        }


        // Function for saving files
        private void save_Click(object sender, RoutedEventArgs e)
        {
            SaveFileDialog dialog = new SaveFileDialog();

            dialog.FileName = "Untitled";
            dialog.DefaultExt = ".txt";
            dialog.Filter = "Text Documents (.txt) | *.txt";

            dialog.ShowDialog();

            TextRange range_of_text_area = new TextRange(text_area.Document.ContentStart, text_area.Document.ContentEnd);

            File.WriteAllText(dialog.FileName, range_of_text_area.Text.ToString());
;        }

        private void exit_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }
    }
}
