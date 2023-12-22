<?php

    $cols = 10;
    $rows = 10;

    for ($tr = 1; $tr <= $rows; $tr ++)
        {
        echo "<table  border='1' align='center'>";
        if($td==1){
            echo "<tr class='prim'>";
        }
        else{
            echo "<tr>";
        }
        
        for($td = 1;$td <=$cols; $td++)
        {
            if($td==1){
                echo "<td class='prim'>" .$tr * $td."</td>\n";
            }
            else if($tr==1){
                echo "<td class='prim'>" .$tr * $td."</td>\n";
            }
            else if($td==$tr){
                echo "<td class='sec'>" .$tr * $td."</td>\n";
            }
            else{
                echo "<td>" .$tr * $td."</td>\n";
            }
        }

echo "</tr>\n";
}   

?>