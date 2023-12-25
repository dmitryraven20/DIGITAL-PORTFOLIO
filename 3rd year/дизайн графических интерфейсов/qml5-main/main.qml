import QtQuick 2.15
import QtQuick.Window 2.15

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")
    Rectangle {
        width: 200
        height: 480
        color: "lightgrey"
        x:25;y:0

        Rectangle{
            id:rect_red
            x:50;y:0
            width:100;height:100
            color:"red"
        }
        Rectangle{
            id:rect_yellow
            x:50;y:110
            width:100;height:100
            color:"yellow"
        }
        Rectangle{
            id:rect_green
            x:50;y:220
            width:100;height:100
            color:"green"
        }

        states:[
            State {
                name: "stop"
                PropertyChanges {target: rect_red; color:"red"}
                PropertyChanges {target:rect_yellow; color:"black"}
                PropertyChanges {target:rect_green; color:"black"}
            },
            State {
                name: "caution"
                PropertyChanges {target: rect_red; color:"black"}
                PropertyChanges {target:rect_yellow; color:"yellow"}
                PropertyChanges {target:rect_green; color:"black"}
            },
            State {
                name: "go"
                PropertyChanges {target: rect_red; color:"black"}
                PropertyChanges {target:rect_yellow; color:"black"}
                PropertyChanges {target:rect_green; color:"green"}
            } ]


        transitions:[
            Transition {
                from: "stop"
                to: "caution"},
            Transition {
                from: "caution"
                to: "go"},
            Transition {
                from: "go"
                to: "stop"}
        ]

        MouseArea{
            anchors.fill:parent
            onClicked: {
                if (parent.state === "stop") {
                    parent.state = "caution";
                } else if (parent.state === "caution") {
                    parent.state = "go";
                } else {
                    parent.state = "stop";
                }
            }
        }
    }


}
