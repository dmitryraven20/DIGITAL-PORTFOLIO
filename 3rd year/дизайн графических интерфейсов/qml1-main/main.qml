import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.3

Window {
    id: win
    width: 480; height: 640; visible: true
    title: qsTr("qt1")

    RowLayout {
        anchors.fill:parent
        spacing:10
    }

    Elem{
        Layout.alignment: Qt.AlignCenter
    }
}
