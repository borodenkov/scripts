1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
from fabric.api import *



def production():
	env.user = 'root'
	env.git_user = 'trnguyen'
	env.project_path = '/home/projects'
	env.venv_path = '/home/.venv'
	env.project_name = 'MyProject'
	env.logs_path = '/home/projects/logs/'
	env.hosts = ['myhost.com']
	env.repo = 'myrepo.com'


def setup():
	create_all_needed_directories()
	create_virtualenv()
	clone_repo()
	checkout_latest()
	install_requirements()


def create_all_needed_directories():
	run('mkdir -p %(project_path)s;\
			mkdir -p %(venv_path)s;\
			mkdir -p %(logs_path)s' % env)


def create_virtualenv():
	run('cd %(venv_path)s; virtualenv %(project_name)s' % env)


def deploy():
	checkout_latest()
	install_requirements()
	migrate()
	create_app_super_user()
	copy_config_files()
	restart_server()


def clone_repo():
	run('cd %(project_path)s; git clone %(git_user)s@%(repo)s:/srv/repos/git/%(project_name)s' % env)


def checkout_latest():
	run('cd %(project_path)s/%(project_name)s; git pull origin master' % env)


def install_requirements():
	run('source %(venv_path)s/%(project_name)s/bin/activate;\
		cd %(project_path)s/%(project_name)s; pip install -r requirements.txt' % env)


def migrate():
	run('source %(venv_path)s/%(project_name)s/bin/activate; \
			cd %(project_path)s/%(project_name)s;\
			python manage.py syncdb --noinput --migrate' % env)


def create_app_super_user():
	run('source %(venv_path)s/%(project_name)s/bin/activate; \
			cd %(project_path)s/%(project_name)s/src/CAS;\
			python manage.py createsuperuser' % env)

def copy_nginx_config():
	run('cp %(project_path)s/%(project_name)s/configs/nginx/default /etc/nginx/sites-available/' % env)


def copy_supervisor_config():
	run('cp %(project_path)s/%(project_name)s/configs/supervisor/guni.conf /etc/supervisor/conf.d/' % env)


def copy_config_files():
	copy_nginx_config()
	copy_supervisor_config()


def restart_server():
	run('service nginx restart')
	run('supervisorctl restart gunicorn')
