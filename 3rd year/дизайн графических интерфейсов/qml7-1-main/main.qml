import QtQuick 2.15
import QtQuick.Controls
import QtQuick.Window 2.15

ApplicationWindow {
    width: 480
    height: 720
    visible: true
    title: qsTr("Hello World")

    background: Rectangle {
        gradient: Gradient {
            GradientStop { position: 0; color: "#ffffff" }
            GradientStop { position: 1; color: "#c1bbf9" }
        }
    }

    Column{
        spacing: 20
        anchors.centerIn: parent
    TextField {
        id: usernameField
        placeholderText: "Username"
        font.pixelSize: 24
        anchors.margins: 30
        color: focus ? "black" : "grey"
        focus:true
        width: 300
    }
    TextField {
        id: passwordField
        placeholderText: "Password"
        font.pixelSize: 24
        echoMode: TextInput.Password
        anchors.margins: 30
        color: focus ? "black" : "grey"
        width: 300
    }
    Row {
    Button {
        text: "Enter"
        anchors.margins: 30
        font.pixelSize: 24
        width: 150
        onClicked: console.log("Data has been entered")
    }
    Button {
        text: "Clear"
        anchors.margins: 30
        font.pixelSize: 24
        width: 150
        onClicked: {
            passwordField.text = ""
            usernameField.text = ""
        }
    }
    }
    }
}
