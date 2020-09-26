# -*- coding: utf-8 -*-                                                                                                 #Version: 1.0.1
#Created by Jose C. García Gamero
#Twitter: @jcgarciagamero

import os
import sys
nombreArchivo = sys.argv[1]

f = open(nombreArchivo,'w')
mensaje = """
<head>
    <title>Report</title>
    <style media="screen">
        body {
            font-family: 'Segoe UI','Microsoft Sans Serif',sans-serif;
        }

        /*
            These next two styles are apparently the modern way to clear a float. This allows the logo
            and the word "Invoice" to remain above the From and To sections. Inserting an empty div
            between them with clear:both also works but is bad style.
            Reference:
            http://stackoverflow.com/questions/490184/what-is-the-best-way-to-clear-the-css-style-float
        */
        header:before, header:after {
            content: " ";
            display: table;
        }

        header:after {
            clear: both;
        }

        .invoiceNbr {
            font-size: 40px;
            margin-right: 30px;
            margin-top: 30px;
            float: right;
        }

        .logo {
            float: left;
        }

        .from {
            float: left;
        }

        .to {
            float: right;
        }

        .fromto {
            border-style: solid;
            border-width: 1px;
            border-color: #e8e5e5;
            border-radius: 5px;
            margin: 20px;
            min-width: 200px;
        }

        .fromtocontent {
            margin: 10px;
            margin-right: 15px;
        }

        .panel {
            background-color: #e8e5e5;
            padding: 7px;
        }

        .items {
            clear: both;
            display: table;
            padding: 20px;
        }

        /* Factor out common styles for all of the "col-" classes.*/
        div[class^="col-"] {
            display: table-cell;
            padding: 7px;
        }

        /*for clarity name column styles by the percentage of width */
        .col-1-10 {
            width: 10%;
        }

        .col-1-52 {
            width: 52%;
        }

        .row {
            display: table-row;
            page-break-inside: avoid;
        }

    </style>

    <!-- These styles are exactly like the screen styles except they use points (pt) as units
        of measure instead of pixels (px) -->
    <style media="print">
        body {
            font-family: 'Segoe UI','Microsoft Sans Serif',sans-serif;
        }

        header:before, header:after {
            content: " ";
            display: table;
        }

        header:after {
            clear: both;
        }

        .invoiceNbr {
            font-size: 30pt;
            margin-right: 30pt;
            margin-top: 30pt;
            float: right;
        }

        .logo {
            float: left;
        }

        .from {
            float: left;
        }

        .to {
            float: right;
        }

        .fromto {
            border-style: solid;
            border-width: 1pt;
            border-color: #e8e5e5;
            border-radius: 5pt;
            margin: 20pt;
            min-width: 200pt;
        }

        .fromtocontent {
            margin: 10pt;
            margin-right: 15pt;
        }

        .panel {
            background-color: #e8e5e5;
            padding: 7pt;
        }

        .items {
            clear: both;
            display: table;
            padding: 20pt;
        }

        div[class^="col-"] {
            display: table-cell;
            padding: 7pt;
        }

        .col-1-10 {
            width: 10%;
        }

        .col-1-52 {
            width: 52%;
        }

        .row {
            display: table-row;
            page-break-inside: avoid;
        }
    </style>

</head>
<body>
    <header>
        <div class="logo">
            <img src="https://notmining.es/assets/img/logo.png" alt="generic business logo" height="90" />
        </div>
        
    </header>

 
</body>
</html>"""

f.write(mensaje)
f.close()