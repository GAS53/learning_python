import re


li_result = []
with open('nginx_logs.txt', 'r') as file:
    for line in file:
        # print(line)
        ip4 = re.search(r'^\d+.\d+.\d+.\d+', line)
        ip6 = re.match(r'([0-9A-Za-z]{1,4}:){7}[0-9A-Za-z]{1,4}', line)
        ip = ip4 if ip4 else ip6
        if ip:
            date = re.search(r'\[.*\]', line).group()[1:-2]
            method = re.search(r'"[A-Z]{3}', line).group()[1:]
            load = re.search(r'/downloads/product_\d', line).group()
            req_res = re.findall(r' [0-9]{1,3}', line)
            request = req_res[0]
            responce = req_res[1]
            line_res = (ip.group(), date, method, load, request, responce)
            li_result.append(line_res)

print(li_result)  # ...('79.136.114.202', '04/Jun/2015:07:06:35 +0000',
                  # '"GET', '/downloads/product_1', ' 404', ' 334')]
