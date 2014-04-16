<html>
<body>
<?php

	//get and check connection
	$db = new mysqli("localhost", "snadmin", "snadmin*", "sensornetworks");
	if($db->connect_error){
		die("error");
	}
	
	
	$query_string = "select *from sp14_jyu_4920_userlog join sp14_jyu_4920_authkeys on sp14_jyu_4920_userlog.addr = sp14_jyu_4920_authkeys.addr ";
	$res = $db->query($query_string);
	
	echo "<table border = '1'>
	<tr>
	<th> Date and Time</th>
	<th> Address</th>
	<th> User </th>
	</tr>";
	
	while ($row = $res->fetch_assoc()){

		echo "<tr>";
		echo "<td>" . $row['dateandtime'] . "</td>";
		echo "<td>" . $row['addr'] . "</td>";
		echo "<td>" . $row['user'] . "</td>";
		echo "</tr>";

	}
	echo "</table>";


	


	
	

	
	


?>
</body>
</html>