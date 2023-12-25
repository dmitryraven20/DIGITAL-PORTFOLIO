import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5

Window {
    width: 400
    height: 400
    visible: true
    title: qsTr("swipe master")

        SwipeView {
            id: view

            currentIndex: 1
            anchors.fill: parent

            Item {
                id: firstPage
                Rectangle {
                    color: "red"
                    height: 400
                    width: 400
                }
            }
            Item {
                id: secondPage
                Rectangle {
                    color: "yellow"
                    height: 400
                    width: 400
                }
            }
            Item {
                id: thirdPage
                Rectangle {
                    color: "lime"
                    height: 400
                    width: 400
                }
            }
        }
        PageIndicator {
            id: indicator

            count: view.count
            currentIndex: view.currentIndex

            anchors.bottom: view.bottom
            anchors.horizontalCenter: parent.horizontalCenter
        }
}
