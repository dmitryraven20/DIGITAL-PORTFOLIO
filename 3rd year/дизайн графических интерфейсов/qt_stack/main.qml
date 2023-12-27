import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.2
Window {
    width: 360
    height: 640
    visible: true
    title: qsTr("StackView_test")

    property int defMargin:10

    StackView{
        id:stack_view
        anchors.fill: parent
        initialItem: page1
    }

    My_Page { id:page1
        backgroundColor: "red"
        buttonText: "To_Yellow"
        buttonText1: "To_Green"
        onButtonClicked: {
            stack_view.push(page3)
        }
        onButtonClicked1: {
            stack_view.push(page2)
        }
    }

    My_Page { id:page3
        visible: false
        backgroundColor: "yellow"
        buttonText: "To_Green"
        buttonText1: "To_Red"
        onButtonClicked: {
            stack_view.push(page2)
        }
        onButtonClicked1: {
            stack_view.pop(page1)
        }
    }

    My_Page { id:page2
        visible: false
        backgroundColor: "green"
        buttonText: "To_Red"
        buttonText1: "To_Yellow"
        onButtonClicked: {
            stack_view.pop(page1)
        }
        onButtonClicked1: {
            stack_view.pop(page3)
        }
    }
}
