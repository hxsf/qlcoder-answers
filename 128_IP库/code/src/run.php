<?php
include("TaobaoIP.php");
$TIP = new TaobaoIP();
$TIP->init();
// $data=$TIP->ip2addr("0.0.0.0");
$cnt = [
    '上海市' => 0,
    '北京市' => 0,
    '杭州市' => 0,
    '深圳市' => 0
];
for ($i=0; $i < 256; $i++) {
    for ($j=0; $j < 256; $j++) {
        for ($k=0; $k < 256; $k++) {
            for ($l=0; $l < 256; $l++) {
                $data=$TIP->ip2addr("$i.$j.$k.$l");
                if ($data['province'] == '上海市') $cnt['上海市']++; // 7
                if ($data['province'] == '北京市') $cnt['北京市']++; // 26
                if ($data['city'] == '杭州市') $cnt['杭州市']++; // 242
                if ($data['city'] == '深圳市') $cnt['深圳市']++; // 75
                echo "$i.$j.$k.$l\n";
                // break;
            }
            // break;
        }
        // break;
    }
    // break;
}
$TIP->close();
var_dump($cnt);
?>
