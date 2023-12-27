import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.2

Page{
    id:root
    property alias backgroundColor:back_fon.color
    property alias buttonText:batton_nav.text
    property alias buttonText1:batton_nav1.text

    signal buttonClicked();
    signal buttonClicked1();
    background: Rectangle{
        id:back_fon
    }
    Button {
        id:batton_nav
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.margins: defMargin // look into main.qml
        onClicked: {
            root.buttonClicked()
        }
    }
    Button {
        id:batton_nav1
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.margins: defMargin // look into main.qml
        onClicked: {
            root.buttonClicked1()
        }
    }

    header:ToolBar{
        id:page_header
        height:40
        RowLayout{
            ToolButton{
                id:back_btn
                Text{
                    text: "<-"
                    font.pixelSize: 24
                    visible:stack_view.depth>1
                    anchors.verticalCenter: parent.verticalCenter}
                onClicked: {
                    root.buttonClicked1()
                }
            }
            Text{
                id:header_page_text
            }
        }
    }
}
