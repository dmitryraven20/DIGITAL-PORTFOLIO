import java.util.*

enum class Direction {
    UP, DOWN, LEFT, RIGHT
}
class SmartRobot(x: Int, y: Int, direction: Direction, var name: String): Robot(x,y,direction) {
    fun moveRobot(toX: Int, toY: Int) {
        stepForward()
    }
}

open class Robot(var x: Int, var y: Int, var direction: Direction) {
    fun stepForward() {
        when (direction) {
            Direction.RIGHT -> x++
            Direction.LEFT -> x--
            Direction.UP -> y++
            Direction.DOWN -> y--
        }
    }

    fun turnRight() {
        direction = when (direction) {
            Direction.RIGHT -> Direction.DOWN
            Direction.LEFT -> Direction.UP
            Direction.UP -> Direction.RIGHT
            Direction.DOWN -> Direction.LEFT
        }
    }

    fun turnLeft() {
        direction = when (direction) {
            Direction.RIGHT -> Direction.UP
            Direction.LEFT -> Direction.DOWN
            Direction.UP -> Direction.LEFT
            Direction.DOWN -> Direction.RIGHT
        }
    }

    override fun toString(): String {
        return "(${x}, ${y}), looks ${direction}"
    }
}

fun moveRobot(robot: Robot, toX: Int, toY: Int) {
    val diffX = toX - robot.x
    val diffY = toY - robot.y

    if (robot.x != toX || robot.y != toY) {
        if (diffX > 0) {
            for (i in 1..diffX) {
                robot.stepForward()
                println(robot)
            }
        } else if (diffX < 0) {
            robot.turnLeft()
            for (i in 1..-diffX) {
                robot.stepForward()
                println(robot)
            }
        }

        if (diffY > 0) {
            robot.turnRight()
            for (i in 1..diffY) {
                robot.stepForward()
                println(robot)

            }
        } else if (diffY < 0) {
            robot.turnLeft()
            for (i in 1..-diffY) {
                robot.stepForward()
                println(robot)
            }
        }
    }
}

fun main() {
    val robot = SmartRobot(1,1, Direction.DOWN, "WALL-E")
    println(robot)
    moveRobot(robot,0,0)
}