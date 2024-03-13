def produce_default_dict():

    dict = {'root': 'password'}
    return dict


def salutation(nom, age):
    return f"Bonjour '{nom}', vous avez actuellement {age} ans."


def power_2(limit):
    result = ['0']  
    current_power = 0

    while 2 ** current_power <= limit:
        result.append(str(2 ** current_power))
        current_power += 1

    result_str = ','.join(result)
    print(result_str)


def check_ip_format(ip):
    parts = ip.split('.')
    if len(parts) == 4:
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return False
        return True
    return False


print(produce_default_dict())

print(salutation('nouhayla', '21'))




power_2(12)

print(check_ip_format('10.0.0.0'))
print(check_ip_format('192.12.'))
