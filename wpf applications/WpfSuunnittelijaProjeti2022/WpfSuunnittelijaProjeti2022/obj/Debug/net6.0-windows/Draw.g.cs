﻿#pragma checksum "..\..\..\Draw.xaml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "9ACAA0CFBCCE9C8EFE9374DFF6CA3BB7EEF59108"
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Controls.Ribbon;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Markup;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Effects;
using System.Windows.Media.Imaging;
using System.Windows.Media.Media3D;
using System.Windows.Media.TextFormatting;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Shell;
using WpfSuunnittelijaProjeti2022;


namespace WpfSuunnittelijaProjeti2022 {
    
    
    /// <summary>
    /// Draw
    /// </summary>
    public partial class Draw : System.Windows.Window, System.Windows.Markup.IComponentConnector {
        
        
        #line 10 "..\..\..\Draw.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.ToolBar MyToolbar;
        
        #line default
        #line hidden
        
        
        #line 11 "..\..\..\Draw.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.RadioButton LineButton;
        
        #line default
        #line hidden
        
        
        #line 12 "..\..\..\Draw.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.RadioButton EllipseButton;
        
        #line default
        #line hidden
        
        
        #line 13 "..\..\..\Draw.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.RadioButton RectangleButton;
        
        #line default
        #line hidden
        
        
        #line 15 "..\..\..\Draw.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Canvas MyCanvas;
        
        #line default
        #line hidden
        
        private bool _contentLoaded;
        
        /// <summary>
        /// InitializeComponent
        /// </summary>
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "7.0.0.0")]
        public void InitializeComponent() {
            if (_contentLoaded) {
                return;
            }
            _contentLoaded = true;
            System.Uri resourceLocater = new System.Uri("/WpfSuunnittelijaProjeti2022;component/draw.xaml", System.UriKind.Relative);
            
            #line 1 "..\..\..\Draw.xaml"
            System.Windows.Application.LoadComponent(this, resourceLocater);
            
            #line default
            #line hidden
        }
        
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "7.0.0.0")]
        [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Never)]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Design", "CA1033:InterfaceMethodsShouldBeCallableByChildTypes")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Maintainability", "CA1502:AvoidExcessiveComplexity")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1800:DoNotCastUnnecessarily")]
        void System.Windows.Markup.IComponentConnector.Connect(int connectionId, object target) {
            switch (connectionId)
            {
            case 1:
            this.MyToolbar = ((System.Windows.Controls.ToolBar)(target));
            return;
            case 2:
            this.LineButton = ((System.Windows.Controls.RadioButton)(target));
            
            #line 11 "..\..\..\Draw.xaml"
            this.LineButton.Click += new System.Windows.RoutedEventHandler(this.LineButton_Click);
            
            #line default
            #line hidden
            return;
            case 3:
            this.EllipseButton = ((System.Windows.Controls.RadioButton)(target));
            
            #line 12 "..\..\..\Draw.xaml"
            this.EllipseButton.Click += new System.Windows.RoutedEventHandler(this.EllipseButton_Click);
            
            #line default
            #line hidden
            return;
            case 4:
            this.RectangleButton = ((System.Windows.Controls.RadioButton)(target));
            
            #line 13 "..\..\..\Draw.xaml"
            this.RectangleButton.Click += new System.Windows.RoutedEventHandler(this.RectangleButton_Click);
            
            #line default
            #line hidden
            return;
            case 5:
            this.MyCanvas = ((System.Windows.Controls.Canvas)(target));
            
            #line 15 "..\..\..\Draw.xaml"
            this.MyCanvas.MouseDown += new System.Windows.Input.MouseButtonEventHandler(this.MyCanvas_MouseDown);
            
            #line default
            #line hidden
            
            #line 15 "..\..\..\Draw.xaml"
            this.MyCanvas.MouseUp += new System.Windows.Input.MouseButtonEventHandler(this.MyCanvas_MouseUp);
            
            #line default
            #line hidden
            
            #line 15 "..\..\..\Draw.xaml"
            this.MyCanvas.MouseMove += new System.Windows.Input.MouseEventHandler(this.MyCanvas_MouseMove);
            
            #line default
            #line hidden
            return;
            }
            this._contentLoaded = true;
        }
    }
}
