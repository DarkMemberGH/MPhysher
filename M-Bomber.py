import requests

url="https://id.vk.com/auth?v=1.46.0&app_id=7913379&uuid=bed0f5b798&redirect_uri=https%3A%2F%2Fvk.com%2Fjoin&app_settings=W10%3D&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInBhcmFtcyI6eyJ0eXBlIjoic2lnbl91cCJ9fQ%3D%3D&scheme=bright_light"

para={
	'login':'+94764087299'
}

respose=requests.get(url,para)
print(response.content)