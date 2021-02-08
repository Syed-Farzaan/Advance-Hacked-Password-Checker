import requests
import hashlib
import sys

def request_api_data(hash_char):
  url = 'https://api.pwnedpasswords.com/range/' + hash_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the API.')
  return res
  # print(res)

# def read_res(response):
#   print(response.text)

def get_password_leaks_count(hashes, hash_to_check):                #* .splitlines() takes the entire result string and splits it into a 
  hashes = (line.split(':') for line in hashes.text.splitlines())   #* -list where each item in the list is a separate line (\n).
  for h, count in hashes:       #* line.split(':') will split the line (a string) into pieces by cutting it wherever it sees a ':' character.
    if h == hash_to_check:           
      return count
  return 0            
    # print(h, count)          
  # print(hashes)
     
     
def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)
  
  # print(response, first5_char, tail)
  # return read_res(response)
  # print(password.encode('utf-8'))
  # print(hashlib.sha1(password.encode('utf-8')))

# pwned_api_check('123')



# def main(args):
#   for password in args:
#     count = pwned_api_check(password)
#     if count:
#       print(f'{password} was found {count} times, you should change your password!')
#     else:
#       print(f'{password} was not found, Carry ON!')
#   return 'Done!'

# if __name__ == '__main__': 
#   sys.exit(main(sys.argv[1:]))

def main():
  with open('Your_Passwords.txt', 'r') as file:
    args = []
    for line in file:
      args.append(line)      # content = line.strip()
                             # args.append(content)

    for password in args:
      count = pwned_api_check(password)
      if count:
        print(f'{password} was found {count} times, you should change your password!')
      else:
        print(f'{password} was not found, Carry ON!')
    return 'Done!'

if __name__ == '__main__': 
  main()