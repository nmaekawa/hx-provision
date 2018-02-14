import multiprocessing

workers = multiprocessing.cpu_count() + 1

#bind = 'unix:/var/run/loris/gunicorn-loris.sock'
bind = '127.0.0.1:9000'

errorlog = '/var/log/loris/gunicorn-loris-error.log'

accesslog = '/var/log/loris/gunicorn-loris-access.log'

proc_name = 'gunicorn_loris'

capture_output = True

pidfile = '/var/run/loris/gunicorn-loris.pid'

secure_scheme_headers = {
    'X-FORWARDED-PROTOCOL': 'https',
    'X-FORWARDED-PROTO': 'https',
    'X-FORWARDED-SSL': 'on'
}

timeout = 60
