<?php

	function url_exists($url) {
		$headers = @get_headers($url); 

		if ($headers && strpos( $headers[0], '200')) { 
			return true;
		} else { 
			return false; 
		}
	}

	if (isset($_GET['q'])) {
		$q = $_GET['q'];
		$url_get = 'https://www.instagram.com/p/'.$q.'/';

		if (url_exists($url_get)) {
			$html = file_get_contents('https://www.instagram.com/p/'.$q.'/');
			$delimiter = '<script type="text/javascript"';
			$html = explode($delimiter, $html);
			$html = $delimiter.$html[4];

			echo $html;
		} else {
			echo "<span class='result'>Erro</span>";
			exit();
		}
	} else {
		echo "<span class='result'>Erro</span>";
		exit();	
	}

?>
<script type="text/javascript">
	if (typeof window._sharedData != "undefined") {
		obj = window._sharedData;
		url = obj.entry_data["PostPage"][0].graphql.shortcode_media.display_url;

		document.write('<span class="result">'+url+'</span>');

	}
</script>