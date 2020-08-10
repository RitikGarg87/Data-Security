from cx_Freeze import setup , Executable
setup(name = "encryption",
         version = "1.0",
         author="Ritik garg",
         description = "protect your data with the help of it",
         executables=[Executable(r"C:\Users\Harshit Garg\Desktop\Practice python\college project.py",
                                 icon=r"C:\Users\Harshit Garg\Desktop\Practice python\crypt.ico",
                                 shortcutName="crypt",
                                 shortcutDir="DesktopFolder")]
      )
