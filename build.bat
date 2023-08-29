@call "D:\PyVenvList\KeyInfoReader\Scripts\activate.bat"
@python.exe -m nuitka --onefile --windows-icon-from-ico=icon.ico main.py -o mdk_make.exe
@call "D:\PyVenvList\KeyInfoReader\Scripts\deactivate.bat"
@cp mdk_make.exe C:\Tools\