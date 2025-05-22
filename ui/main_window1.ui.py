<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>500</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Vehicle Sticker Generator</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLineEdit" name="plateNumberInput">
      <property name="placeholderText">
       <string>Enter Plate Number</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLineEdit" name="areaInput">
      <property name="placeholderText">
       <string>Enter Area</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QDateEdit" name="expiryDateInput">
      <property name="calendarPopup">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QComboBox" name="stickerTypeCombo">
      <item>
       <property name="text">
        <string>Standard</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Visitor</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Contractor</string>
       </property>
      </item>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="qrCodeLabel">
      <property name="minimumSize">
       <size>
        <width>150</width>
        <height>150</height>
       </size>
      </property>
      <property name="frameShape">
       <enum>QFrame::Box</enum>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
      <property name="text">
       <string>QR Code Preview</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="generateQRButton">
      <property name="text">
       <string>Generate QR</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="printStickerButton">
      <property name="text">
       <string>Print Sticker</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="saveRecordButton">
      <property name="text">
       <string>Save Record</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
