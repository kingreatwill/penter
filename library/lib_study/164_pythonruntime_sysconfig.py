import sysconfig

# python -m sysconfig

print(sysconfig.get_config_var('Py_ENABLE_SHARED'))

print(sysconfig.get_config_var('LIBDIR'))

print(sysconfig.get_config_vars('posix_home', 'prefix'))

print(sysconfig.get_config_vars())


print(sysconfig.get_scheme_names())

"""
stdlib: directory containing the standard Python library files that are not platform-specific.
platstdlib: directory containing the standard Python library files that are platform-specific.
platlib: directory for site-specific, platform-specific files.
purelib: directory for site-specific, non-platform-specific files.
include: directory for non-platform-specific header files.
platinclude: directory for platform-specific header files.
scripts: directory for script files.
data: directory for data files.
"""
print(sysconfig.get_path_names())

print(sysconfig.get_path("data"))

print(sysconfig.get_paths("nt"))


print(sysconfig.get_python_version())

print(sysconfig.get_platform())
print(sysconfig.is_python_build())
print(sysconfig.get_config_h_filename())
print(sysconfig.get_makefile_filename())

