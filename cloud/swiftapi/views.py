# -*- coding: utf-8 -*-
import  os
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from swiftclient import client

# Create your views here.
conname = "Ben"
def index():
	_authurl = os.environ['OS_AUTH_URL']
	_auth_version = '3'
	_user = "admin"
	_key = "0901"
	_os_options = {
		'user_domain_name': os.environ['OS_USER_DOMAIN_NAME'],
		'project_domain_name': os.environ['OS_PROJECT_DOMAIN_NAME'],
		'project_name': os.environ['OS_PROJECT_NAME']
	}
	conn = client.Connection(
		authurl=_authurl,
		user=_user,
		key=_key,
		os_options=_os_options,
		auth_version=_auth_version
	)
	return conn
conn=index()
def loin(req):
	return render(req,'login.html')
def login(req):
	return HttpResponseRedirect("/swift/1")
# def swift(request):
# 	# _authurl = 'http://127.0.0.1:5000/v3'
# 	# _auth_version = '3'
# 	# _user = 'admin'
# 	# _key = '0901'
# 	# _os_options = {
# 	# 	'user_domain_id': domain_id,
# 	# 	'project_domain_id': domain_id,
# 	# 	'project_id': '8adadc87a48c444da51601a1b47e5b3c'
# 	# }
# 	# conn = client.Connection(
# 	# 	authurl=_authurl,
# 	# 	user=_user,
# 	# 	key=_key,
# 	# 	os_options=_os_options,
# 	# 	auth_version=_auth_version
# 	# )
# 	return render_to_response('swift.html',locals())
def swift(request):
	accinfo,accounts = conn.get_account()
	ken,container = conn.get_container(conname)
	# objects = conn.get_object(conname,"zzh")
	return render_to_response('swift.html',locals())
def get_container(req):
	if req.method=="POST":id=req.POST
	container = conn.get_container(id['name'])[1]
	return render_to_response('swift.html',locals())
def put_container(req):
	if req.method=="POST":id=req.POST
	conn.put_container(id['name'])
	return render_to_response('swift.html',locals())
def delete_container(req):
	if req.method=="POST":id=req.POST
	conn.delete_container(id['id'])
	return render_to_response('swift.html',locals())
def delete_object(req):
	if req.method=="POST":id=req.POST
	conn.delete_object(conname,id['id'])
	return render_to_response('swift.html',locals())
def put_object(req):
	# 创建文件夹
	content_type = 'application/directory'
	obj = None
	if req.method=="POST":id=req.POST
	conn.put_object(conname,id['name'],obj, content_type=content_type)
	return render_to_response('swift.html',locals())
def get_object(req):
	# 下载文件
	if req.method=="POST":id=req.POST
	n,m=conn.get_object(conname,id['id'])
	with open('/home/'+id['id'], 'w') as local:
		local.write(m)
	return render_to_response('swift.html',locals())
def put_objectfile(req):
	# 上传文件
	content_type = 'text/plain'
	if req.method == "POST": id = req.FILES.get("img",None)
	destination = open(os.path.join("/home", id.name), 'wb+')
	for chunk in id.chunks():
		destination.write(chunk)
	destination.close()
	with open("/home/"+id.name, 'r') as local:
		conn.put_object(
			conname,
			id.name,
			contents=local,
			content_type='text/plain'
		)
	return HttpResponseRedirect("/swift/1")
# # def delete_container(req):
# # 	if req.method=="POST":id=req.POST
# # 	conn.delete_container(id['id'])
# # 	return render(req, 'filecontent.html')