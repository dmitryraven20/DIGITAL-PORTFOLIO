import QtQuick 2.15

Item{
    id: root
    anchors.fill: parent
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
        anchors.bottom: rect_bot.top
        anchors.margins:10

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
        id:rect_bot
        color: "lightgray"
        anchors.bottom: parent.bottom
        height:100
        width: win.width/3.5
        x:win.width/16
        y:win.width/16
        anchors.bottomMargin:10

        Text {
            id:txt2
            text:"1"
            font.pixelSize: 24
            anchors.centerIn: parent
            wrapMode: Text.WordWrap
            font.family: "Century Gothic"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
    Rectangle {
        id:rect_bot1
        color: "lightgray"
        anchors.bottom: parent.bottom
        height:100
        width: win.width/3.5
        x:win.width*6/16
        y:win.width/16
        anchors.bottomMargin:10

        Text {
            id:txt3
            text:"2"
            font.pixelSize: 24
            anchors.centerIn: parent
            wrapMode: Text.WordWrap
            font.family: "Century Gothic"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
    Rectangle {
        id:rect_bot2
        color: "lightgray"
        anchors.bottom: parent.bottom
        height:100
        width: win.width/3.5
        x:win.width*11/16
        y:win.width/16
        anchors.bottomMargin:10

        Text {
            id:txt4
            text:"3"
            anchors.centerIn: parent
            font.pixelSize: 24
            wrapMode: Text.WordWrap
            font.family: "Century Gothic"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
}
