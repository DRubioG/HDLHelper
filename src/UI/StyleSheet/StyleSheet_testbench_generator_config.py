"""
Style sheet
"""

testbench_generator_config_gui = """
    /* Push Button */
    QPushButton{
        color:   #354547 ;
        font: 14px 'Helvetica';
        background-color: #ebeced;
        border-radius: 15px

    }
    QPushButton:hover{
        background-color:  #d4dbe6;
    }
    QPushButton#pushButton_cancel:hover{
        background-color:  #ec774f ;
    }
    QPushButton#pushButton_save:hover{
        background-color: #47e2f7 
    }

    /* QLineEdit */
    QLineEdit{
        color: blue;
        border-radius: 5px;
    }
    QLineEdit:focus{
        border: 2px solid  #a9d1f4
    }

    /* QComboBox */
 /*   QComboBox{
        border-radius: 5px;
        text-align: right;
    }
    QComboBox:focus{
        border: 2px solid  #a9d1f4;
    }
    
    QComboBox:!editable{
        color: black;
        border-radius: 5px;
        background-color: white;
        text-align: right;
    }
    QComboBox:editable{
        color: blue;
        background-color: #47e2f7 ;
        border-radius: 5px;
        background-color: white;
        text-align: right;
    }
    
    QComboBox:!editable:on{
        color: blue;
        border-radius: 5px;
        background-color: white;
        text-align: right;
    }*/
    /*QComboBox::down-arrow{
        image: url(icon.png)
    }*/
    

"""