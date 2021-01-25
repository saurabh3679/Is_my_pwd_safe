import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    # print(hashes)
    # creating a tuple comprehension
    all_hashes = (line.split(':') for line in hashes.splitlines())
    print(all_hashes)
    for h, count in all_hashes:
        print(h, count)
        if h == hash_to_check:
            return print(f'Your password has been hacked {count} number of times!')
    return print("You are lucky. Your password has never been hacked yet.")


def pwned_api_check(password):
    # Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print(sha1password)
    first5_char, tail = sha1password[:5], sha1password[5:]
    print(first5_char)
    print(tail)
    response = request_api_data(first5_char)
    print(response)
    # response text is a string type, not a list
    return get_password_leaks_count(response.text, tail)


def main(pwd):
    pwned_api_check(pwd)
    return print("We are done!")


if __name__ == '__main__':  # run this file only from command-line, not as an import
    sys.exit(main(sys.argv[1]))
