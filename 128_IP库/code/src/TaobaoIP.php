<?php
class TaobaoIP {
	public $fh = null;
	public function init () {
		$this->fh = fopen("../ip.data","r");
	}
	public function close () {
		fclose($this->fh);
	}
	public function ip2addr($ip)
	{
		include("country.php");
		include("province.php");
		include("city.php");
		include("proxy.php");
		$arr=explode(".",$ip);
		if(sizeof($arr)!=4)return false;
		foreach($arr as $a)
		{
			if($a>255||$a<0)return false;
		}
		$loc=(1<<16)*intval($arr[0])+(1<<8)*(intval($arr[1]))+intval($arr[2]);
		$loc*=5;
		// $this->fh=fopen("../ip.data","r");
		fseek($this->fh,$loc);
		$country_id=ord(fread($this->fh,1));
		$province_id=ord(fread($this->fh,1));
		$city_id1=ord(fread($this->fh,1));
		$city_id2=ord(fread($this->fh,1));
		$city_id=$city_id1*256+$city_id2;
		$proxy_id=ord(fread($this->fh,1));
        // fclose($this->fh);
		$addr=array();
		$addr['country']=$country[$country_id];
		$addr['province']=$province[$province_id];
		$addr['city']=$city[$city_id];
		$addr['proxy']=$proxy[$proxy_id];
		return $addr;
	}
}
