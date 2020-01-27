import hashlib

sessions = {'3.2': ['2-Logging', 
                    '3-Graphics'], 
            '9.1': ['2-The Current Weather', 
                    '3-Crypto Exchange', 
                    '4-Google directions', 
                    '5-Flying Aircraft']}

def problem_choice(email, seminar, problems):
    email = email.strip().lower()
    assert "@minerva.kgi.edu" in email
    seminar = seminar.strip().lower()
    enc = (email + seminar).encode()
    md5 = hashlib.md5(enc).hexdigest()
    ind = int(md5, 16) % len(problems)
    return problems[ind]

if __name__ == '__main__':
    email = input('Please enter your student email address: ')
    sessions_key = input('What session is this for (sessions supported: {}): '.format(', '.join([*sessions])))
    print(problem_choice(email, sessions_key, sessions[sessions_key]))
