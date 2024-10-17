run:
	export http_proxy=http://127.0.0.1:1087;export https_proxy=http://127.0.0.1:1087;
	python test.py

curl:
	curl -L \
	-H 'Host: pda.weather.gov.hk' \
	-H 'accept: application/json, text/javascript, */*; q=0.01' \
	-H 'sec-fetch-site: same-origin' \
	-H 'referer: https://pda.weather.gov.hk/locspc/data/ocf_data/graph/arwf/index.html?stationCode=HKO&currentHour=202410161013&device=iOS&theme=light&lang=sc' \
	-H 'sec-fetch-dest: empty' \
	-H 'x-requested-with: XMLHttpRequest' \
	-H 'sec-fetch-mode: cors' \
	-H 'accept-language: zh-CN,zh-Hans;q=0.9' \
	-H 'user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148' \
	--compressed \
	'https://pda.weather.gov.hk/locspc/data/ocf_data/HKO.v2.xml' \
	> rsp_body.json
