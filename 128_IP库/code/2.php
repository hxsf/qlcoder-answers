<?php
$arr = [255, 255, 255, 255];
$loc = (1<<16)*intval($arr[0])+(1<<8)*(intval($arr[1]))+intval($arr[2]);
echo $loc;
