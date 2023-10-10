<?php
$username = 'hxsf';
function one($value) {
	for ($i=1000000; $i < 10000000000; $i++) {
		$md = md5(date_format(date_create(), "Ymd").$username.$value.$i);
		if (strncasecmp('000000', $md, 6) == 0) {
			return $i;
		}
	}
	return -1;
}

for ($i=0; $i < 1002; $i++) {
	$token = one($i);
	echo "\"$i\": ", $token, ",\n";
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "http://www.qlcoder.com/train/handsomerank?user=hxsf&checkcode=$token");
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_HEADER, 0);
	$output = curl_exec($ch);
	if (strncasecmp($output, '验证码错误', 6) == 0) {
		echo 'error';
		exit(0);
	}
	curl_close($ch);
}
