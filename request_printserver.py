import requests

login_headers = {
    'X-Authorization': 'PHAROS-USER <base64 encoded "netid:pass">', # PHAROS-USER base64encoded(netid:password)
    'Referer': 'https://aggieprint.tamu.edu/myprintcenter/',
    'Host': 'aggieprint.tamu.edu',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Accept': '*/*'
}

login_params = {
    'KeepMeLoggedIn': 'no',
    'includeprintjobs': 'no',
    'includedeviceactivity': 'yes',
    'includeprivileges': 'yes',
    'includecostcenters': 'yes',
    'excudeLocation': 'yes',
    'notRefreshBalance': 'no',
    '_request': 'b7180777-880e-4aa4-b7c9-87686d24c082',
    '_': '1537066069771'
}

login_url = 'https://aggieprint.tamu.edu/PharosAPI/logon?KeepMeLoggedIn=no&includeprintjobs=no&includedeviceactivity=yes&includeprivileges=yes&includecostcenters=yes&excudeLocation=yes&notRefreshBalance=no&_request=b7180777-880e-4aa4-b7c9-87686d24c082&_=1537066069771'

upload_params = {
    '_request': '1f464115-133b-4f0c-86df-f16eb8cc11cc'
}

upload_headers = {
    'Referer': 'https://aggieprint.tamu.edu/myprintcenter/',
    'Host': 'aggieprint.tamu.edu',
    'Accept': '*/*',
    'Cookie': ''
    # 'Content-Type': 'multipart/form-data; boundary=--------abcdefghijklmnopqr,stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ143791859014642624391843701300'
}

upload_url = 'https://aggieprint.tamu.edu/PharosAPI/users/asxktmuIqDH9LBCNzvm_cw2/printjobs?_request=1f464115-133b-4f0c-86df-f16eb8cc11cc'

cookie_names = ['PharosAPI.SignIn.Token', 'PharosAPI.X-PHAROS-USER-TOKEN', 'PharosAPI.X-PHAROS-USER-URI']

res = requests.get(login_url, params=login_params, headers=login_headers)

# print(res.text)

complete_cookie_string = ''

for cookie_name in cookie_names:
    if cookie_name in res.cookies:
        # print('COOKIE:',cookie_name, ': ', res.cookies[cookie_name])
        complete_cookie_string += '{}={}; '.format(cookie_name,res.cookies[cookie_name])

for i in range(len(cookie_names)):
    if cookie_names[i] in res.cookies:
        # print('COOKIE:',cookie_names[i], ': ', res.cookies[cookie_names[i]])
        if i != len(cookie_names)-1:
            complete_cookie_string += '{}={}; '.format(cookie_names[i],res.cookies[cookie_names[i]])
        else:
            complete_cookie_string += '{}={}'.format(cookie_names[i],res.cookies[cookie_names[i]])

upload_headers['Cookie'] = complete_cookie_string

upload_meta = '{"FinishingOptions":{"Mono":true,"Duplex":false,"PagesPerSide":"1","Copies":"1","DefaultPageSize":"Letter","PageRange":""},"PrinterName":""}'

file = open('test.txt','r')
upload_file = {'MetaData': upload_meta, 'content': ('test.txt', file, 'text/plain')} # Add dynamic content-type and filename
print(upload_file['content'])

up_res = requests.post(upload_url, headers=upload_headers, files=upload_file)

print(up_res.text)
# print(up_res.status)
