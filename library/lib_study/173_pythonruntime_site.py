# python3 -m site --user-site
"""
--user-base
Print the path to the user base directory.

--user-site
Print the path to the user site-packages directory.
"""
import site

print(site.PREFIXES)
print(site.ENABLE_USER_SITE)
print(site.USER_SITE)
print(site.USER_BASE)
print(site.main())
print(site.getsitepackages())
print(site.getuserbase())
print(site.getusersitepackages())
# print(site.addsitedir(""))
