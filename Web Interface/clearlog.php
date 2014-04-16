<html>
<body>
<?php

	$address = $_POST['addr'];
	$user = $_POST['name'];

	$db = new mysqli("localhost", "snadmin", "snadmin*", "sensornetworks");

	if($db->connect_error){
		die("error");
	}
	

	
	$query_string1 = "delete from sp14_jyu_4920_authkeys";
	

	$db->query($query_string1);

	echo "successfully cleared log!"
	
	
	
	


?>
</body>
</html>