# from django.http import HttpResponse

from keystoneclient.v3 import client
import glanceclient
from novaclient import client as novaclient
from django.shortcuts import render_to_response
import json

# Create your views here.

DOMAIN_NAME = 'default'
USER = 'admin'
PASS = '0901'
PROJECT_DOMAIN_NAME = 'default'
PROJECT_NAME = 'admin'
KEYSTONE_URL = 'http://controller:35357/v3'
domainid = 'fe2e1f412ba74de78cda4ed88c0f2903'
id={}

keystone = client.Client(user_domain_name=DOMAIN_NAME,
						 username=USER,
						 password=PASS,
						 project_domain_name=PROJECT_DOMAIN_NAME,
						 project_name=PROJECT_NAME,
						 auth_url=KEYSTONE_URL)

OS_AUTH_TOKEN = keystone.auth_token

def index(request):
	DOMAIN_NAME = 'default'
	USER = 'admin'
	PASS = '0901'
	PROJECT_DOMAIN_NAME = 'default'
	PROJECT_NAME = 'admin'
	KEYSTONE_URL = 'http://controller:35357/v3'

	keystone = client.Client(user_domain_name=DOMAIN_NAME,
							 username=USER,
							 password=PASS,
							 project_domain_name=PROJECT_DOMAIN_NAME,
							 project_name=PROJECT_NAME,
							 auth_url=KEYSTONE_URL)

	project = keystone.projects.list()
	domain = keystone.domains.list()
	service = keystone.services.list()


	return render_to_response('index.html', locals())

def users(request):
	users = keystone.users.list()
	return render_to_response('key_users.html',locals())

def groups(request):
	groups = keystone.groups.list()
	return render_to_response('key_groups.html',locals())

def roles(request):
	roles = keystone.roles.list()
	return render_to_response('key_roles.html',locals())

def glance(request):

	keystone = client.Client(user_domain_name=DOMAIN_NAME,
							 username=USER,
							 password=PASS,
							 project_domain_name=PROJECT_DOMAIN_NAME,
							 project_name=PROJECT_NAME,
							 auth_url=KEYSTONE_URL)
	OS_AUTH_TOKEN = keystone.auth_token
	glance=glanceclient.client.Client('2',endpoint='http://localhost:9292/v2',token=OS_AUTH_TOKEN)
	list=glance.images.list()

	# glance_create=glance.images.create(name="zzh")

	return render_to_response('glance.html',locals())

def role_delete(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	keystone.roles.delete(gid)

	return render_to_response('key_roles.html')

def role_update(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	gname = id['name']
	keystone.roles.update(gid,gname)

	return render_to_response('key_roles.html')

def role_create(req):
	if req.method=="POST":
		id=req.POST
	gname = id['name']
	keystone.roles.create(name=gname, doamin_id=domainid)
	return render_to_response('key_roles.html')

def group_delete(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	keystone.groups.delete(gid)

	return render_to_response('key_roles.html')

def group_update(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	gname = id['name']
	keystone.groups.update(gid,gname)

	return render_to_response('key_roles.html')

def group_create(req):
	if req.method=="POST":
		id=req.POST
	gname = id['name']
	keystone.groups.create(gname,domainid)
	return render_to_response('key_roles.html')

def user_delete(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	keystone.users.delete(gid)

	return render_to_response('key_roles.html')

def user_update(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	gname = id['name']
	keystone.users.update(gid,gname)

	return render_to_response('key_roles.html')

def user_create(req):
	if req.method=="POST":
		id=req.POST
	gname = id['name']
	keystone.users.create(gname,domainid)
	return render_to_response('key_roles.html')

def project_delete(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	keystone.projects.delete(gid)

	return render_to_response('key_roles.html')

def project_update(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	gname = id['name']
	keystone.projects.update(gid,gname)

	return render_to_response('key_roles.html')

def project_create(req):
	if req.method=="POST":
		id=req.POST
	gname = id['name']
	keystone.projects.create(gname,domainid)
	return render_to_response('key_roles.html')

def glance_delete(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	glance = glanceclient.client.Client('2', endpoint='http://localhost:9292/v2', token=OS_AUTH_TOKEN)
	glance.images.delete(gid)

	return render_to_response('key_roles.html')

def glance_update(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	gname = id['name']
	glance = glanceclient.client.Client('2', endpoint='http://localhost:9292/v2', token=OS_AUTH_TOKEN)
	glance.images.update(gid,name = gname)

	return render_to_response('key_roles.html')

def glance_create(req):
	if req.method=="POST":
		id=req.POST
	gname = id['name']
	glance = glanceclient.client.Client('2', endpoint='http://localhost:9292/v2', token=OS_AUTH_TOKEN)
	glance.images.create(name=gname)
	return render_to_response('key_roles.html')