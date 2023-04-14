using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;
using System.Windows.Media;

namespace WpfAppOlympiaRenkaat
{
    public class MyCanvas : Canvas
    {
        double x;
        protected override void OnRender(DrawingContext dc)
        {
            //base.OnRender(dc);
            dc.DrawEllipse(null, new Pen(Brushes.Blue, 7), new System.Windows.Point(107, 107), 50, 50);
            dc.DrawEllipse(null, new Pen(Brushes.Yellow, 7), new System.Windows.Point(222, 157), 50, 50);
            dc.DrawEllipse(null, new Pen(Brushes.Black, 7), new System.Windows.Point(289, 107), 50, 50);
            dc.DrawEllipse(null, new Pen(Brushes.Green, 7), new System.Windows.Point(351, 157), 50, 50);
            dc.DrawEllipse(null, new Pen(Brushes.Red, 7), new System.Windows.Point(416, 107), 50, 50);
        }

        public void SetX(double x1)
        {
            this.x = x1;
            InvalidateVisual();
        }
    }
}
