<?php
if(isset($_POST['search'])) {
        $valuetosearch = $_POST['valuetosearch'];
        $query = "SELECT * from test WHERE CONCAT(STOVEPIPE,DATACENTER,VSN,FQDN,IP,PORT,POLICY,DEVICE) LIKE '%".$valuetosearch."%'";
        $search_result = filtertable($query);
	echo "Connection established";
} else {
        $query = "SELECT * from search";
        /*$search_result = filtertable($query);*/
        echo "Enter to search based on the below table:<br><br>";
}
function filtertable($query) {
        $connect = mysqli_connect("localhost","root","Tulsi@991","searchdb");
        $filter_result = mysqli_query($connect,$query);
        return $filter_result;
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>F5 Search</title>
<style type = "text/css">
        .menu a {
                text-decoration:none;
                color: white;
        }
        .row_yel {
                color: #f9ff33;
        }
        .row_blue {
                color: #33ffe3;
        }
        .row_green {
                color: #33ff68;
        }
        body    {
                font-family: "Eras Bold ITC";
        }
        th {
                background-color: #588c7e;
                color: white;
        }
        #top,
        #bottom {
                position: fixed;
                left: 0;
                right: 0;
                height: 50%;
        }
        #top    {
                top: 0;
                background-color: #000f2b;
        }
        #bottom {
                bottom: 0;
                background-color: white;
                font: "Eras Bold ITC";
                overflow: auto;
		text-align: center;
	}
	th {
		background-color: #588c7e;
		color: white;
	}
	input[type=text] {
		width: 20%;
		height: 10%;
		padding: 10px 10px;
		margin: 4px 0;
		border-radius: 10px;
		background: white;
	}
	html {
		height: 100%;
		width: 95%;
		background-color: #000f2b;
		margin: 0;
		padding: 0;
		text-align: justify;
		color: white;
	}
	h1 { font-size: 30px; }
	a {color: white; text-decoration: none; }
	a:hover { color: #335; text-decoration: none; }
	tr,th,td {
		border: 1px solid black;
	}
	table {
		font-family: Eras Bold ITC;
		text-align: center;
	}
</style>
</head>
<div id = "top">
        <body style = "background-color:#000f2b;">
        <div id="heading" style="text-align:center; font-fammily: Eras Bold ITC; font-size:medium;">
                <h1 font="Eras Bold ITC"> F5 Search </h1>
                <p font="Eras Bold ITC"> Enter the word to search for example: UTC or fannie or 10.136 etc. </p>
                <form action="" method="POST" enctype="multipart/form-data">
                        <input type="text" name="valuetosearch" placeholder="Search">
                        <input type="submit" name="search" value="Search"><br><br>
                </form>
        </div>
</div>
<div id = "bottom" style="text-align:center; font-fammily: Eras Bold ITC; font-size:medium;">
        <table align="center">
                <?php if (isset($query)) : ?>
                        <tr>
                                <th align="center"> STOVEPIPE </th>
				<th align="center"> DATACENTER </th>
                                <th aligh="center"> VIRTUALSERVERNAME </th>
                                <th align="center"> FQDN </th>
                                <th align="center"> IPADDRESS </th>
				<th align="center"> PORT </th>
				<th aligh="center"> POLICY </th>
                                <th align="center"> DEVICENAME </th>
                        </tr>
                        <?php while($row = mysqli_fetch_array($search_result)): ?>
				<tr>
					<td style="font-weight:bold; color:#ff7433"> <?php echo $row['STOVEPIPE']?> </td>
					<td style="font-weight:bold; color:#ff7433"> <?php echo $row['DATACENTER']?> </td>
					<td style="font-weight:bold; color:#ff7433"> <?php echo $row['VSN']?> </td>
					<td style="font-weight:bold; color:#ff7433"> <?php echo $row['FQDN']?> </td>
					<td style="font-weight:bold; color:#ff7433"> <?php echo $row['IP']?> </td>
					<td style="font-weight:bold; color:#ff7433"> <?php echo $row['PORT']?> </td>
					<td style="font-weight:bold; color:#ff7433"> <?php echo $row['POLICY']?> </td>
					<td style="font-weight:bold; color:#ff7433"> <?php echo $row['DEVICE']?> </td>
				</tr>
                        <?php endwhile; ?>
                <?php endif; ?>
        </table>
</div>
</body>
</html>
