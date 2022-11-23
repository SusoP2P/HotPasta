/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 6.3
import QtQuick.Controls 6.3
import Test

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor
    property alias launchonstartup: launchonstartup

    ToolBar {
        id: toolBar
        x: 0
        y: 0
        width: 1280
        height: 27

        Button {
            id: button2
            x: 0
            y: 0
            width: 88
            height: 27
            text: qsTr("Settings")
        }

        Button {
            id: button3
            x: 82
            y: 0
            width: 88
            height: 27
            text: qsTr("About")
        }
    }

    Switch {
        id: switch1
        x: 195
        y: 269
        width: 53
        height: 23
        text: ""
        icon.color: "#003e5b45"
        display: AbstractButton.TextBesideIcon
        layer.enabled: true
        smooth: true
        checkable: true
        checked: false
    }

    GroupBox {
        id: groupBox
        x: 49
        y: 243
        width: 212
        height: 136
        title: qsTr("Behaviour")
    }

    Text {
        id: text1
        x: 49
        y: 263
        width: 140
        height: 29
        text: qsTr("Behav1")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    Switch {
        id: switch2
        x: 195
        y: 304
        width: 53
        height: 23
        text: ""
        checked: false
        smooth: true
        icon.color: "#003e5b45"
        layer.enabled: true
        display: AbstractButton.TextBesideIcon
        checkable: true
    }

    Text {
        id: text2
        x: 49
        y: 298
        width: 140
        height: 29
        text: qsTr("Behav2")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    Switch {
        id: switch3
        x: 195
        y: 339
        width: 53
        height: 23
        text: ""
        checked: false
        smooth: true
        icon.color: "#003e5b45"
        layer.enabled: true
        display: AbstractButton.TextBesideIcon
        checkable: true
    }

    Text {
        id: text3
        x: 49
        y: 333
        width: 140
        height: 29
        text: qsTr("Behav3")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    Switch {
        id: launchonstartup
        x: 195
        y: 103
        width: 56
        height: 29
        scale: 0.85
        checked: false
        smooth: true
        icon.color: "#003e5b45"
        layer.enabled: true
        display: AbstractButton.TextBesideIcon
        checkable: true
    }

    GroupBox {
        id: groupBox1
        x: 49
        y: 83
        width: 212
        height: 136
        title: qsTr("Startup")
    }

    Text {
        id: text4
        x: 49
        y: 103
        width: 140
        height: 29
        text: qsTr("Launch on startup")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    Switch {
        id: switch5
        x: 195
        y: 144
        width: 53
        height: 23
        text: ""
        scale: 0.85
        checked: false
        icon.color: "#003e5b45"
        smooth: true
        layer.enabled: true
        display: AbstractButton.TextBesideIcon
        checkable: true
    }

    Text {
        id: text5
        x: 49
        y: 138
        width: 140
        height: 29
        text: qsTr("Launch minized")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    Switch {
        id: switch6
        x: 195
        y: 179
        width: 53
        height: 23
        text: ""
        scale: 0.85
        checked: false
        icon.color: "#003e5b45"
        smooth: true
        layer.enabled: true
        display: AbstractButton.TextBesideIcon
        checkable: true
    }

    Text {
        id: text6
        x: 49
        y: 173
        width: 140
        height: 29
        text: qsTr("Always show Onboarding")
        font.pixelSize: 12
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }
    
    GroupBox {
        id: groupBox2
        x: 49
        y: 448
        width: 212
        height: 136
        title: qsTr("Hotkeys")

        TextInput {
            id: textInput
            x: 114
            y: 32
            width: 86
            height: 20
            text: qsTr("CTRL + ALT + C")
            font.pixelSize: 12
        }

        TextInput {
            id: textInput1
            x: 114
            y: 67
            width: 86
            height: 20
            text: qsTr("CTRL + ALT + V")
            font.pixelSize: 12
        }

        TextInput {
            id: textInput2
            x: 114
            y: 103
            width: 86
            height: 21
            text: qsTr("CTRL + ALT + X")
            font.pixelSize: 12
            scale: 1
        }
    }

    Text {
        id: text7
        x: 49
        y: 473
        width: 115
        height: 29
        text: qsTr("Copy")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    Text {
        id: text8
        x: 49
        y: 508
        width: 115
        height: 29
        text: qsTr("Paste")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    Text {
        id: text9
        x: 49
        y: 543
        width: 115
        height: 29
        text: qsTr("Erase last copy")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    TextField {
        id: textField
        x: 428
        y: 486
        placeholderText: qsTr("Text Field")
    }
}
