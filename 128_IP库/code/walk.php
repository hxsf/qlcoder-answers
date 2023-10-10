<?php
// include("src/province.php");
// include("src/city.php");
// print($city[242]);
// print($city[29]);
// print($city[133]);
// print($city[75]);
//
// die;
$fd = fopen("./ip.data","r");
$cnt = ['杭州市' => 0, '北京市' => 0, '上海市' => 0, '深圳市' => 0];
while (!feof($fd)) {
    if (ftell($fd) > 16777215*5) break;
    $country_id=ord(fread($fd,1));
    $province_id=ord(fread($fd,1));
    $city_id1=ord(fread($fd,1));
    $city_id2=ord(fread($fd,1));
    $city_id=$city_id1*256+$city_id2;
    $proxy_id=ord(fread($fd,1));
    switch ($city_id) {
        case 133: $cnt['上海市']++; break;
        case 29: $cnt['北京市']++; break;
        case 242: $cnt['杭州市']++; break;
        case 75: $cnt['深圳市']++; break;
    }
}
printf("%d,%d,%d,%d", $cnt['杭州市'], $cnt['北京市'], $cnt['上海市'], $cnt['深圳市']);
fclose($fd);
