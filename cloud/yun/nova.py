# -*- coding: utf8 -*-
from django.shortcuts import render_to_response
from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client

USER = 'admin'
PASS = '0901'
PROJECT_NAME = 'admin'
KEYSTONE_URL = 'http://controller:5000/v3'
domain_id = 'fe2e1f412ba74de78cda4ed88c0f2903'

auth = v3.Password(auth_url=KEYSTONE_URL,
				   username = USER,
				   password = PASS,
				   project_name = PROJECT_NAME,
				   user_domain_id = domain_id,
				   project_domain_id = domain_id)
sess = session.Session(auth=auth)

def nova(request):
	# auth = v3.Password(auth_url=KEYSTONE_URL,
	# username = USER,
	# password = PASS,
	# project_name = PROJECT_NAME,
	# user_domain_id = domain_id,
	# project_domain_id = domain_id)
	# sess = session.Session(auth=auth)
	nova = client.Client("2.1", session=sess)
	nova_server =nova.servers.list()
	nova_falvors = nova.flavors.list()
	nova_volumes = nova.volumes.list()
	mn = []
	for n in nova_server:
		mn = n.__dict__
	mm=""
	for n in nova_falvors:
		mm = n.__dict__

	return render_to_response('nova.html',locals())

def nova_create(req):
	if req.method=="POST":
		id=req.POST
	gname = id['name']
	nova = client.Client("2.1", session=sess)
	flavor = nova.flavors.find(name="m1.tiny")
	image = nova.images.find(name="cirros")
	nics = [{'net-id': u'68809862-6654-4b2d-b525-133bf27e47e3', "v4-fixed-ip": ''}]
	nova.servers.create(name=gname,
						image=image,
						flavor=flavor,
						nics=nics,)

	return render_to_response('nova.html', locals())
def nova_delete(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	nova = client.Client("2.1", session=sess)
	nova.servers.delete(gid)

	return render_to_response('nova.html')

def nova_update(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	gname = id['name']
	nova = client.Client("2.1", session=sess)
	nova.servers.update(gid,name=gname)

	return render_to_response('nova.html')
def nova_stop(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	nova = client.Client("2.1", session=sess)
	nova.servers.stop(gid)

	return render_to_response('nova.html')
def nova_restart(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	nova = client.Client("2.1", session=sess)
	nova.servers.reboot(gid)

	return render_to_response('nova.html')
def nova_start(req):
	if req.method=="POST":
		id=req.POST
	gid = id['id']
	nova = client.Client("2.1", session=sess)
	nova.servers.start(gid)

	return render_to_response('nova.html')