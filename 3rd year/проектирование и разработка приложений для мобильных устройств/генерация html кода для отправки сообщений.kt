import java.io.File

data class Message(val address: String?, val topic: String?, val content: String?, val timestamp: String?) {
    fun toHTML(): String {
        var template = "<!DOCTYPE html>\n" +
                "<html>\n" +
                "<head>\n" +
                "<link rel=\"stylesheet\" type=\"text/css\" href=\"css.css\">\n" +
                "</head>\n" +
                "<body>\n"
        template += "<table> "
        address?.let {
            template += ("<tr class=\"address\"><td>Адрес:</td><td>$it</td></tr> \n")
        }
        topic?.let {
            template += ("<tr><td class=\"topic\">Тема:</td><td>$it</td></tr> \n")
        }
        content?.let {
            template += ("<tr><td class=\"body\">Текст письма:</td><td>$it</td></tr> \n")
        }
        timestamp?.let {
            template += ("<tr><td class=\"date\">Дата отправки:</td><td>$it</td></tr> \n")
        }
        template +=  "</table>"
        template +=  "</body>\n" + "</html>\n"
        return template
    }
    fun toCSS(): String {
        var template_css = "table { font-size: 20px; border: 5px solid black; }\n" +
                "td {padding: 5px; \n border: 1px solid black;}\n"
        address?.let {
            template_css += ".address {font-style: italic;}\n"
        }
        topic?.let {
            template_css += ".topic {color: black;}\n"
        }
        content?.let {
            template_css += ".body {color: black; font-weight: bold;}\n"
        }
        timestamp?.let {
            template_css += ".date {color: darkgrey}\n"
        }
        return template_css
    }
}

fun main() {
    val m = Message(
        "ipetrushin@microsoft.com",
        "Важное письмо",
        "Здравствуйте, работа в процессе.",
        "Понедельник, 18 декабря, 2023 12:00:00"
    )
    val html = m.toHTML()
    println(html)
    val css = m.toCSS()
    val file = File("message.html")
    file.writeText(html)
    val file_css = File("css.css")
    file_css.writeText(css)
}