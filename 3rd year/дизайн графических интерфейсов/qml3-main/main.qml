import QtQuick 2.15
import QtQuick.Controls
import QtQuick.Window 2.15

ApplicationWindow {
    id: win
    width: 480
    height: 720
    visible: true
    title: qsTr("Interaction")

    background: Rectangle {
        gradient: Gradient {
            GradientStop { position: 0; color: "#ffffff" }
            GradientStop { position: 1; color: "#c1bbf9" }
        }
    }
    Rectangle {
        id:rect_top
        color: "lightgray"
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.margins: 10
        height:100

        Text {
            id:txt
            text:"Header"
            anchors.centerIn: parent
            font.pixelSize: 24
            wrapMode: Text.WordWrap
            font.family: "Century Gothic"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
    Rectangle {
        id:rect_mid
        color: "#eeffee"
        anchors.top: rect_top.bottom
        anchors.left: parent.left
        anchors.right:parent.right
        anchors.margins:10
        height:480

        Text {
            id:txt1
            text:"Main text"
            anchors.centerIn: parent
            font.pixelSize: 24
            wrapMode: Text.WordWrap
            font.family: "Century Gothic"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }

    Rectangle {
        id:rect_bot1
        color: "lightblue"
        anchors.bottom: parent.bottom
        border.width: 2;
        height:100
        width: win.width/3.5
        x:win.width/16
        y:win.width/16
        anchors.bottomMargin:10

        Text {
            id:txt3
            text:"Foot1"
            font.pixelSize: 24
            anchors.centerIn: parent
            wrapMode: Text.WordWrap
            font.family: "Century Gothic"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        MouseArea{
            id:mouse
            anchors.fill: parent
            hoverEnabled: true
            onClicked: console.log("CLICKED")
            onEntered: {
                rect_bot1.border.width+=5;
                txt2.color="lightgrey"
                txt4.color="lightgrey"
            }
            onExited: {
                rect_bot1.border.width-=5;
                txt2.color="black"
                txt4.color="black"
            }
        }
    }

    Rectangle {
        id:rect_bot2
        color: "lightblue"
        anchors.bottom: parent.bottom
        border.width: 2;
        height:100
        width: win.width/3.5
        x:win.width*6/16
        y:win.width/16
        anchors.bottomMargin:10

        Text {
            id:txt2
            text:"Foot2"
            font.pixelSize: 24
            anchors.centerIn: parent
            wrapMode: Text.WordWrap
            font.family: "Century Gothic"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        MouseArea{
            id:mouse2
            anchors.fill: parent
            hoverEnabled: true
            onClicked: console.log("CLICKED1")
            onEntered: {
                rect_bot2.border.width+=5;
                txt3.color="lightgrey"
                txt4.color="lightgrey"
                txt.text="Заглавие"
            }
            onExited: {
                rect_bot2.border.width-=5;
                txt3.color="black"
                txt4.color="black"
                txt.text="Header"
            }
        }
    }

    Rectangle {
        id:rect_bot3
        color: "lightblue"
        anchors.bottom: parent.bottom
        border.width: 2;
        height:100
        width: win.width/3.5
        x:win.width*11/16
        y:win.width/16
        anchors.bottomMargin:10

        Text {
            id:txt4
            text:"Foot3"
            font.pixelSize: 24
            anchors.centerIn: parent
            wrapMode: Text.WordWrap
            font.family: "Century Gothic"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        MouseArea{
            id:mouse3
            anchors.fill: parent
            hoverEnabled: true
            onClicked: console.log("CLICKED2")
            onEntered: {
                rect_bot3.border.width+=5;
                txt2.color="lightgrey"
                txt3.color="lightgrey"
                txt1.text="Все стабильно работает"
            }
            onExited: {
                rect_bot3.border.width-=5;
                txt2.color="black"
                txt3.color="black"
                txt1.text="Main text"
            }
        }
    }


}
