#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : pypi-flask
Version  : 2.2.2
Release  : 74
URL      : https://files.pythonhosted.org/packages/69/b6/53cfa30eed5aa7343daff36622843688ba8c6fe9829bb2b92e193ab1163f/Flask-2.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/69/b6/53cfa30eed5aa7343daff36622843688ba8c6fe9829bb2b92e193ab1163f/Flask-2.2.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/69/b6/53cfa30eed5aa7343daff36622843688ba8c6fe9829bb2b92e193ab1163f/Flask-2.2.2.tar.gz.asc
Summary  : A simple framework for building complex web applications.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-flask-bin = %{version}-%{release}
Requires: pypi-flask-license = %{version}-%{release}
Requires: pypi-flask-python = %{version}-%{release}
Requires: pypi-flask-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(click)
BuildRequires : pypi(itsdangerous)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(py)
BuildRequires : pypi(werkzeug)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Flask
=====
Flask is a lightweight `WSGI`_ web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around `Werkzeug`_
and `Jinja`_ and has become one of the most popular Python web
application frameworks.

%package bin
Summary: bin components for the pypi-flask package.
Group: Binaries
Requires: pypi-flask-license = %{version}-%{release}

%description bin
bin components for the pypi-flask package.


%package license
Summary: license components for the pypi-flask package.
Group: Default

%description license
license components for the pypi-flask package.


%package python
Summary: python components for the pypi-flask package.
Group: Default
Requires: pypi-flask-python3 = %{version}-%{release}

%description python
python components for the pypi-flask package.


%package python3
Summary: python3 components for the pypi-flask package.
Group: Default
Requires: python3-core
Provides: pypi(flask)
Requires: pypi(click)
Requires: pypi(itsdangerous)
Requires: pypi(jinja2)
Requires: pypi(werkzeug)

%description python3
python3 components for the pypi-flask package.


%prep
%setup -q -n Flask-2.2.2
cd %{_builddir}/Flask-2.2.2
pushd ..
cp -a Flask-2.2.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672272250
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-flask
cp %{_builddir}/Flask-%{version}/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-flask/e32a549b135c4b2b268107adc12d13cca2ca1e8c || :
cp %{_builddir}/Flask-%{version}/docs/license.rst %{buildroot}/usr/share/package-licenses/pypi-flask/4747036caafe4df836d096b9b49d7fdb2782b0ff || :
cp %{_builddir}/Flask-%{version}/examples/javascript/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-flask/e32a549b135c4b2b268107adc12d13cca2ca1e8c || :
cp %{_builddir}/Flask-%{version}/examples/tutorial/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-flask/e32a549b135c4b2b268107adc12d13cca2ca1e8c || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flask

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-flask/4747036caafe4df836d096b9b49d7fdb2782b0ff
/usr/share/package-licenses/pypi-flask/e32a549b135c4b2b268107adc12d13cca2ca1e8c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
