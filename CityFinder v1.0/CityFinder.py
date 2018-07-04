import sys
import urllib.parse, urllib.request, urllib.error
import json
from PyQt4 import QtGui, QtCore
import webbrowser

app = QtGui.QApplication(sys.argv)

url = 'https://maps.googleapis.com/maps/api/geocode/json?'
url2 = 'https://www.google.com.pk/?gws_rd=cr&ei=0B5ZWaD8E8HTvgTK96XoBg#q='
api_key = '&key=AIzaSyBjw3nZzQ5KCrdFr5rP5AMf3jPZ0Yvneqk'


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(700, 400, 525, 300)
        self.setWindowTitle('City Finder')
        self.setWindowIcon(QtGui.QIcon('Map.ico'))

        self.labbel21 = QtGui.QLabel(self)
        self.labbel21.resize(250, 30)
        self.labbel21.move(325, 55)

        self.labbel22 = QtGui.QLabel('By Noman Abid', self)
        self.labbel22.resize(250, 30)
        self.labbel22.move(450, 11)

        self.labbel23 = QtGui.QLabel('Place Name:', self)
        self.labbel23.resize(250, 30)
        self.labbel23.move(260, 55)

        self.labbel0 = QtGui.QLabel('City Name:', self)
        self.labbel0.resize(100, 20)
        self.labbel0.move(130, 8)

        self.labbel = QtGui.QLabel('Waiting for the Input....', self)
        self.labbel.resize(250, 40)
        self.labbel.move(50, 50)

        self.labbel1 = QtGui.QLabel('Status:', self)#1
        self.labbel1.resize(250, 20)
        self.labbel1.move(20, 100)

        self.labbel2 = QtGui.QLabel('Formatted Address:', self)#2
        self.labbel2.resize(250, 20)
        self.labbel2.move(20, 130)

        self.labbel3 = QtGui.QLabel('Place Name:', self)#3
        self.labbel3.resize(250, 20)
        self.labbel3.move(20, 160)

        self.labbel4 = QtGui.QLabel('District:', self)#4
        self.labbel4.resize(250, 20)
        self.labbel4.move(20, 190)

        self.labbel5 = QtGui.QLabel('Province/Capital:', self)#5
        self.labbel5.resize(250, 20)
        self.labbel5.move(20, 220)

        self.labbel6 = QtGui.QLabel(self)#6
        self.labbel6.resize(250, 20)
        self.labbel6.move(60, 100)

        self.labbel7 = QtGui.QLabel(self)#7
        self.labbel7.resize(130, 20)
        self.labbel7.move(120, 130)

        self.labbel8 = QtGui.QLabel(self)#8
        self.labbel8.resize(250, 20)
        self.labbel8.move(85, 160)

        self.labbel9 = QtGui.QLabel(self)#9
        self.labbel9.resize(250, 20)
        self.labbel9.move(62, 190)

        self.labbel10 = QtGui.QLabel(self)#10
        self.labbel10.resize(250, 20)
        self.labbel10.move(107, 220)

        self.labbel11 = QtGui.QLabel('Place ID:', self)#11
        self.labbel11.resize(250, 20)
        self.labbel11.move(260, 100)

        self.labbel12 = QtGui.QLabel('Latitude:', self)#12
        self.labbel12.resize(250, 20)
        self.labbel12.move(260, 130)

        self.labbel13 = QtGui.QLabel('Longitude:', self)#13
        self.labbel13.resize(250, 20)
        self.labbel13.move(260, 160)

        self.labbel14 = QtGui.QLabel('Country Name (Long):', self)#14
        self.labbel14.resize(250, 20)
        self.labbel14.move(260, 190)

        self.labbel15 = QtGui.QLabel('Country Name (Short):', self)#15
        self.labbel15.resize(250, 20)
        self.labbel15.move(260, 220)

        self.labbel16 = QtGui.QLabel(self)#16
        self.labbel16.resize(250, 20)
        self.labbel16.move(310, 100)

        self.labbel17 = QtGui.QLabel(self)#17
        self.labbel17.resize(250, 20)
        self.labbel17.move(310, 130)

        self.labbel18 = QtGui.QLabel(self)#18
        self.labbel18.resize(250, 20)
        self.labbel18.move(315, 160)

        self.labbel19 = QtGui.QLabel(self)#19
        self.labbel19.resize(250, 20)
        self.labbel19.move(373, 190)

        self.labbel20 = QtGui.QLabel(self)#20
        self.labbel20.resize(250, 20)
        self.labbel20.move(376, 220)

        Action1 = QtGui.QAction(QtGui.QIcon('filedown2.png'), 'Print Hi', self)
        Action1.triggered.connect(self.Print2)
        Action2 = QtGui.QAction(QtGui.QIcon('filedown.png'), 'Print Hi', self)
        Action2.triggered.connect(self.Print3)

        ToolBar = self.addToolBar('GUI')
        ToolBar.addAction(Action1)
        ToolBar.addAction(Action2)

        self.ProgressBar = QtGui.QProgressBar(self)
        self.ProgressBar.resize(410, 30)
        self.ProgressBar.move(5, 265)
        

        self.Textbox = QtGui.QLineEdit(self)
        self.Textbox.setPlaceholderText('Enter Any City Name Here')
        self.Textbox.resize(200, 25)
        self.Textbox.move(200, 5)
        self.btnn()

    def Print2(self):
        print('Hello from Folder Icon!')

    def Print3(self):
        print('Hello from File Icon!')

    def btnn(self):
        self.btn = QtGui.QPushButton('Access', self)
        self.btn.move(420, 265)
        self.btn.clicked.connect(self.ProgresBar)
        self.btnn2()

    def btnn2(self):
        self.btn2 = QtGui.QPushButton('JSON Script', self)
        self.btn2.move(420, 235)
        self.btn2.clicked.connect(self.Web)

        self.show()

    def ProgresBar(self):
        download = 0
        while download < 100:
            download += 0.001
            self.ProgressBar.setValue(download)
        self.labbel21.setText(self.Textbox.text())
        self.setGeometry(700, 400, 525, 300)
        self.Print()
        
    def Print(self):
        try:
            x = self.Textbox.text()
            self.b = url + urllib.parse.urlencode({'address': x}) + api_key
            print(self.b)
            c = urllib.request.urlopen(self.b)
            d = c.read().decode()
            e = json.loads(d)
            f = json.dumps(e, indent=4)
        except:
            pass
        try:
            self.frmtd_add = e['results'][0]['formatted_address']
        except:
            self.frmtd_add = 'n/a'
        try:
            self.lat = e['results'][0]['geometry']['location']['lat']
        except:
            self.lat = 'n/a'
        try:
            self.lng = e['results'][0]['geometry']['location']['lng']
        except:
            self.lng = 'n/a'
        try:
            self.placeid = e['results'][0]['place_id']
        except:
            self.placeid = 'n/a'
        try:
            self.longname = e['results'][0]['address_components'][0]['long_name']
        except:
            self.longname = 'n/a'
        try:
            self.district = e['results'][0]['address_components'][1]['long_name']
        except:
            self.district = 'n/a' 
        try:
            self.ProvinceCapital = e['results'][0]['address_components'][2]['long_name']
        except:
            self.ProvinceCapital = 'n/a'
        try:
            self.countrylong = e['results'][0]['address_components'][3]['long_name']
        except:
            self.countrylong = 'n/a'
        try:
            self.countryshort = e['results'][0]['address_components'][3]['short_name']
        except:
            self.countryshort = 'n/a'
        try:
            self.status = e['status']
        except:
            self.status = 'FAIL'
        self.saving()

    def saving(self):
        database = open('database.txt', 'a')
        lat = str(self.lat)
        lng = str(self.lng)
        database.write(self.longname + "'s Latitude: " + lat + "\n")
        database.write(self.longname + "'s Longitude: " + lng + "\n" + "\n")
        database.close()
        self.Lebbel()

    def Lebbel(self):
        self.labbel.setText('->  Data Retrieved from Google.')
        self.Lebbel1()

    def Lebbel1(self):
        self.labbel6.setText(self.status)
        self.Lebbel2()

    def Lebbel2(self):
        self.labbel7.setText(self.frmtd_add)
        self.Lebbel3()

    def Lebbel3(self):
        try:
            self.labbel8.setText(self.longname)
        except:
            pass
        self.Lebbel4()
        
    def Lebbel4(self):
        try:
            self.labbel9.setText(self.district)
        except:
            pass
        self.Lebbel5()
        
    def Lebbel5(self):
        try:
            self.labbel10.setText(self.ProvinceCapital)
        except:
            pass
        self.Lebbel6()
        
    def Lebbel6(self):
        try:
            self.labbel16.setText(self.placeid)
        except:
            pass
        self.Lebbel7()

    def Lebbel7(self):
        try:
            self.labbel17.setNum(self.lat)
        except:
            self.labbel17.setText('n/a')
            pass
        self.Lebbel8()

    def Lebbel8(self):
        try:
            self.labbel18.setNum(self.lng)
        except:
            self.labbel18.setText('n/a')
            pass
        self.Lebbel9()
        
    def Lebbel9(self):
        try:
            self.labbel19.setText(self.countrylong)
        except:
            pass
        self.Lebbel10()

    def Lebbel10(self):
        try:
            self.labbel20.setText(self.countryshort)
        except:
            pass

    def Web(self):
        url3 = url2 + self.placeid
        webbrowser.open_new(self.b)
        
#
GUI = Window()
sys.exit(app.exec_())
