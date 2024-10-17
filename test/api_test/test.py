import datetime
import http

import requests


def get_api() -> str:
    schema = "https"
    host = "pda.weather.gov.hk"
    path = "/locspc/data/ocf_data/HKO.v2.xml"
    api = f"{schema}://{host}{path}"
    return api


def do_req(api: str) -> requests.Response:
    rsp = requests.get(api)
    return rsp


def test_rsp_status_code(rsp: requests.Response) -> bool:
    rsp_code = rsp.status_code
    return rsp_code == http.HTTPStatus.OK


def extract_humidity(date: str, rsp: requests.Response):
    """
    Extract the relative humidity (e,g, 60 - 85%) for the date.
    """
    rsp_body = rsp.json()
    hourly_forecast = rsp_body.get("HourlyWeatherForecast")
    humidity_list = [
        item.get("ForecastRelativeHumidity")
        for item in hourly_forecast
        if item.get("ForecastHour")[:-2] == date
    ]
    return min(humidity_list), max(humidity_list)
    # humidity_list = []
    # for item in hourly_forecast:
    #     if item.get("ForecastHour")[:-2] == date:
    #         humidity = item.get("ForecastRelativeHumidity")
    #         humidity_list.append(humidity)


def test():
    api = get_api()
    rsp = do_req(api)
    if test_rsp_status_code(rsp):
        print("request is successful")
    else:
        print(f"request failed with status code {rsp.status_code}")
        return

    now = datetime.datetime.now()
    the_day_after_tomorrow = (now + datetime.timedelta(days=2)).strftime("%Y%m%d")
    humidity_min, humidity_max = extract_humidity(the_day_after_tomorrow, rsp)
    print(f"{the_day_after_tomorrow} humidity: {humidity_min}-{humidity_max}%")


if __name__ == "__main__":
    test()
