<?php
$username = 'hxsf';
function one($value) {
	for ($i=0; $i < 10000000000; $i++) {
		$md = md5($value.'hxsf'.$i.'20170401');
		if (strncasecmp('000000000000000000000000000', $md, 27) == 0) {
			return $i;
		}
	}
	return -1;
}

echo one('7632');