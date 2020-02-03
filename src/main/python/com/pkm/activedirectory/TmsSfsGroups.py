#! /bin/env python
# 
# USAGE
# $ python ad_utils.py "My Group Name"
#
# Author: 
# Trinh Nguyen
# dangtrinhnt@gmail.com
# www.dangtrinh.com

import sys
import ldap


#AD_SERVERS = [ '<dc ip address>', 'dc ip address']
#AD_SERVERS = [ 'PW08TMSDC12.tmsnet.ri:389']
AD_SERVERS = [ 'PW08TMSDC12.tmsnet.ri']

#AD_USER_BASEDN = "<BASE DN. E.g. OU=Users,DC=Example,DC=Com>"
AD_USER_BASEDN = "OU=TMS,DC=tmsnet,DC=ri"

#AD_USER_FILTER = '(&(objectClass=USER)(sAMAccountName={username}))'
AD_USER_FILTER = '(&(objectClass=USER)(sAMAccountName={username}))'

#AD_USER_FILTER2 = '(&(objectClass=USER)(dn={userdn}))'
AD_USER_FILTER2 = '(&(objectClass=USER)(dn={userdn}))'

#AD_GROUP_FILTER = '(&(objectClass=GROUP)(cn={group_name}))'
AD_GROUP_FILTER = '(&(objectClass=GROUP)(cn={group_name}))'

#AD_BIND_USER = 'administrator@example.com'
AD_BIND_USER = 'pmartin@tmsnet.ri'

#AD_BIND_PWD = 'administratorpassword'
AD_BIND_PWD = 'Incred!bleHu1k_2008'


# ldap connection
def ad_auth(username=AD_BIND_USER, password=AD_BIND_PWD, address=AD_SERVERS[0]):
	#print(ldap.__file__)
    #print("Initializing LDAP[{0}, {1}, {2}]".format(username, password, address))
	conn = ldap.initialize('ldaps://' + address)
	conn.protocol_version = 3
	#conn.set_option(ldap.OPT_REFERRALS, 0)

	result = True
	print("Connection Established")

	try:
		conn.simple_bind_s(username, password)
		print("Succesfully authenticated")
	except ldap.INVALID_CREDENTIALS:
		return "Invalid credentials", False
	except ldap.SERVER_DOWN:
		return "Server down", False
	except ldap.LDAPError as e:
		if type(e.message) == dict and e.message.has_key('desc'):
			return "Other LDAP error: " + e.message['desc'], False
		else:
			return "Other LDAP error: " + e, False
	except:
		e = sys.exc_info()[0]
		print(e)

	return conn, result

def get_dn_by_username(username, ad_conn, basedn=AD_USER_BASEDN):
	return_dn = ''
	ad_filter = AD_USER_FILTER.replace('{username}', username)
	results = ad_conn.search_s(basedn, ldap.SCOPE_SUBTREE, ad_filter)
	if results:
		for dn, others in results:
			return_dn = dn
	return return_dn

#
# query only enabled users with the following filter
# (!(userAccountControl:1.2.840.113556.1.4.803:=2))
#
def get_email_by_dn(dn, ad_conn):
	email = ''
	result = ad_conn.search_s(dn, ldap.SCOPE_BASE, \
		'(&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))')
	if result:
		for dn, attrb in result:
			if 'mail' in attrb and attrb['mail']:
				email = attrb['mail'][0].lower()
				break
	return email


def get_group_members(group_name, ad_conn, basedn=AD_USER_BASEDN):
	members = []
	ad_filter = AD_GROUP_FILTER.replace('{group_name}', group_name)
	result = ad_conn.search_s(basedn, ldap.SCOPE_SUBTREE, ad_filter)
	if result:
		if len(result[0]) >= 2 and 'member' in result[0][1]:
			members_tmp = result[0][1]['member']
			for m in members_tmp:
				email = get_email_by_dn(m, ad_conn)
				if email:
					members.append(email)
	return members
	

if __name__ == "__main__":
  group_name = sys.argv[1]
  ad_conn, result = ad_auth()
  if result:
    group_members = get_group_members(group_name, ad_conn)
    for m in group_members:
      print (m)
  else:
      print ("Result object was false, ad_conn={0}".format(ad_conn))