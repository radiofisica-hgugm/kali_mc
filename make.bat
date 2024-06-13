echo on
pyinstaller --noconsole --name kali_mc --noconfirm --icon .\ui\res\science-atom-icon.png main.py --paths ./ --splash .\ui\res\science-atom-icon.png --add-data "data/*.*;data/"
