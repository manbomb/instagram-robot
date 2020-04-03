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
		$url_get = 'https://www.instagram.com/explore/tags/'.$q.'/';

		if (url_exists($url_get)) {
			$html = file_get_contents($url_get);
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
<body></body>
<script type="text/javascript">
	if (typeof window._sharedData != "undefined") {
		obj = window._sharedData;
		urls = obj.entry_data["TagPage"][0].graphql.hashtag.edge_hashtag_to_media.edges;

		for (var i = urls.length - 1; i >= 0; i--) {
			url = urls[i].node.shortcode;
			document.body.innerText += url+"\n";
		}

	}
</script>